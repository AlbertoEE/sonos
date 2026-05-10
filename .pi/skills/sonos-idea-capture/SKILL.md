---
name: sonos-idea-capture
description: Captura ideas rápidas de Sonos, las clasifica como boss, escena, viaje, set-armadura, set-habilidades u objeto, y las guarda como markdown pendiente en vaults/campaign/ideas/ o vaults/system/ideas/. Use when the DM wants to save a quick idea, note, seed, concept, encounter, item recipe, system idea, or future content prompt without developing it yet.
---

# Sonos Idea Capture

Captura ideas rápidas para Sonos y guárdalas en el banco de ideas sin desarrollarlas.

Este skill reemplaza el prompt antiguo:

```text
.pi/prompts/idea.md
```

## Objetivo

El usuario suelta una idea en bruto. Tu trabajo es:

1. Clasificarla.
2. Guardarla como archivo markdown pendiente.
3. Responder con una sola línea de confirmación.

No desarrolles la idea. No la mejores. No inventes detalles.

## Carpetas de destino

Hay dos bancos de ideas:

```text
vaults/campaign/ideas/   # ideas de campaña: bosses, escenas, viajes, secretos, sesiones
vaults/system/ideas/     # ideas de sistema: reglas, cartas, sets, objetos, mecánicas
```

Crea la carpeta elegida si no existe.

### Enrutado por defecto

- Guarda en `vaults/campaign/ideas/` las ideas de campaña: `boss`, `escena`, `viaje`, NPCs, secretos, sesiones o contenido narrativo.
- Guarda en `vaults/system/ideas/` las ideas de sistema: `set-habilidades`, `set-armadura`, reglas, cartas, mecánicas u objetos de diseño general.
- Para `objeto`, usa `vaults/system/ideas/` si es un objeto/receta de diseño general; usa `vaults/campaign/ideas/` si es loot, tesoro, pista o elemento específico de una sesión/campaña.
- Para `otro`, si no está claro el banco, pregunta una sola vez.

## Tipos permitidos

| Tipo | Cuándo usarlo |
|---|---|
| `boss` | enemigos importantes, jefes, antagonistas, combate especial |
| `escena` | lugar, entrada, ambiente, descripción, sitio concreto |
| `viaje` | trayecto, ruta, camino, desplazamiento, eventos de viaje |
| `set-armadura` | armadura, casco, peto, grevas, pieza defensiva, bonus de set |
| `set-habilidades` | habilidades, cartas, rudimentos, fundamentos, set de cartas |
| `objeto` | ítems, recetas, consumibles, equipo, herramienta, loot, crafting |
| `otro` | idea válida pero todavía no clasificable |

## Clasificación

Determina el tipo a partir del texto del usuario.

### Prefijo explícito

Si la idea empieza con uno de estos prefijos de tipo, úsalo directamente y elimina el prefijo del texto guardado:

```text
boss:
escena:
viaje:
set-armadura:
set-habilidades:
objeto:
otro:
```

También acepta un prefijo de banco, que debe eliminarse del texto guardado:

```text
campaign:
campaña:
system:
sistema:
```

Se pueden combinar, por ejemplo:

```text
system: objeto: cinturón que altera el coste de Resonancia
campaña: escena: mercado nocturno bajo la lluvia
```

Acepta mayúsculas/minúsculas.

### Palabras clave

| Tipo | Palabras clave |
|---|---|
| `boss` | enemigo, jefe, boss, combate, antagonista, criatura élite |
| `escena` | lugar, entrada, sitio, ambiente, escena, descripción |
| `viaje` | trayecto, camino, destino, ruta, viaje, desplazamiento |
| `set-armadura` | armadura, pieza, casco, yelmo, corona, peto, coraza, grevas, botas, defensivo |
| `set-habilidades` | habilidad, skill, rudimento, fundamento, carta, set de habilidades, pulso, síncopa, ataque |
| `objeto` | objeto, ítem, item, receta, consumible, poción, cinturón, herramienta, crafting, loot |

Si no puedes distinguir entre `set-armadura`, `set-habilidades` y `objeto`, pregunta **una sola vez**.

Si no encaja en nada, pregunta **una sola vez** si debe ser `boss`, `escena`, `viaje`, `set-armadura`, `set-habilidades`, `objeto` u `otro`.

Si el tipo está claro pero el banco no, pregunta **una sola vez** si debe guardarse en `campaign` o `system`.

## Nombre de archivo

Genera el nombre con:

```text
YYYY-MM-DD-{slug}.md
```

Reglas:

- Fecha: fecha actual.
- Slug: 3–7 palabras significativas del texto.
- Minúsculas.
- Sin tildes.
- Sin artículos/preposiciones si se puede.
- Separadas por guiones.

Ejemplos:

```text
2026-05-10-set-potenciar-pulsos.md
2026-05-10-boss-coro-huesos.md
2026-05-10-cinturon-pociones-gratis.md
```

Si el archivo ya existe en la carpeta elegida, añade sufijo incremental:

```text
-2
-3
```

## Contenido del archivo

Usa este formato exacto:

```markdown
---
type: {tipo}
date: {fecha}
status: pending
source: sonos-idea-capture
---

{texto de la idea tal como el usuario lo expresó, sin prefijos explícitos si los había}
```

No añadas análisis, propuestas ni desarrollo.

## Respuesta final

Después de guardar, responde con una sola línea:

```text
Idea guardada en {banco} como {tipo}: {nombre-de-archivo}
```

## Integración con otros skills

Las ideas guardadas pueden desarrollarse después con:

| Tipo | Skill recomendado |
|---|---|
| `boss` | `sonos-boss-designer` |
| `escena` | `sonos-scene-describer` |
| `viaje` | `sonos-travel-planner` |
| `set-armadura` | `sonos-armor-set-designer` |
| `set-habilidades` | `sonos-skill-set-designer` |
| `objeto` | `sonos-item-designer` |

No ejecutes esos skills desde aquí salvo que el usuario lo pida explícitamente. Este skill solo captura.

## Qué no hacer

- No desarrollar la idea.
- No crear contenido final.
- No hacer múltiples preguntas.
- No guardar fuera de `vaults/campaign/ideas/` o `vaults/system/ideas/`.
- No cambiar ideas existentes salvo para evitar colisión de nombre.
