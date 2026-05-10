---
description: Captura una idea rápida y la clasifica para usar después con crear-boss, crear-escena, crear-viaje, crear-set-armadura o crear-set-habilidades
---

Captura la siguiente idea en el banco de ideas de Sonos.

**Idea:** $ARGUMENTS

## Carpeta de destino

`/home/k8s/dev/sonos/vaults/campaign/ideas/`

## Instrucciones

1. **Determina el tipo** a partir de `$ARGUMENTS`:

   | Tipo | Palabras clave |
   |------|---------------|
   | `boss` | enemigo, jefe, boss, combate, antagonista |
   | `escena` | lugar, entrada, sitio, ambiente, escena |
   | `viaje` | trayecto, camino, destino, ruta, viaje |
   | `set-armadura` | armadura, pieza, casco, peto, guantes, defensivo |
   | `set-habilidades` | habilidad, skill, rudimento, fundamento, carta, set de habilidades, síncopas, ataques |

   - Si el texto empieza con `boss:`, `escena:`, `viaje:`, `set-armadura:` o `set-habilidades:` (con o sin mayúscula), usa esa categoría y extrae el texto que sigue.
   - Si no puedes determinarlo con seguridad entre `set-armadura` y `set-habilidades`, pregunta **una sola vez** antes de continuar.
   - Si no encaja en ninguna categoría, pregunta **una sola vez** cuál de las cinco es.

2. **Genera el nombre de archivo** con el formato `YYYY-MM-DD-{slug}.md`:
   - Fecha: hoy.
   - Slug: 3–5 palabras significativas del texto, minúsculas, separadas por guiones (sin artículos ni preposiciones). Ejemplo: `set-potenciar-pulsos`.

3. **Crea el archivo** en la carpeta de destino con este contenido:

```markdown
---
type: {tipo}
date: {fecha}
status: pending
---

{texto de la idea tal como el usuario lo expresó}
```

4. **Responde con una sola línea:** `Idea guardada como {tipo}: {nombre-de-archivo}`

No desarrolles la idea. No hagas preguntas adicionales tras guardar.
