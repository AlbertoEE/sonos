---
name: sonos-rules-task-tracker
description: Trackea tareas pendientes de reglas de Sonos en vaults/system/rules/_meta/tareas.md. Use when adding, listing, triaging, completing, updating, or importing follow-ups/TODOs for Sonos rules work without directly changing rule mechanics.
---

# Sonos Rules Task Tracker

Gestiona el backlog vivo de tareas pendientes de reglas de Sonos.

## Fuente del tracker

Usa siempre este archivo:

```text
vaults/system/rules/_meta/tareas.md
```

Este archivo **no es una regla canónica** y **no debe añadirse** a:

```text
vaults/system/rules/_meta/manifest.yml
```

No recompiles `vaults/system/rules.md` solo por tocar el tracker. Si una tarea se convierte en un cambio real de reglas, usa `sonos-rules-maintainer` para modificar módulos, registrar patch y compilar.

## Cuándo usar esta skill

Úsala cuando el usuario quiera:

- Guardar una tarea pendiente sobre reglas.
- Listar tareas abiertas.
- Revisar el backlog de reglas.
- Marcar una tarea como hecha.
- Asociar una tarea a un módulo o patch.
- Importar follow-ups desde `vaults/system/rules-patches/`.
- Convertir una duda verbal en una tarea accionable.

No la uses para resolver mecánicas directamente salvo que el usuario pida explícitamente trabajar la regla; en ese caso transfiere a `sonos-rules-maintainer`.

## Procedimiento base

1. Lee `vaults/system/rules/_meta/tareas.md` antes de editar.
2. Identifica la intención: `añadir`, `listar`, `completar`, `actualizar`, `triage`, `importar follow-ups`.
3. Haz cambios mínimos y precisos con `edit`.
4. Mantén el formato de checkbox Markdown.
5. Responde con un resumen breve y la ruta del archivo.

## IDs de tareas

Cada tarea persistente debe tener un ID estable:

```markdown
- [ ] **RT-001 · Alta:** texto breve de la tarea.  
  Módulos: [[ruta/al/modulo.md]]  
  Notas: contexto mínimo.
```

Reglas:

- Prefijo: `RT-`.
- Numeración: 3 dígitos (`RT-001`, `RT-002`, ...).
- Para crear una tarea, busca el mayor `RT-###` existente y suma 1.
- No reutilices IDs completados.
- Si el tracker aún no tiene IDs, crea el primero como `RT-001`.

## Categorías

Añade la tarea en la sección más apropiada:

| Sección | Uso |
|---|---|
| `## Inbox` | Entrada rápida cuando no está clara la categoría. |
| `## Flujo y mantenimiento` | Workflow, publicación, patches, compilación, estructura. |
| `## Diseño pendiente` | Reglas o subsistemas que faltan diseñar. |
| `## Clarificaciones pendientes` | Ambigüedades, wording, edge cases, dudas de interpretación. |
| `## Balance pendiente` | Números, costes, dificultad, exploits, ritmo de combate. |
| `## Publicación / documentación` | Printable, guía pública, cheatsheets, ejemplos, docs externas. |
| `## Completadas` | Archivo histórico de tareas cerradas si existe. |

Si una sección contiene `_Empty._`, elimínalo al añadir la primera tarea real.

## Añadir tareas

Cuando el usuario dé una tarea en lenguaje natural:

1. Resume la tarea en una frase accionable.
2. Infiera prioridad solo si es evidente; si no, usa `Media`.
3. Enlaza módulos si el usuario los menciona o si son obvios por el tema.
4. Si no hay módulo claro, usa `Módulos: pendiente`.
5. Añade `Origen:` si proviene de un patch, conversación o archivo.

Formato recomendado:

```markdown
- [ ] **RT-### · Prioridad:** tarea accionable.  
  Módulos: [[relative/path.md]]  
  Notas: contexto breve.  
  Origen: conversación YYYY-MM-DD.
```

Prioridades permitidas:

```text
Alta
Media
Baja
```

No hagas preguntas salvo que no se pueda entender qué tarea guardar.

## Listar tareas

Al listar, no edites. Lee el tracker y responde agrupando por sección:

```text
Abiertas:
- RT-001 [Media] — tarea...
```

Si el usuario pide solo una categoría o prioridad, filtra.

## Completar tareas

Cuando el usuario pida cerrar una tarea:

1. Busca por ID (`RT-###`) o por texto.
2. Cambia `- [ ]` a `- [x]`.
3. Añade debajo:

```markdown
  Resuelta: YYYY-MM-DD. Patch: [[ruta/al/patch.md]].
```

Si no hay patch, usa:

```markdown
  Resuelta: YYYY-MM-DD. Patch: ninguno; tarea de tracking/documentación.
```

No elimines tareas completadas. Si existe `## Completadas`, puedes moverlas ahí solo si el usuario lo pide.

## Actualizar tareas

Para cambiar prioridad, módulos o notas:

- Mantén el mismo ID.
- Edita solo la línea o campos necesarios.
- Conserva contexto útil.

## Importar follow-ups desde patches

Si el usuario pide importar follow-ups:

1. Revisa `vaults/system/rules-patches/*.md`.
2. Extrae checkboxes abiertas de secciones `## Follow-ups`.
3. No dupliques tareas ya existentes por texto similar o mismo origen.
4. Añádelas como tareas con `Origen: [[ruta/al/patch.md]]`.
5. Usa categoría según contenido; si no está claro, `## Inbox`.

## Relación con reglas canónicas

- El tracker puede apuntar a módulos en `vaults/system/rules/`.
- El tracker no sustituye patch notes.
- Una tarea resuelta mediante cambio de reglas debe tener un patch en `vaults/system/rules-patches/`.
- Para cambios mecánicos, carga y sigue `sonos-rules-maintainer`.

## Respuesta final

Sé breve. Ejemplos:

```text
Añadida RT-004 en vaults/system/rules/_meta/tareas.md.
```

```text
Marcada RT-002 como completada en vaults/system/rules/_meta/tareas.md.
```
