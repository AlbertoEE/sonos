---
allowed-tools: Read, Edit, Write, Bash
description: Lista las ideas pendientes del banco de ideas, deja elegir una y ejecuta el crear-* correspondiente con ella como punto de partida
---

Revisa el banco de ideas pendientes de Sonos y ayuda al DM a desarrollar una.

**Filtro opcional:** $ARGUMENTS  
*(Si $ARGUMENTS contiene un tipo — boss, escena, viaje, set-armadura, set-habilidades — muestra solo ese tipo. Si está vacío, muestra todos.)*

## Carpeta de ideas

`/home/k8s/dev/sonos/vaults/campaign/ideas/`

## Proceso

### Paso 1 — Listar ideas pendientes

1. Lee todos los archivos `.md` de la carpeta de ideas con `Bash`: `ls /home/k8s/dev/sonos/vaults/campaign/ideas/`
2. Para cada archivo, lee su frontmatter y filtra solo los que tienen `status: pending`.
3. Si hay filtro en `$ARGUMENTS`, muestra solo los del tipo indicado.
4. Agrupa las ideas por tipo y muéstralas numeradas:

```
Ideas pendientes

[set-habilidades]
  1. 2026-05-05 — un set que vaya de potenciar ataques básicos (pulsos)
  2. 2026-05-05 — un set de síncopas con ataques cargados y predicts

[set-armadura]
  3. 2026-05-05 — pasiva de set de armadura al tercer pulso consecutivo

[boss] — (vacío)
[escena] — (vacío)
[viaje] — (vacío)
```

5. Si no hay ninguna idea pendiente, responde: `No hay ideas pendientes.` y termina.

### Paso 2 — El usuario elige

Pregunta: **¿Qué idea quieres desarrollar? (número)**

Espera la respuesta antes de continuar.

### Paso 3 — Ejecutar el crear-* correspondiente

1. Lee el archivo de la idea elegida para obtener el tipo y el texto.
2. Según el tipo, lee el archivo de skill correspondiente:

   | type | archivo de skill |
   |------|-----------------|
   | `boss` | `/home/k8s/dev/sonos/.claude/commands/crear-boss.md` |
   | `escena` | `/home/k8s/dev/sonos/.claude/commands/crear-escena.md` |
   | `viaje` | `/home/k8s/dev/sonos/.claude/commands/crear-viaje.md` |
   | `set-armadura` | `/home/k8s/dev/sonos/.claude/commands/crear-set-armadura.md` |
   | `set-habilidades` | `/home/k8s/dev/sonos/.claude/commands/crear-set-habilidades.md` |

3. Ejecuta esa skill **usando el texto de la idea como `$ARGUMENTS`**. Sigue sus instrucciones exactamente igual que si el usuario la hubiera invocado directamente con ese texto.

### Paso 4 — Marcar como completada

Cuando el proceso de creación haya terminado y el usuario haya confirmado que está satisfecho con el resultado, edita el archivo de la idea y cambia `status: pending` por `status: done`.

Confirma con una línea: `Idea marcada como completada: {nombre-de-archivo}`
