---
name: sonos-card-visual-designer
description: Diseña o revisa la narrativa visual de cartas y sets de habilidades de Sonos sin tocar su diseño mecánico. Use when adding visual flavor, sensory identity, telegraphing, animations, VFX, Obsidian Visual sections, or describing how a Sonos card/set looks at the table after mechanics are already defined.
---

# Sonos Card Visual Designer

Diseña la **narrativa visual y sensorial** de cartas o sets de habilidades de Sonos una vez que la mecánica ya está definida.

Este skill existe para separar el diseño mecánico del diseño visual: no debe cargar el contexto principal de creación de cartas con sabor secundario, pero sí puede enriquecer cartas terminadas.

## Objetivo

Dado un set o una lista de cartas:

1. Leer las cartas fuente si existen.
2. Identificar su fantasía mecánica sin cambiarla.
3. Proponer una identidad visual común.
4. Describir cómo se ve cada carta en mesa.
5. Opcionalmente guardar esa narrativa como sección `## Visual` en los `.md` de las cartas.

## Fuentes

Cartas canónicas:

```text
vaults/system/cards/
```

Cartas legacy solo como inspiración estilística si el usuario lo pide:

```text
vaults/system/cards-legacy/
```

No leas reglas completas salvo que una descripción visual pueda confundirse con una mecánica.

## Cuándo usar este skill

Úsalo cuando el usuario pida:

- “dar visual” a un set;
- “cómo se ve esta carta”;
- “narrativa visual”;
- “flavor visual”;
- “VFX”;
- “telegraph” de áreas, predicciones, ataques o estados;
- revisar cartas mecánicamente terminadas para añadir sabor no mecánico.

No lo uses para diseñar números, costes, daño, alcance o balance; para eso usa `sonos-skill-set-designer`.

## Reglas importantes

- **No cambies mecánicas.** No alteres coste, daño, alcance, estados, timing ni condiciones.
- **No añadas efectos implícitos.** Una descripción visual no debe sugerir ventaja mecánica no escrita.
- **No contradigas el alcance.** Si la carta afecta 1 casilla, el visual no debe parecer un área enorme de daño real.
- **Distingue telegraph de efecto.** Las señales visuales pueden ser amplias, pero el impacto mecánico debe coincidir con el área indicada.
- **Mantén las cartas jugables fuera del set.** La narrativa de cada carta debe funcionar individualmente.
- **El set puede tener un motivo común**, pero cada carta necesita una silueta visual propia.
- **No sobreescribas archivos sin confirmación explícita.**

## Flujo obligatorio

### Paso 1 — Identificar input

Si el usuario da:

- **nombre de set**: busca cartas con `set: {nombre}` en `vaults/system/cards/`.
- **rutas de cartas**: lee esas rutas.
- **texto pegado**: trabaja sobre ese texto.
- **idea general sin cartas**: pregunta si quiere primero diseñar mecánicas o solo una propuesta visual conceptual.

Comando útil para buscar sets:

```bash
rg -n "^set:" vaults/system/cards
```

### Paso 2 — Leer cartas

Para cada carta, extrae:

- nombre;
- tipo: Fundamento o Rudimento;
- elemento;
- coste si aplica;
- set;
- bonus_set si existe;
- `## Base` completa;
- `## Visual` si ya existe.

Si ya existe `## Visual`, pregunta si debe reemplazarse, ampliarse o mantenerse.

### Paso 3 — Diseñar identidad visual común

Define, de forma breve:

- **Motivo central:** imagen recurrente del set.
- **Lenguaje visual:** formas, materiales, color, luz, sombras, geometría, símbolos.
- **Lenguaje sonoro:** qué se oye cuando se activa.
- **Telegraph en tablero:** cómo ven los jugadores/enemigos zonas, predicciones o preparaciones.
- **Diferencia entre carga, acierto y fallo:** si aplica.

Evita lore de campaña salvo que el usuario lo pida.

### Paso 4 — Proponer visual por carta

Para cada carta, entrega:

```markdown
### [Nombre]
**Lectura visual:** [1 frase: silueta clara]
**En mesa:** [2-4 frases de descripción sensorial]
**Telegraph / resolución:** [solo si aplica]
```

La descripción debe ser concreta y accionable para narrar en partida.

### Paso 5 — Preguntar antes de guardar

Pregunta:

```text
¿Quieres que añada estas descripciones como `## Visual` en las cartas Markdown?
```

No edites hasta que el usuario confirme.

### Paso 6 — Guardar si confirma

Si el usuario confirma, añade o actualiza en cada carta:

```markdown
## Visual
[descripción final]
```

Ubicación recomendada:

- después de `## Base` y su contenido;
- si ya hay `## Visual`, reemplaza solo si el usuario lo autorizó.

Después de editar, no hace falta regenerar `card-generator/data.json` porque el generador solo usa `## Base`, salvo que también se hayan cambiado mecánicas.

## Estilo recomendado

- Español claro y evocador.
- 2-5 frases por carta.
- Visual fuerte, pero no barroco.
- Usa metáforas musicales, espaciales o materiales si ayudan.
- Para Síncopa: cortes, huecos, desplazamientos imposibles, compases truncados, geometría de asesinato, silencios súbitos.
- Para Disonancia: fracturas, inversión, ruido, duplicación, espejos rotos, distorsión.
- Para Armonía: halos, acordes, resonancias cálidas, escudos, tejidos sonoros.
- Para Ritmo: percusión, peso, repetición, impacto, cadencia física.
- Para Melodía: líneas fluidas, color, venenos, ondas, propagación.
- Para Tempo: relojería, retardos, congelación, ecos temporales, metrónomos.

## Formato de respuesta recomendado

```markdown
# Visual del set: [Nombre]

## Identidad visual común

**Motivo central:** ...
**Lenguaje visual:** ...
**Lenguaje sonoro:** ...
**Telegraph en tablero:** ...
**Acierto / fallo:** ...

---

## Visual por carta

### [Carta]
**Lectura visual:** ...
**En mesa:** ...
**Telegraph / resolución:** ...

[...]

¿Quieres que añada estas descripciones como `## Visual` en las cartas Markdown?
```

## Qué no hacer

- No rediseñar la mecánica.
- No cambiar costes, alcance, daño, estados ni condiciones.
- No añadir reglas nuevas.
- No convertir el visual en lore obligatorio de campaña.
- No guardar sin confirmación.
- No regenerar `card-generator/data.json` salvo que se hayan cambiado secciones mecánicas.
