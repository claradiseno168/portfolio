// Descarga una sola vez las imágenes del sitio de Webflow y las guarda en /assets.
// Las PNG/JPG pesadas (>150 KB) se convierten a WebP para que el sitio cargue más rápido.
// Lo ejecuta la GitHub Action "Fetch assets"; también funciona en local: `node tools/fetch-assets.mjs`
import { readFile, writeFile, mkdir, access } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const manifest = JSON.parse(await readFile(path.join(root, 'tools/assets.json'), 'utf8'));
await mkdir(path.join(root, 'assets'), { recursive: true });

let sharp = null;
try { sharp = (await import('sharp')).default; } catch { console.warn('sharp no disponible: se guardan los originales'); }

const exists = (p) => access(p).then(() => true, () => false);
let done = 0, skipped = 0;
for (const [id, a] of Object.entries(manifest)) {
  const out = path.join(root, a.local);
  if (await exists(out)) { skipped++; continue; }
  const res = await fetch(a.url);
  if (!res.ok) throw new Error(`${res.status} al descargar ${a.name} (${a.url})`);
  let buf = Buffer.from(await res.arrayBuffer());
  if (a.convert === 'webp') {
    if (!sharp) throw new Error('Hace falta sharp para convertir a WebP');
    buf = await sharp(buf).webp({ quality: 82, effort: 6 }).toBuffer();
  }
  await writeFile(out, buf);
  done++;
  console.log(`✓ ${a.name} → ${a.local} (${Math.round(buf.length / 1024)} KB)`);
}
console.log(`Listo: ${done} descargados, ${skipped} ya existían.`);
