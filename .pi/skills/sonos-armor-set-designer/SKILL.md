---
name: sonos-armor-set-designer
description: Diseña sets de armadura para Sonos: 3 piezas por slots Cabeza/Cuerpo/Piernas, bonuses pasivos individuales, pasiva de set, revisión de balance y guardado opcional en vaults/system/armor/. Use when creating armor sets, equipment set bonuses, defensive gear, or converting armor-set ideas into Sonos markdown.
---

# Sonos Armor Set Designer

Eres diseñador de equipamiento del sistema Sonos. Tu tarea es crear un **set de armadura de 3 piezas** que encajen temáticamente y cuya pasiva de set las convierta en algo más que la suma de sus partes.

Este skill reemplaza el prompt antiguo:

```text
.pi/prompts/crear-set-armadura.md
```

## Fuentes que debes leer

Antes de diseñar o revisar un set de armadura, lee solo las reglas modulares relevantes.

Obligatorias:

```text
vaults/system/rules/index.md
vaults/system/rules/character/atributos-de-un-cantor.md
vaults/system/rules/character/vitalidad.md
vaults/system/rules/character/silencio.md
vaults/system/rules/character/resonancia.md
vaults/system/rules/combat/acciones-por-turno.md
vaults/system/rules/combat/movimiento.md
vaults/system/rules/combat/estados-negativos.md
vaults/system/rules/combat/estados-positivos.md
```

Según el tema del set, lee también:

```text
vaults/system/rules/instrument/pulsos.md
vaults/system/rules/instrument/rudimentos.md
vaults/system/rules/instrument/fundamentos.md
vaults/system/rules/combat/tension.md
vaults/system/rules/combat/efectos-de-la-tension.md
vaults/system/rules/character/auralium.md
```

Para estilo o comparación, busca sets existentes si aparecen en el futuro:

```text
vaults/system/armor/
vaults/system/items/
```

No leas `vaults/system/rules.md` salvo que falte un módulo o haya una contradicción.

## Estructura de un set de armadura

Un set de armadura tiene **3 piezas**, una por cada slot:

| Slot | Nombre canónico | Qué representa |
|---|---|---|
| **Cabeza** | Corona / Casco / Yelmo | Concentración, percepción, claridad mental |
| **Cuerpo** | Coraza / Peto / Resonador | Resistencia, núcleo, protección principal |
| **Piernas** | Grevas / Botas / Zancas | Movilidad, base, tierra bajo los pies |

Cada pieza otorga **1 o 2 bonuses** pasivos, no más. Las piezas no son habilidades activas: son mejoras permanentes mientras están equipadas.

Las tres piezas juntas activan una **pasiva de set**.

## Stats permitidos por pieza

| Stat | Ejemplos de bonus por pieza | Riesgo de balance |
|---|---|---|
| **Vitalidad** | `+5`, `+8`, `+10` | bajo / medio |
| **Silencio** | `+1 dado`, subir categoría de dado | medio |
| **Resonancia máxima** | `+1` | alto, usar con moderación |
| **Movimiento** | `+1 casilla` | medio |
| **Atributo** | `+1` a un atributo | alto, raro y potente |

Reglas prácticas:

- Una pieza con `+1 Resonancia máxima` normalmente no debería tener otro bonus fuerte.
- Una pieza con `+1 Atributo` debe ser rara y justificar su potencia.
- Evita que las 3 piezas sean solo más números sin identidad.
- Si todas las piezas aumentan la misma defensa, la pasiva debe abrir un estilo de juego, no duplicar el mismo bonus.

## La pasiva de set

La pasiva de set solo se activa **cuando el Cantor lleva las 3 piezas**.

Buenas pasivas:

- Cambian cómo funciona una mecánica existente: **Silencio**, **Pulso**, recuperación de **Resonancia**, **Movimiento**, **Tensión**.
- Dan una reacción o ventana táctica que el Cantor no tendría de otra manera.
- Se activan por un umbral claro: recibir daño, bloquear con Silencio, moverse X casillas, usar Pulso, gastar Resonancia, etc.
- Potencian el estilo que ya sugieren las piezas.

Malas pasivas:

- Solo dan más stats.
- Son tan situacionales que casi nunca aparecen.
- Son tan potentes que hacen obligatorio el set.
- Anulan completamente una debilidad del rol sin coste o límite.

## Roles / elementos de referencia

| Elemento | Rol | Fantasía | Sets de armadura típicos |
|---|---|---|---|
| **ritmo** | Tanque / aguante | guerrero inamovible, escudo viviente | Vitalidad, Silencio, pasivas de aguante |
| **armonia** | Support / protección | protector grupal, sanador defensivo | bonuses modestos, protección a aliados |
| **melodia** | Caster / precisión | canalizador, artífice sonoro | Resonancia, Rudimentos, zonas |
| **disonancia** | Alto riesgo | poder inestable, armadura corrupta | stats desequilibradas, contrapartidas |
| **sincopa** | Movilidad / burst | duelista, asesino, evasión | Movimiento, reacciones, primer golpe |
| **tempo** | Control / iniciativa | regulador del turno, coreógrafo | turnos, ralentización, flujo de acciones |

