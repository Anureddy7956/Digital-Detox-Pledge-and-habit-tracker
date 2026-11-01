// Builds the deployable single-file index.html from the readable src/index.html.
// Only CSS/JS whitespace and identifiers are minified; there are no runtime dependencies.
import { readFileSync, writeFileSync } from 'node:fs';
import { transform } from 'esbuild';

const BUDGET = 100 * 1024;
const src = readFileSync(new URL('./src/index.html', import.meta.url), 'utf8');
const STYLE = /<style>([\s\S]*?)<\/style>/, SCRIPT = /<script>([\s\S]*?)<\/script>/;

const css = await transform(src.match(STYLE)[1], { loader: 'css', minify: true });
const js = await transform(src.match(SCRIPT)[1], { loader: 'js', minify: true, target: 'es2022' });
const out = src
  .replace(STYLE, () => `<style>${css.code.trim()}</style>`)
  .replace(SCRIPT, () => `<script>${js.code.trim()}</script>`)
  .replace(/>\n+</g, '><');

writeFileSync(new URL('./index.html', import.meta.url), out);
const size = Buffer.byteLength(out);
console.log(`index.html: ${(size / 1024).toFixed(1)} KB (budget ${BUDGET / 1024} KB)`);
if (size >= BUDGET) { console.error('Over the 100 KB budget'); process.exit(1); }
