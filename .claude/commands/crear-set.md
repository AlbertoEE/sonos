---
allowed-tools: Read
description: Entrevista al usuario y genera un set de 6 habilidades coherentes (2 fundamentos + 4 rudimentos) para Sonos
---

Eres diseñador de habilidades del sistema Sonos. Tu tarea es crear un **set de 6 habilidades** que funcionen juntas como el kit de un personaje de MOBA.

**Set solicitado:** $ARGUMENTS

## Estructura de un set

- **2 Fundamentos** — pasivas siempre activas, coste 0
- **4 Rudimentos** — activas que cuestan Resonancia (`0`, `1`, `2`, `3`, `4`, `M` = mitad del máximo, `X` = variable, `-` = sin coste fijo)

Las 6 deben compartir un **tema** y una **mecánica interna** que las vincule — igual que las habilidades de un campeón de MOBA.

## Referencia de roles

| Rol | Fantasía | Mecánicas típicas |
|---|---|---|
| **Armonía** | Support, escudos, curación | Silencio extra, auras, Resonancia compartida |
| **Ritmo** | Tanque, daño sostenido | Empujes, múltiples golpes, aguante |
| **Melodía** | Mago, área, estados | Zonas persistentes, veneno, encadenamiento |
| **Disonancia** | Alto riesgo / alta recompensa | Lanzar moneda, intercambios, azar controlado |
| **Tempo** | Control, interrupciones | Stuns, turnos extra, ralentizaciones |
| **Síncopa** | Burst, asesino, movilidad | Ejecutar, reacciones, combos de daño verdadero |

Un set puede ser de **un solo rol** o de **dos roles combinados** (ej: Ritmo + Síncopa para un bruiser).

## Proceso

Si el usuario ya ha dado suficiente información en `$ARGUMENTS`, genera el set directamente.

Si no, haz estas preguntas **de una en una**:

1. **¿Qué rol o roles quieres?** — Muestra la tabla y espera respuesta.
2. **¿Tienes un subtema?** — Da 2-3 ejemplos acordes al rol elegido. Ej: para Armonía → "escudos reactivos", "resonancia compartida", "auras de área".
3. **¿Qué mecánica interna quieres que los conecte?** — Ej: acumular cargas, marcar y explotar, crear zonas, gestionar un recurso secundario. Si no tiene idea, propón tú una basándote en lo anterior y confirma.
4. **¿Cómo quieres que se sienta jugarlo?** — Agresivo y rápido / lento y de control / reactivo (muchas reacciones) / de setup (preparar antes de explotar).

## Formato de salida

```markdown
# Set: [Nombre]

**Rol:** [rol(es)]  
**Subtema:** [subtema]  
**Mecánica central:** [una línea — qué hilo conecta las 6 habilidades]

---

## Fundamentos

### [Nombre]
**Elemento:** [elemento]
**Base:** [descripción. **negrita** para términos de juego, *cursiva* para tipos de daño o estados]
**Evolucionado:** [versión mejorada — amplía sin cambiar por completo]

### [Nombre]
**Elemento:** [elemento]
**Base:** ...
**Evolucionado:** ...

---

## Rudimentos

### [Nombre]
**Elemento:** [elemento]
**Coste:** [valor]
**Base:** ...
**Evolucionado:** ...

[× 4 rudimentos]

---

## Loop de juego

[2-3 frases: qué activa qué, cuál es el combo principal, cómo los fundamentos potencian los rudimentos]
```

## Stats de referencia para las descripciones

Las habilidades no usan daño plano — escalan con las stats del personaje:

| Notación | Significado |
|---|---|
| `[AT]` | Suma el Atributo Total una vez |
| `[2AT]`, `[3AT]` | Suma el AT N veces |
| `[DI]` | Tira el Dado de Instrumento una vez |
| `[1DI]`, `[2DI]` | Tira el DI N veces |
| `[DI+AT]` | Tira el DI y suma el AT |
| `[2DI+AT]` | Tira el DI dos veces y suma el AT |
| `[1d4]`, `[1d6]`... | Dados fijos independientes del instrumento |

**DI** representa el daño bruto del instrumento (depende del instrumento equipado).  
**AT** representa la maestría del personaje con su instrumento (sube con la progresión).

Usa siempre esta notación entre corchetes en las descripciones. Elige la escala según la intención:
- Daño moderado y frecuente → `[DI]` o `[AT]`
- Daño principal de un rudimento → `[DI+AT]`
- Daño alto o de burst → `[2DI+AT]` o `[2AT]`
- Efectos secundarios menores → `[AT]` o `[1d4]`
- Daño aleatorio con varianza → `[1dX AT]` (ej: `[1d4 AT]` = tira 1d4 veces el AT)

## Principios de diseño

- Los fundamentos deben ser relevantes en casi cualquier turno, no solo en casos concretos
- Al menos un rudimento debe costar 0 o 1 — el set necesita ser jugable con poca Resonancia
- Cada habilidad hace algo único; no repetir el mismo efecto en dos cartas distintas
- El Evolucionado amplía la habilidad sin cambiarla — debe seguir siendo reconocible
- Si hay dos roles, cada uno aporta algo diferente al set: no duplicar función
- Los nombres tienen sabor musical o sonoro, acordes con el universo Sonos

## Después de generar

Presenta el set completo y pregunta:
1. ¿Algo que no encaje o quiera cambiar?
2. ¿Quiere guardar las cartas como archivos Markdown en `vaults/system/cards/`?

Si confirma guardar, genera cada carta en el formato exacto del vault:

```markdown
---
type: [fundamento / rudimento]
element: [elemento]
coste: "[valor]"
---

# [Nombre]

## Base
[descripción]

## Evolucionado
[descripción]
```

Recuérdale que tras guardar debe ejecutar `node card-generator/build-data.js` para regenerar el JSON.
