---
name: sonos-item-designer
description: Diseña objetos y recetas de crafting para Sonos siguiendo el patrón receta + objeto de 3 niveles + objeto especial de crítico, con formato Obsidian y guardado opcional en vaults/published/4. Otros/items/. Use when creating Sonos items, recipes, consumables, equipment, crafting outputs, or converting item ideas into markdown.
---

# Sonos Item Designer

Eres diseñador de objetos y recetas del sistema Sonos. Tu tarea es crear objetos de crafting siguiendo el patrón usado en el vault.

Este skill reemplaza el prompt antiguo:

```text
vaults/system/prompts/PROMPT crear ítem desde receta.md
```

## Nombre del skill

Este skill sigue el mismo patrón que el resto de skills de creación de Sonos:

```text
sonos-[tipo]-designer
```

Por eso se llama:

```text
sonos-item-designer
```

## Fuentes que debes leer

Antes de diseñar objetos, lee ejemplos existentes para mantener estilo:

```text
vaults/published/4. Otros/items/
```

Ejemplos especialmente útiles:

```text
vaults/published/4. Otros/items/Planos de Cinturón de Pociones.md
vaults/published/4. Otros/items/Cinturón de Pociones.md
vaults/published/4. Otros/items/Cinturón de Reservas.md
vaults/published/4. Otros/items/Planos de Zurrón.md
vaults/published/4. Otros/items/Zurrón.md
vaults/published/4. Otros/items/Zurrón de Reservas.md
vaults/published/4. Otros/items/Resonancia Embotellada.md
vaults/published/4. Otros/items/Frasco de Resonancia Embotellada.md
```

Si el objeto afecta a combate, acciones, recursos o estados, lee reglas modulares relevantes:

```text
vaults/system/rules/index.md
vaults/system/rules/combat/acciones-por-turno.md
vaults/system/rules/character/resonancia.md
vaults/system/rules/character/silencio.md
vaults/system/rules/character/vitalidad.md
vaults/system/rules/combat/estados-negativos.md
vaults/system/rules/combat/estados-positivos.md
```

Si el objeto afecta a habilidades o crafting, lee:

```text
vaults/system/rules/core/checks-de-habilidades-en-rol.md
vaults/system/rules/character/habilidades.md
```

No leas `vaults/system/rules.md` salvo que falte un módulo o haya una contradicción.

## Carpeta de salida

Los objetos existentes viven en:

```text
vaults/published/4. Otros/items/
```

Por defecto guarda ahí, porque es el estilo actual del repo.

Si el usuario quiere que el objeto sea privado o de sistema, pregunta antes de guardarlo en otra ruta.

## Patrón principal: receta + objeto + crítico

Normalmente una receta produce:

1. **Una receta / plano** con tabla de resultados por tier.
2. **Un objeto base con 3 niveles**.
3. **Un objeto especial de crítico**.

Ejemplo conceptual:

```text
Planos de Cinturón de Pociones.md  → receta
Cinturón de Pociones.md            → objeto niveles 1/2/3
Cinturón de Reservas.md            → objeto especial de crítico
```

## Proceso de entrevista

Si el usuario ya dio suficiente información, genera la propuesta directamente.

Si falta información, pregunta **de una en una**:

1. **¿Qué gremio o habilidad lo crea?** Ej: sastrería, alquimia, mecánica, cocina, lutería, herrería.
2. **¿Qué objeto base produce la receta?** Debe tener 3 niveles.
3. **¿Qué mejora cada nivel?** Ej: 1/2/3 usos, ranuras, cargas, dados, alcance, duración.
4. **¿Qué objeto especial sale con crítico?** Debe ser una versión excepcional, no solo “nivel 4”.
5. **¿Qué coste, materiales y tiempo de preparación quieres?** Si no lo sabe, propón valores y márcalos como ajustables.

No hagas todas las preguntas a la vez.

## Tipos de item comunes

Frontmatter `tipo` habitual:

```text
receta
equipo
consumible
material
herramienta
```

`uso` habitual cuando aplica:

```text
armadura
arma
herramienta
consumible
accesorio
```

`gremio` puede ser string o lista. Sigue el estilo existente:

```yaml
gremio: sastrería
```

o:

```yaml
gremio:
  - sastrería
```

## Balance para objetos que afectan acciones

Cuidado especial con efectos que reducen coste de acciones.

En Sonos cada Cantor tiene **3 Puntos de Acción (PA)** por turno. Cualquier objeto que permita hacer algo “sin coste de acción” debe tener límites claros:

- equipado antes del combate;
- número de ranuras / usos;
- una vez por ronda;
- consume carga;
- no permite encadenar acciones infinitas;
- no duplica recursos sin coste.

Si el objeto genera **Resonancia**, **Silencio**, curación o acciones gratis, haz revisión de balance explícita.

## Formato de propuesta inicial

