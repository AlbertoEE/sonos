---
type: rules_task_tracker
status: active
updated: "2026-05-15"
source_of_truth: "vaults/system/rules/"
managed_by: "sonos-rules-task-tracker"
printable: false
---

# Tareas pendientes de reglas

Backlog vivo para registrar dudas, huecos y cambios pendientes del sistema de reglas de Sonos.

Este archivo **no forma parte del documento imprimible** y no debe añadirse a `vaults/system/rules/_meta/manifest.yml`. Las reglas canónicas siguen estando en `vaults/system/rules/`; cuando una tarea se resuelva, debe hacerse mediante un patch en `vaults/system/rules-patches/` y recompilar `vaults/system/rules.md`.

## Cómo usarlo

- Añade tareas como checkboxes (`- [ ]`).
- Si una tarea apunta a una regla concreta, enlaza el módulo afectado.
- Si se resuelve con un patch, marca la tarea como completada y añade el enlace al patch.
- Mantén aquí los follow-ups persistentes; los `Follow-ups` de patches pueden copiarse aquí si siguen abiertos.

Formato recomendado:

```markdown
- [ ] **RT-### · Prioridad:** tarea breve.  
  Módulos: [[ruta/al/modulo.md]]  
  Notas: contexto mínimo o decisión pendiente.  
  Origen: conversación YYYY-MM-DD.
```

Los IDs `RT-###` son estables: no se reutilizan al completar tareas.

## Inbox

- [ ] **RT-001 · Media:** Añadir aquí nuevas dudas o cambios pendientes de reglas cuando aparezcan.  
  Módulos: pendiente  
  Origen: inicialización del tracker 2026-05-14.

## Flujo y mantenimiento

- [ ] **RT-002 · Alta:** Usar `sonos-rules-maintainer` para futuros cambios en reglas en vez de editar el documento imprimible directamente.  
  Módulos: [[index.md]], [[_meta/manifest.yml]]  
  Origen: [[../../rules-patches/2026-05-10-alpha-0.1.0-canonical-modular-rules.md]]

## Diseño pendiente

- [x] **RT-003 · Media:** Decidir cómo se debería otorgar la Auralita Refinada a un grupo de jugadores.  
  Módulos: [[instrument/mejoras-del-instrumento-vital.md]], [[instrument/desafinacion.md]]  
  Notas: definir ritmo de entrega, si es recompensa grupal o individual, y cómo escala con el tamaño del grupo.  
  Origen: conversación 2026-05-14.  
  Resuelta: 2026-05-14. Patch: [[../../rules-patches/2026-05-14-alpha-0.2.1-ritmo-auralita-refinada.md]].

- [x] **RT-004 · Media:** Decidir cómo los jugadores pueden acceder a las habilidades en forma de cartas de Fundamentos y Rudimentos.  
  Módulos: [[instrument/fundamentos.md]], [[instrument/rudimentos.md]], [[instrument/mejoras-del-instrumento-vital.md]], [[instrument/obtencion-de-cartas.md]]  
  Notas: definir si se obtienen por progreso, entrenamiento, hallazgos, compra, recompensas narrativas, requisitos del Instrumento Vital o combinación de varios métodos.  
  Origen: conversación 2026-05-14.  
  Resuelta: 2026-05-14. Patch: [[../../rules-patches/2026-05-14-alpha-0.2.0-obtencion-de-cartas.md]].

- [x] **RT-007 · Media:** Brainstormear e incluir en las reglas una forma de mejorar el Dado de Instrumento y los rangos/distancias de Pulsos de un Instrumento Vital.  
  Módulos: [[instrument/dano-de-un-instrumento-vital.md]], [[character/silencio.md]], [[character/vitalidad.md]], [[instrument/mejoras-del-instrumento-vital.md]], [[instrument/instrumento-vital.md]]  
  Notas: resuelto como progresión individual y permanente de Dado de Instrumento, Silencio y Vitalidad mediante Auralita Refinada; los Pulsos no cambian.  
  Origen: conversación 2026-05-14.  
  Resuelta: 2026-05-15. Patch: [[../../rules-patches/2026-05-15-alpha-0.4.0-progresion-di-silencio-vitalidad.md]].

