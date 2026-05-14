---
type: rules_task_tracker
status: active
updated: "2026-05-14"
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

- [ ] **RT-003 · Media:** Decidir cómo se debería otorgar la Auralita Refinada a un grupo de jugadores.  
  Módulos: [[instrument/mejoras-del-instrumento-vital.md]], [[instrument/desafinacion.md]]  
  Notas: definir ritmo de entrega, si es recompensa grupal o individual, y cómo escala con el tamaño del grupo.  
  Origen: conversación 2026-05-14.

- [x] **RT-004 · Media:** Decidir cómo los jugadores pueden acceder a las habilidades en forma de cartas de Fundamentos y Rudimentos.  
  Módulos: [[instrument/fundamentos.md]], [[instrument/rudimentos.md]], [[instrument/mejoras-del-instrumento-vital.md]], [[instrument/obtencion-de-cartas.md]]  
  Notas: definir si se obtienen por progreso, entrenamiento, hallazgos, compra, recompensas narrativas, requisitos del Instrumento Vital o combinación de varios métodos.  
  Origen: conversación 2026-05-14.  
  Resuelta: 2026-05-14. Patch: [[../../rules-patches/2026-05-14-alpha-0.2.0-obtencion-de-cartas.md]].

- [ ] **RT-007 · Media:** Brainstormear e incluir en las reglas una forma de mejorar el Dado de Instrumento y los rangos/distancias de Pulsos de un Instrumento Vital.  
  Módulos: [[instrument/dano-de-un-instrumento-vital.md]], [[instrument/pulsos.md]], [[instrument/mejoras-del-instrumento-vital.md]], [[instrument/instrumento-vital.md]]  
  Notas: explorar si la mejora ocurre mediante prestigios, add-ons/modificaciones del Instrumento Vital, cambio a un Instrumento Vital superior u otro sistema equivalente.  
  Origen: conversación 2026-05-14.

- [ ] **RT-008 · Media:** Diseñar cómo funciona la ventaja y la doble ventaja en combate cuando no hay tiers de resultado.  
  Módulos: [[core/checks-de-habilidades-en-rol.md]], [[combat/acciones-por-turno.md]], [[combat/estados-positivos.md]], [[combat/estados-negativos.md]], [[character/silencio.md]], [[instrument/dano-de-un-instrumento-vital.md]]  
  Notas: fuera de combate mantener el enfoque tipo Draw Steel de subir/bajar tier; en combate revisar propuesta: si el daño requiere tirar dado, ventaja convierte el dado en mitad de daño asegurado y doble ventaja en daño máximo; si la carta ya hace daño fijo/máximo, ventaja hace que la mitad del daño atraviese el Silencio y doble ventaja lo trata como daño verdadero. Evaluar balance, edge cases y redacción final.  
  Origen: conversación 2026-05-14.

- [ ] **RT-010 · Media:** Incluir en las reglas una guía para que los Dungeon Masters creen sus propios Fundamentos y Rudimentos.  
  Módulos: [[instrument/fundamentos.md]], [[instrument/rudimentos.md]], [[instrument/evoluciones.md]]  
  Notas: diseñar un sistema paso a paso para crear cartas propias, con estructura recomendada, criterios de coste y balance, tips, ejemplos y lista de don'ts/errores comunes al diseñar habilidades.  
  Origen: conversación 2026-05-14.

- [ ] **RT-011 · Media:** Diseñar el sistema de Partituras como magia utilizable fuera de combate.  
  Módulos: [[instrument/fundamentos.md]], [[instrument/rudimentos.md]], [[instrument/dano-de-un-instrumento-vital.md]], [[character/atributos-de-un-cantor.md]], [[core/checks-de-habilidades-en-rol.md]]  
  Notas: definir hechizos no centrados en combate que puedan usar DI o AT para determinar potencia, alcance, duración o calidad del efecto; establecer tipos de Partituras, costes, límites de uso, relación con Fundamentos/Rudimentos y ejemplos de efectos útiles en exploración, social e investigación.  
  Origen: conversación 2026-05-14.

## Clarificaciones pendientes

- [ ] **RT-006 · Media:** Clarificar el sistema de rangos/distancias de los Pulsos de cada Instrumento Vital.  
  Módulos: [[instrument/pulsos.md]], [[instrument/dano-de-un-instrumento-vital.md]], [[combat/acciones-por-turno.md]], [[combat/movimiento.md]]  
  Notas: actualmente cada Instrumento Vital tiene 3 rangos, pero no se explica cómo se elige o cambia entre ellos, si requiere acción/coste, ni qué restricciones tiene durante el combate.  
  Origen: conversación 2026-05-14.

- [ ] **RT-009 · Media:** Revisar si existe y, si falta, crear una guía clara para elegir qué atributo sumar en acciones de rol.  
  Módulos: [[character/atributos-de-un-cantor.md]], [[character/habilidades.md]], [[character/habilidades-de-un-cantor.md]], [[core/checks-de-habilidades-en-rol.md]]  
  Notas: aclarar cómo distinguir entre Armonía, Melodía y otros atributos al combinarlos con una skill en acciones roleras; incluir criterios prácticos, ejemplos y posibles combinaciones atributo + habilidad para reducir dudas en mesa.  
  Origen: conversación 2026-05-14.

## Balance pendiente

- [ ] **RT-005 · Media:** Modificar el sistema de obtención de Resonancia durante el combate.  
  Módulos: [[character/resonancia.md]], [[combat/combate.md]], [[combat/acciones-por-turno.md]], [[combat/resintonia.md]]  
  Notas: revisar cuándo se genera Resonancia, cuánto se obtiene, límites por turno/combate y cómo afecta al ritmo de uso de Rudimentos.  
  Origen: conversación 2026-05-14.

## Publicación / documentación

_Empty._

## Completadas

_Empty._
