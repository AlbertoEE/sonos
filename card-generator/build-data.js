#!/usr/bin/env node
// Converts vaults/system/cards/fundamentos/*.md + rudimentos/*.md → card-generator/data.json
// Usage: node build-data.js
// The MD files are the source of truth; run this after editing them.

const fs = require('fs');
const path = require('path');

const VAULT_DIR = path.join(__dirname, '../vaults/system/cards');
const OUTPUT = path.join(__dirname, 'data.json');

function mdToHtml(text) {
  return text
    .replace(/\*\*\*(.+?)\*\*\*/g, '<b><i>$1</i></b>')
    .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
    .replace(/\*(.+?)\*/g, '<i>$1</i>');
}

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]+?)\n---\n([\s\S]*)$/);
  if (!match) return { meta: {}, body: content };

  const meta = {};
  for (const line of match[1].split('\n')) {
    const colon = line.indexOf(':');
    if (colon === -1) continue;
    const key = line.slice(0, colon).trim();
    let val = line.slice(colon + 1).trim();
    if (val.startsWith('[') && val.endsWith(']')) {
      val = val.slice(1, -1).split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
    } else {
      val = val.replace(/^["']|["']$/g, '');
    }
    meta[key] = val;
  }
  return { meta, body: match[2] };
}

function parseCard(filePath, defaultType) {
  const content = fs.readFileSync(filePath, 'utf8');
  const { meta, body } = parseFrontmatter(content);

  const nameMatch = body.match(/^#\s+(.+)/m);
  const name = nameMatch ? nameMatch[1].trim() : path.basename(filePath, '.md');

  const element = Array.isArray(meta.element) ? meta.element : [meta.element];
  const bucket = meta.bucket || element[0];
  const type = meta.type || defaultType;

  const sections = {};
  let current = null;
  for (const line of body.split('\n')) {
    if (line.startsWith('## ')) {
      current = line.slice(3).trim().toLowerCase();
      sections[current] = [];
    } else if (current && line.trim()) {
      sections[current].push(line);
    }
  }

  const baseText = (sections['base'] || []).join(' ').trim();
  const evolText = (sections['evolucionado'] || []).join(' ').trim();

  return {
    bucket,
    card: {
      name,
      type,
      element,
      coste: meta.coste || '0',
      base: { description: mdToHtml(baseText) },
      evolved: { description: mdToHtml(evolText) },
    },
  };
}

function buildSection(dir, defaultType) {
  const result = {};
  for (const file of fs.readdirSync(dir).filter(f => f.endsWith('.md'))) {
    const { bucket, card } = parseCard(path.join(dir, file), defaultType);
    if (!result[bucket]) result[bucket] = [];
    result[bucket].push(card);
  }
  return result;
}

const fundamentos = buildSection(path.join(VAULT_DIR, 'fundamentos'), 'fundamento');
const rudimentos = buildSection(path.join(VAULT_DIR, 'rudimentos'), 'rudimento');

// Preserve estados from existing data.json
let estados = {};
if (fs.existsSync(OUTPUT)) {
  try { estados = JSON.parse(fs.readFileSync(OUTPUT, 'utf8')).estados || {}; }
  catch (_) {}
}

fs.writeFileSync(OUTPUT, JSON.stringify({ fundamentos, rudimentos, estados }, null, 2), 'utf8');
const nF = Object.values(fundamentos).flat().length;
const nR = Object.values(rudimentos).flat().length;
console.log(`data.json actualizado (${nF} fundamentos, ${nR} rudimentos)`);