- [x] **RT-008 · Media:** Diseñar cómo funciona la ventaja y la doble ventaja en combate cuando no hay tiers de resultado.  
  Módulos: [[core/checks-de-habilidades-en-rol.md]], [[combat/acciones-por-turno.md]], [[combat/estados-positivos.md]], [[combat/estados-negativos.md]], [[character/silencio.md]], [[instrument/dano-de-un-instrumento-vital.md]]  
  Notas: fuera de combate la ventaja/desventaja simple modifica el power roll en ±2, y la doble ventaja/desventaja sustituye ese modificador por subir o bajar 1 tier; en combate se define una tabla para daño con dado y daño fijo derivado de dado.  
  Origen: conversación 2026-05-14.  
  Resuelta: 2026-05-15. Patch: [[../../rules-patches/2026-05-15-alpha-0.5.1-ventaja-desventaja.md]].

- [ ] **RT-010 · Media:** Incluir en las reglas una guía para que los Dungeon Masters creen sus propios Fundamentos y Rudimentos.  
  Módulos: [[instrument/fundamentos.md]], [[instrument/rudimentos.md]], [[instrument/evoluciones.md]]  
  Notas: diseñar un sistema paso a paso para crear cartas propias, con estructura recomendada, criterios de coste y balance, tips, ejemplos y lista de don'ts/errores comunes al diseñar habilidades.  
  Origen: conversación 2026-05-14.

- [ ] **RT-011 · Media:** Diseñar el sistema de Partituras como magia utilizable fuera de combate.  
  Módulos: [[instrument/fundamentos.md]], [[instrument/rudimentos.md]], [[instrument/dano-de-un-instrumento-vital.md]], [[character/atributos-de-un-cantor.md]], [[core/checks-de-habilidades-en-rol.md]]  
  Notas: definir hechizos no centrados en combate que puedan usar DI o AT para determinar potencia, alcance, duración o calidad del efecto; establecer tipos de Partituras, costes, límites de uso, relación con Fundamentos/Rudimentos y ejemplos de efectos útiles en exploración, social e investigación.  
  Origen: conversación 2026-05-14.

- [ ] **RT-012 · Media:** Revisar cómo funciona la muerte de un Cantor durante combate y diseñar el sistema de revivir.  
  Módulos: [[character/silencio.md]], [[character/recursos-de-un-cantor.md]], [[combat/combate.md]], [[combat/acciones-por-turno.md]], [[combat/estados.md]]  
  Notas: definir cuándo un Cantor queda fuera de combate o muere, qué ocurre durante sus turnos, qué ventanas tienen los aliados para intervenir, costes/requisitos para revivir y consecuencias mecánicas o narrativas tras volver.  
  Origen: conversación 2026-05-14.

- [ ] **RT-014 · Media:** Añadir a la tabla de mejoras con Auralita Refinada el concepto de huecos de gemas para el Instrumento Vital.  
  Módulos: [[instrument/mejoras-del-instrumento-vital.md]], [[instrument/instrumento-vital.md]]  
  Notas: definir cómo se desbloquean hasta 3 huecos de gemas y cómo las gemas otorgan pequeñas mejoras al Instrumento Vital.  
  Origen: conversación 2026-05-15.

- [ ] **RT-016 · Media:** Preparar dos modos de juego para la gestión de muerte y derrota: Hardcore y Arcade.  
  Módulos: [[character/silencio.md]], [[character/recursos-de-un-cantor.md]], [[combat/combate.md]], [[combat/acciones-por-turno.md]], [[combat/estados.md]]  
  Notas: modo Hardcore: si el personaje muere, muere definitivamente. Modo Arcade: si el grupo pierde una pelea, puede reiniciar el combate como en un videojuego. Diseñar variantes de dificultad Arcade: reinicio cuando muere cualquier jugador, modo fácil cuando mueren todos los jugadores, y modo con X muertes compartidas estilo Monster Hunter, consumibles por el mismo jugador o por distintos jugadores, tras las cuales se reinicia.  
  Origen: conversación 2026-05-15.

- [x] **RT-017 · Media:** Modificar las reglas para que la construcción de personajes sea totalmente flexible y la Resonancia máxima no dependa de atributos.  
  Módulos: [[character/resonancia.md]], [[character/atributos-de-un-cantor.md]], [[character/recursos-de-un-cantor.md]], [[instrument/mejoras-del-instrumento-vital.md]]  
  Notas: todos los personajes comienzan con 4 de Resonancia máxima; a partir de ahí, cada jugador invierte libremente donde quiera mediante la tabla de Auralita Refinada, sin que la Resonancia máxima esté ligada a un atributo.  
  Origen: conversación 2026-05-15.

