# Sonos — Guía del repositorio

## Estructura general

```
sonos/
├── card-generator/        # Generador de cartas imprimibles
├── character-sheet/       # Hojas de personaje (A4 y A5)
├── documentation/         # Documentación del sistema
├── icon/                  # Iconos del juego
├── recursos/              # Recursos gráficos y assets
├── rules/                 # Reglas del sistema
└── vaults/                # Vaults de Obsidian
    ├── published/         # Vault pública (jugadores)
    ├── campaign/          # Vault de campaña (DM)
    └── system/            # Vault de sistema (diseño)
```

---

## Carpetas

### `card-generator/`
Genera las hojas de cartas imprimibles en HTML+CSS.

- `cards-full.html` — vista de cartas a tamaño completo
- `cards.html` — vista alternativa
- `data.json` — datos de las cartas en JSON. **Archivo generado, no editar a mano.**
- `build-data.js` — script conversor: lee los Markdown de `vaults/system/cards/` y regenera `data.json`
- `artwork/` — ilustraciones de las cartas

**Para regenerar `data.json` tras editar cartas:**
```bash
node card-generator/build-data.js
```

---

### `vaults/system/cards/` — FUENTE DE LA VERDAD de las cartas

Cada carta es un archivo Markdown independiente. Edita aquí, luego regenera el JSON.

```
vaults/system/cards/
├── fundamentos/   # Skills pasivas (una por archivo)
└── rudimentos/    # Skills activas (una por archivo)
```

**Formato de cada archivo:**
```markdown
---
type: fundamento        # o rudimento
element: armonia        # elemento principal
coste: "0"              # coste de Resonancia (string)
# bucket: ritmo         # solo si el bucket JSON difiere de element[0]
# element: [sincopa, ritmo]  # array si tiene varios elementos
---

# Nombre de la Carta

## Base
Descripción de la habilidad base. Usa **negrita** para términos de juego e *cursiva* para tipos de daño.

## Evolucionado
Descripción de la versión evolucionada.
```

**Convenciones de formato:**
- `**texto**` → `<b>texto</b>` en el JSON (términos de juego: **Resonancia**, **Silencio**, **Pulso**...)
- `*texto*` → `<i>texto</i>` (tipos: *daño verdadero*, *ventaja*, *desventaja*...)
- `***texto***` → `<b><i>texto</i></b>` (etiquetas de tipo de acción: ***Reacción.***, ***Activable.***)

---

### `vaults/system/cheatsheets/`
Resúmenes de referencia rápida del sistema para uso en mesa.

### `vaults/system/prompts/`
Prompts de IA para generar contenido (cartas, enemigos, escenas...).

---

### `vaults/published/`
Vault pública accesible para los jugadores. Contiene reglas, recaps de sesiones, lore e información de personajes.

```
published/
├── 1. Empieza Aquí/   # Introducción al juego
├── 2. Jugadores/      # Fichas y info de personajes
├── 3. Recaps/         # Resúmenes de sesiones
└── 4. Otros/          # Lore, items, reglas adicionales
```

### `vaults/campaign/`
Vault privada del DM. Notas de campaña, sesiones planificadas, secretos.

---

### `rules/`
Reglas del sistema en formato documento. Fuente de la verdad para las mecánicas del juego.

### `character-sheet/`
Hojas de personaje en HTML+CSS, disponibles en formato A4 y A5.

### `documentation/`
Documentación técnica y de diseño del sistema.