Antes de guardar, presenta los tres archivos conceptualmente:

```markdown
# Propuesta de objeto: [Nombre]

**Gremio:** [gremio]  
**Tipo:** receta + objeto de 3 niveles + crítico  
**Fantasía:** [qué hace y cómo se ve]

---

## 1. Receta — [Nombre de receta/plano]

**Descripción:** ...
**Materiales:** ...
**Tiempo de preparación:** ...

| Tier | Resultado |
|---|---|
| Pifia | ... |
| 1 | [[Objeto Base]] 1 |
| 2 | [[Objeto Base]] 2 |
| 3 | [[Objeto Base]] 3 |
| Crítico | [[Objeto Especial]] |

## 2. Objeto base — [Nombre]

**Tipo:** equipo / consumible / etc.  
**Uso:** ...

| Nivel | Efecto |
|---|---|
| 1 | ... |
| 2 | ... |
| 3 | ... |

## 3. Objeto crítico — [Nombre]

[Descripción y efecto especial]

## Revisión de balance

[Análisis breve]
```

## Revisión de balance obligatoria

Antes de presentar, revisa:

- ¿El nivel 1 ya es útil?
- ¿Los niveles 2 y 3 escalan de forma simple y clara?
- ¿El crítico es especial sin invalidar el objeto base?
- ¿El objeto rompe la economía de acciones, Resonancia, curación o Silencio?
- ¿El objeto requiere estar equipado/preparado si da acciones gratis?
- ¿Los materiales y tiempo reflejan la potencia?

Usa severidad:

```text
🔴 roto
🟡 fuerte pero manejable
🟢 aceptable
```

Si hay un problema 🔴, ajusta el diseño antes de presentarlo.

## Guardar archivos

Después de presentar la propuesta, pregunta:

1. ¿Quieres ajustar nombres, niveles, materiales o crítico?
2. ¿El balance te convence?
3. ¿Quieres guardar los archivos Markdown en `vaults/published/4. Otros/items/`?

No guardes archivos hasta que el usuario confirme.

Cuando confirme, crea 3 archivos.

### Archivo 1 — Receta / Planos

Nombre recomendado:

```text
Planos de [Objeto Base].md
```

Para alquimia/cocina puede usarse directamente el nombre de la receta si el estilo encaja.

Formato:

```markdown
---
dg-publish: true
gremio: [gremio]
precio: [precio]
tipo: receta
tags: item
---

# Descripción
[Descripción breve de la receta/plano.] ^[anchor]

# Materiales
- [material]
- [material]

# Preparación
Tiempo de preparación: [tiempo]

| Tier    | Resultado                               |
| ------- | --------------------------------------- |
| Pifia   | [fallo]                                 |
| 1       | [[Objeto Base]] 1                       |
| 2       | [[Objeto Base]] 2                       |
| 3       | [[Objeto Base]] 3                       |
| Crítico | [[Objeto Especial]]                     |
```

Usa un anchor corto y estable, por ejemplo:

```text
^cinturon-pociones
```

### Archivo 2 — Objeto base de 3 niveles

Formato:

```markdown
---
dg-publish: true
tipo: equipo
uso: [uso]
precio: [precio nivel 1, nivel 2, nivel 3]
tags: item
gremio:
  - [gremio]
---

# Descripción
![[Planos de Objeto Base#^anchor]]

# Efecto
[Regla general]

| Nivel | Efecto |
| ----  | ------ |
| 1     | ...    |
| 2     | ...    |
| 3     | ...    |
```

### Archivo 3 — Objeto especial de crítico

Formato:

```markdown
---
dg-publish: true
tipo: equipo
uso: [uso]
precio: ???
tags: item
gremio:
  - [gremio]
---

# Descripción
[Descripción del objeto excepcional.]

# Efecto
[Debe incluir o superar el efecto del objeto base nivel 3 de forma especial y clara.]
```

## Nombres y enlaces

- Usa nombres en español con mayúsculas normales para archivos publicados, como los existentes:

```text
Cinturón de Pociones.md
Planos de Cinturón de Pociones.md
```

- Usa wikilinks Obsidian:

```text
[[Cinturón de Pociones]]
```

- Si un archivo ya existe, no lo sobrescribas sin pedir confirmación.

## Si viene desde una idea pendiente

Si el input viene de `vaults/campaign/ideas/` o `vaults/system/ideas/`:

1. Usa el texto de la idea como briefing.
2. Diseña los tres archivos.
3. Cuando el usuario esté satisfecho y los archivos estén guardados, cambia `status: pending` a `status: done` en la idea original.

## Qué no hacer

- No guardar archivos sin confirmación explícita.
- No sobrescribir objetos existentes sin confirmación.
- No crear efectos de acciones gratis sin límite claro.
- No inventar reglas nuevas como si fueran canónicas.
- No cambiar el estilo del vault de items sin motivo.