- [ ] **RT-018 · Media:** Diseñar opciones para que los jugadores puedan reinvertir su Auralita Refinada mediante un reset de build.  
  Módulos: [[instrument/mejoras-del-instrumento-vital.md]], [[character/auralium.md]], [[character/recursos-de-un-cantor.md]], [[combat/combate.md]]  
  Notas: permitir recuperar toda la Auralita Refinada invertida y volver a asignarla. Al comenzar una campaña, DM y jugadores deberían acordar una opción: reset pagando X de Auralita Refinada, reset libre al final de sesión, sin reset, o reset permitido en modo Arcade al perder una batalla, entre otras posibles variantes.  
  Origen: conversación 2026-05-15.

- [ ] **RT-019 · Media:** Aclarar que en modo Arcade, al perder una batalla, los jugadores pueden invertir la Auralita Refinada acumulada antes de repetir el combate.  
  Módulos: [[instrument/mejoras-del-instrumento-vital.md]], [[character/auralium.md]], [[combat/combate.md]]  
  Notas: permitir mejorar el Instrumento Vital con Auralita Refinada acumulada tras una derrota en modo Arcade, sin tener que esperar al final de la sesión o al inicio de la siguiente.  
  Origen: conversación 2026-05-15.

## Clarificaciones pendientes

- [x] **RT-006 · Media:** Clarificar el sistema de rangos/distancias de los Pulsos de cada Instrumento Vital.  
  Módulos: [[instrument/pulsos.md]], [[instrument/dano-de-un-instrumento-vital.md]], [[combat/acciones-por-turno.md]], [[combat/movimiento.md]]  
  Notas: actualmente cada Instrumento Vital tiene 3 rangos, pero no se explica cómo se elige o cambia entre ellos, si requiere acción/coste, ni qué restricciones tiene durante el combate.  
  Origen: conversación 2026-05-14.  
  Resuelta: 2026-05-14. Patch: [[../../rules-patches/2026-05-14-alpha-0.2.3-modos-de-pulso.md]].

- [ ] **RT-009 · Media:** Revisar si existe y, si falta, crear una guía clara para elegir qué atributo sumar en acciones de rol.  
  Módulos: [[character/atributos-de-un-cantor.md]], [[character/habilidades.md]], [[character/habilidades-de-un-cantor.md]], [[core/checks-de-habilidades-en-rol.md]]  
  Notas: aclarar cómo distinguir entre Armonía, Melodía y otros atributos al combinarlos con una skill en acciones roleras; incluir criterios prácticos, ejemplos y posibles combinaciones atributo + habilidad para reducir dudas en mesa.  
  Origen: conversación 2026-05-14.

## Balance pendiente

- [x] **RT-005 · Media:** Modificar el sistema de obtención de Resonancia durante el combate.  
  Módulos: [[character/resonancia.md]], [[combat/combate.md]], [[combat/acciones-por-turno.md]], [[combat/resintonia.md]]  
  Notas: revisar cuándo se genera Resonancia, cuánto se obtiene, límites por turno/combate y cómo afecta al ritmo de uso de Rudimentos.  
  Origen: conversación 2026-05-14.  
  Resuelta: 2026-05-15. Patch: [[../../rules-patches/2026-05-15-alpha-0.2.5-resonancia-pulso-meditar.md]].

- [ ] **RT-013 · Media:** Revisar la mecánica de Tensión.  
  Módulos: [[combat/tension.md]], [[combat/subidas-de-tension.md]], [[combat/bajada-de-tension.md]], [[combat/efectos-de-la-tension.md]], [[combat/acciones-por-turno.md]]  
  Notas: evaluar si la subida, bajada, efectos por umbral y acciones relacionadas con Tensión funcionan bien en mesa y están balanceadas.  
  Origen: conversación 2026-05-15.

## Publicación / documentación

- [ ] **RT-015 · Media:** Aclarar en la documentación que en Sonos no hay niveles de personaje.  
  Módulos: [[character/perks.md]], [[character/progresion-de-habilidades.md]], [[instrument/mejoras-del-instrumento-vital.md]], [[character/vitalidad.md]], [[character/silencio.md]], [[character/resonancia.md]], [[instrument/dano-de-un-instrumento-vital.md]], [[instrument/obtencion-de-cartas.md]]  
  Notas: explicar que al final de cada sesión se invierte en construir el personaje mediante mejoras como Vida, Silencio, Resonancia, DI, capacidad de cartas u otros elementos de build.  
  Origen: conversación 2026-05-15.

## Completadas

_Empty._
