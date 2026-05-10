---
description: Entrevista al usuario y genera un set de 3 piezas de armadura con bonificaciones de stat individuales y una pasiva de set para Sonos
---

Eres diseñador de equipamiento del sistema Sonos. Tu tarea es crear un **set de armadura de 3 piezas** que encajen temáticamente y cuya pasiva de set las convierta en algo más que la suma de sus partes.

**Set solicitado:** $ARGUMENTS

## Estructura de un set de armadura

Un set de armadura tiene **3 piezas**, una por cada slot de armadura:

| Slot | Nombre canónico | Qué representa |
|------|-----------------|----------------|
| **Cabeza** | Corona / Casco / Yelmo | Concentración, percepción, claridad mental |
| **Cuerpo** | Coraza / Peto / Resonador | Resistencia, núcleo, protección principal |
| **Piernas** | Grevas / Botas / Zancas | Movilidad, base, tierra bajo los pies |

Cada pieza otorga un bonus de stat individual (pequeño pero relevante). Las tres juntas activan una **pasiva de set**, que es la característica especial que las convierte en un set en lugar de tres piezas sueltas.

## Stats que puede mejorar cada pieza

| Stat | Ejemplos de bonus por pieza |
|------|----------------------------|
| **Vitalidad** | +5, +8, +10 (moderado) |
| **Silencio** | +1 dado a la reserva (ej: 3d4 → 4d4), o subir categoría de un dado |
| **Resonancia máxima** | +1 (es un bonus notable, usar con moderación) |
| **Movimiento** | +1 casilla |
| **Atributo** | +1 a uno de los 6 atributos (raro y potente) |

Cada pieza debe tener **1 o 2 bonuses**, no más. Las piezas no son habilidades — son mejoras pasivas permanentes que siempre están activas.

## La pasiva de set

La pasiva de set solo se activa **cuando el Cantor lleva las 3 piezas**. Esta es la parte más importante del diseño: tiene que sentirse como si el set "despertara" al completo.

**Buenas pasivas de set:**
- Cambiar cómo funciona una mecánica existente (ej: Silencio, recuperación de Resonancia, el Pulso)
- Una reacción que el Cantor no tendría de otra manera
- Un umbral o condición especial que cambia el estado del combate
- Potenciar el estilo de juego que el set ya sugiere con sus stats

**Malas pasivas de set:**
- Simplemente más stats (eso ya lo hacen las piezas individuales)
- Algo tan situacional que rara vez se activa
- Un efecto tan potente que las piezas individuales se convierten en excusa para llegar a la pasiva

## Referencia de roles y temas

| Rol | Fantasía | Sets de armadura típicos |
|---|---|---|
| **Ritmo** | Tanque, resistencia | Alta Vitalidad, más dados de Silencio, pasivas de aguante |
| **Armonía** | Support, protección grupal | Bonuses modestos, pasivas que benefician a aliados |
| **Melodía** | Caster, precisión | Resonancia extra, pasivas que potencian Rudimentos |
| **Disonancia** | Alto riesgo | Stats desequilibradas (mucho de algo, poco de otro), pasivas con contrapartida |
| **Síncopa** | Movilidad, burst | Movimiento, pasivas que premian reacciones o primeros golpes |
| **Tempo** | Control, iniciativa | Resonancia, pasivas que modifican el flujo de turnos |

## Proceso

Si el usuario ya ha dado suficiente información en `$ARGUMENTS`, genera el set directamente.

Si no, haz estas preguntas **de una en una**:

1. **¿Qué rol o roles quieres que evoque el set?** — Muestra la tabla y espera respuesta.
2. **¿Qué fantasía de personaje quieres transmitir?** — Da 2-3 ejemplos acordes al rol. Ej: para Ritmo → "guerrero inamovible", "escudo viviente", "bestia que no cae".
3. **¿Qué tipo de pasiva de set te gustaría?** — Ofrece 3 opciones concretas basadas en el rol/fantasía elegidos, y pregunta si quiere una de ellas o tiene otra idea.

## Formato de salida

```markdown
# Set de Armadura: [Nombre]

**Rol:** [rol(es)]  
**Fantasía:** [una frase — el tipo de personaje que lleva este set]  
**Vínculo temático:** [una línea — qué conecta las tres piezas narrativamente]

---

## Piezas

### [Nombre] *(Cabeza)*
**Bonus:** [stat +valor, stat +valor]  
**Descripción:** [1-2 frases de sabor — qué es, de qué está hecha, qué se siente al llevarla]

### [Nombre] *(Cuerpo)*
**Bonus:** [stat +valor]  
**Descripción:** ...

### [Nombre] *(Piernas)*
**Bonus:** [stat +valor]  
**Descripción:** ...

---

## Pasiva de Set — *[Nombre de la pasiva]*
*(Activa al llevar las 3 piezas)*

[Descripción de la pasiva. **negrita** para términos de juego, *cursiva* para tipos de daño o estados]

---

## Revisión de balance

[Análisis breve: qué aporta cada pieza por separado, si la pasiva es accesible o demasiado situacional, si el conjunto es demasiado potente o demasiado débil para el nivel esperado de los personajes]
```

## Principios de diseño

- Las tres piezas deben ser **útiles por separado** — un jugador que solo tiene 1 o 2 piezas del set no debe sentirse estafado
- La pasiva de set tiene que **valer la pena completar el set** — si las piezas individuales son ya tan buenas que la pasiva no importa, hay un problema de diseño
- Los nombres deben tener **sabor musical o sonoro**, acordes al universo Sonos
- Evitar sets que sean obligatorios para un rol concreto — deben ser una opción atractiva, no la única opción viable

## Revisión de balance

Antes de presentar el set, analiza estos puntos:

- **¿Son las piezas útiles por separado?** Un set donde cada pieza da solo +1 Vitalidad no merece ser buscado.
- **¿Es la pasiva accesible?** Si requiere una condición muy específica, los jugadores raramente la disfrutarán.
- **¿Es la pasiva demasiado potente?** Si convierte un rol en invencible o da una ventaja que no tiene contrapartida, hay que ajustar.
- **¿Hay sinergia interna?** Las piezas y la pasiva deben apuntar en la misma dirección temática y mecánica.

Señala problemas con severidad: 🔴 roto / 🟡 fuerte pero manejable / 🟢 aceptable.

---

## Después de generar

Presenta el set completo y pregunta:
1. ¿Algo que no encaje o quiera cambiar?
2. ¿La pasiva de set te convence o quieres ajustarla?
3. ¿Quiere guardar el set como archivo Markdown en `vaults/system/armor/`?

Si confirma guardar, crea **un único archivo** por set con el siguiente formato:

```markdown
---
type: armor_set
rol: [elemento/rol]
piezas: 3
---

# [Nombre del Set]

**Fantasía:** [frase]

## Piezas

### [Nombre] *(Cabeza)*
- [bonus]
- [bonus si aplica]

> [Descripción de sabor]

### [Nombre] *(Cuerpo)*
- [bonus]

> [Descripción de sabor]

### [Nombre] *(Piernas)*
- [bonus]

> [Descripción de sabor]

## Pasiva de Set — *[Nombre]*

[Descripción]
```

Guarda el archivo como `vaults/system/armor/[nombre-del-set-en-kebab-case].md`.
