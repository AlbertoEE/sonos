---
name: sonos-idea-reviewer
description: Revisa los bancos de ideas pendientes de Sonos en campaign y system, muestra ideas por tipo, deja elegir una y la desarrolla usando el skill adecuado. Use when the DM wants to review pending ideas, pick an idea to develop, process the idea backlog, or continue from a saved campaign or system idea.
---

# Sonos Idea Reviewer

Revisa los bancos de ideas pendientes de Sonos y ayuda al DM a desarrollar una.

Este skill reemplaza el prompt antiguo:

```text
.pi/prompts/revisar-ideas.md
```

## Carpetas de ideas

Hay dos bancos de ideas:

```text
vaults/campaign/ideas/   # ideas de campaña: bosses, escenas, viajes, secretos, sesiones
vaults/system/ideas/     # ideas de sistema: reglas, cartas, sets, objetos, mecánicas
```

## Tipos soportados

| Tipo | Skill recomendado |
|---|---|
| `boss` | `sonos-boss-designer` |
| `escena` | `sonos-scene-describer` |
| `viaje` | `sonos-travel-planner` |
| `set-armadura` | `sonos-armor-set-designer` |
| `set-habilidades` | `sonos-skill-set-designer` |
| `objeto` | `sonos-item-designer` |
| `otro` | preguntar qué hacer |

## Flujo obligatorio

### Paso 1 — Listar ideas pendientes

1. Lista los archivos `.md` en ambas carpetas:

```text
vaults/campaign/ideas/
vaults/system/ideas/
```

2. Lee el frontmatter de cada archivo.
3. Filtra solo ideas con:

```yaml
status: pending
```

4. Si el usuario dio un filtro, muestra solo ese tipo o ese banco.

Filtros de tipo válidos:

```text
boss, escena, viaje, set-armadura, set-habilidades, objeto, otro
```

Filtros de banco válidos:

```text
campaign, campaña, system, sistema
```

5. Agrupa por banco y tipo, y muestra una lista numerada global:

```text
Ideas pendientes

[campaign / boss]
  1. 2026-05-05 — boss del coro de huesos

[campaign / escena]
  2. 2026-05-06 — entrada al faro inundado

[system / set-habilidades]
  3. 2026-05-05 — un set que vaya de potenciar ataques básicos
  4. 2026-05-05 — síncopas con ataques cargados y predicts

[system / objeto]
  5. 2026-05-10 — cinturón de pociones gratis

[campaign / viaje] — vacío
[system / set-armadura] — vacío
```

Para cada idea, muestra:

- número;
- fecha;
- resumen de una línea del cuerpo;
- nombre de archivo si ayuda a distinguir.

Si no hay ideas pendientes, responde:

```text
No hay ideas pendientes.
```

y termina.

### Paso 2 — Elegir idea

Pregunta:

```text
¿Qué idea quieres desarrollar? (número)
```

Espera respuesta antes de continuar.

### Paso 3 — Leer la idea elegida

Lee el archivo completo. Extrae:

- `type`
- `date`
- `status`
- cuerpo de la idea
- ruta del archivo
- banco (`campaign` si está en `vaults/campaign/ideas/`, `system` si está en `vaults/system/ideas/`)

Si `status` no es `pending`, avisa y pide confirmación antes de desarrollarla.

### Paso 4 — Desarrollar con el skill adecuado

Usa el flujo correspondiente al tipo:

| type | Acción |
|---|---|
| `boss` | Cargar/seguir `sonos-boss-designer` con el texto de la idea como briefing |
| `escena` | Cargar/seguir `sonos-scene-describer` |
| `viaje` | Cargar/seguir `sonos-travel-planner` |
| `set-armadura` | Cargar/seguir `sonos-armor-set-designer` |
| `set-habilidades` | Cargar/seguir `sonos-skill-set-designer` |
| `objeto` | Cargar/seguir `sonos-item-designer` |
| `otro` | Preguntar a qué tipo debe convertirse antes de continuar |

Importante: en Pi, si no puedes invocar técnicamente otro skill como comando interno, **lee su `SKILL.md` con la herramienta `read` y sigue sus instrucciones**.

Rutas de skills:

```text
.pi/skills/sonos-boss-designer/SKILL.md
.pi/skills/sonos-scene-describer/SKILL.md
.pi/skills/sonos-travel-planner/SKILL.md
.pi/skills/sonos-armor-set-designer/SKILL.md
.pi/skills/sonos-skill-set-designer/SKILL.md
.pi/skills/sonos-item-designer/SKILL.md
```

### Paso 5 — Marcar como completada

Solo cuando el usuario confirme que está satisfecho con el resultado final, edita el archivo de la idea y cambia:

```yaml
status: pending
```

a:

```yaml
status: done
```

Añade, si no existe:

```yaml
completed_date: YYYY-MM-DD
```

Si se generó un archivo final, añade también:

```yaml
output: ruta/del/archivo.md
```

Confirma con una línea:

```text
Idea marcada como completada: {nombre-de-archivo}
```

## Si el desarrollo no termina

Si el usuario no queda satisfecho o quiere dejarlo para luego:

- No cambies `status`.
- Opcionalmente añade notas solo si el usuario lo pide.

## Reglas importantes

- No desarrolles todas las ideas de golpe.
- No marques una idea como `done` solo porque generaste un borrador; espera confirmación.
- No inventes detalles que contradigan la idea original.
- Si el skill correspondiente requiere leer reglas modulares, hazlo.
- Si el tipo es ambiguo, pregunta antes de desarrollar.
- Si faltan skills, dilo claramente y ofrece crearlos.

## Comandos útiles

Listar ideas:

```bash
find vaults/campaign/ideas vaults/system/ideas -maxdepth 1 -type f -name '*.md' | sort
```

Buscar pendientes rápido:

```bash
rg -n "status: pending" vaults/campaign/ideas vaults/system/ideas
```

## Formato de interacción recomendado

Primera respuesta tras listar:

```markdown
Ideas pendientes

[system / set-habilidades]
1. `vaults/system/ideas/2026-05-05-set-potenciar-pulsos.md` — set que potencia ataques básicos / Pulsos

[campaign / objeto]
2. `vaults/campaign/ideas/2026-05-10-cinturon-pociones.md` — cinturón para usar pociones sin gastar PA

¿Qué idea quieres desarrollar? (número)
```