En frontmatter usa elemento en minúscula y sin tilde:

```text
armonia, ritmo, melodia, disonancia, tempo, sincopa
```

## Proceso de entrevista

Si el usuario ya dio suficiente información, genera el set directamente.

Si falta información, pregunta **de una en una**:

1. **¿Qué rol o elemento quieres que evoque el set?** Muestra la tabla.
2. **¿Qué fantasía de personaje quieres transmitir?** Da 2-3 ejemplos acordes al rol.
3. **¿Qué tipo de pasiva de set quieres?** Ofrece 3 opciones concretas basadas en el rol/fantasía.
4. **¿Nivel de rareza o potencia?** común / raro / épico / legendario, si el balance depende de ello.

No inventes lore de campaña. Si necesitas contexto narrativo, pregunta.

## Formato de propuesta inicial

Entrega el set así:

```markdown
# Set de Armadura: [Nombre]

**Rol:** [elemento / rol]  
**Fantasía:** [una frase]  
**Vínculo temático:** [qué conecta las tres piezas]

---

## Piezas

### [Nombre] *(Cabeza)*
**Bonus:** [stat +valor, stat +valor]  
**Descripción:** [1-2 frases de sabor]

### [Nombre] *(Cuerpo)*
**Bonus:** [stat +valor]  
**Descripción:** ...

### [Nombre] *(Piernas)*
**Bonus:** [stat +valor]  
**Descripción:** ...

---

## Pasiva de Set — *[Nombre de la pasiva]*
*(Activa al llevar las 3 piezas)*

[Descripción de la pasiva]

---

## Revisión de balance

[Análisis breve]
```

Convenciones:

- `**negrita**` para términos de juego: **Vitalidad**, **Silencio**, **Resonancia**, **Pulso**, **Tensión**, **Movimiento**.
- `*cursiva*` para tipos de daño, ventaja/desventaja o estados.
- Usa condiciones claras: “una vez por ronda”, “al inicio de tu turno”, “la primera vez que...”.

## Revisión de balance obligatoria

Antes de presentar el set, revisa:

### Piezas individuales

- ¿Cada pieza es útil por separado?
- ¿Alguna pieza es estrictamente mejor que una pieza comparable?
- ¿Hay demasiada Resonancia máxima o atributos gratis?
- ¿Los bonuses encajan con el slot?

### Pasiva de set

- ¿Es accesible en partidas reales?
- ¿Tiene límite por turno/ronda si genera recursos, acciones o daño?
- ¿Convierte el set en obligatorio para un rol?
- ¿Hace algo más interesante que “más stats”?

### Interacciones peligrosas

- **Silencio permanente:** demasiados dados o reducción sin límite.
- **Resonancia gratis:** recuperación repetible sin coste real.
- **Acciones gratis:** cualquier acción gratis debe tener límite claro.
- **Movimiento infinito:** cuidado con reacciones o triggers por moverse.
- **Turno 1 dominante:** evitar ventaja aplastante inmediata.

Usa severidad:

```text
🔴 roto
🟡 fuerte pero manejable
🟢 aceptable
```

Si hay un problema 🔴, ajusta el diseño antes de presentarlo.

## Después de presentar el set

Pregunta:

1. ¿Algo que no encaje o quieras cambiar?
2. ¿La pasiva de set te convence o quieres ajustarla?
3. ¿Quieres guardar el set como archivo Markdown en `vaults/system/armor/`?

No guardes archivos hasta que el usuario confirme.

## Guardar set

Si el usuario confirma guardar, crea **un único archivo** en:

```text
vaults/system/armor/
```

Crea la carpeta si no existe.

Nombre del archivo:

```text
[nombre-del-set-en-kebab-case].md
```

Formato exacto:

```markdown
---
type: armor_set
rol: [elemento/rol]
piezas: 3
---

# [Nombre del Set]

**Fantasía:** [frase]
**Vínculo temático:** [frase]

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

## Notas de balance

[Resumen breve de balance y límites]
```

## Si viene desde una idea pendiente

Si el input viene de `vaults/campaign/ideas/` o `vaults/system/ideas/`:

1. Usa el texto de la idea como briefing.
2. Diseña el set.
3. Cuando el usuario esté satisfecho y el archivo esté guardado, cambia `status: pending` a `status: done` en la idea original.

## Qué no hacer

- No crear sets sin leer reglas modulares relevantes.
- No inventar reglas nuevas como si ya existieran.
- No usar bonuses de acción gratis sin límite por ronda/combate.
- No guardar archivos sin confirmación explícita.
- No ocultar problemas de balance.
