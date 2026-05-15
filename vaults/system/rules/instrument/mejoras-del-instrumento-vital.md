---
title: "Mejoras del Instrumento Vital"
rules_status: canonical
source_section: "2.4.4 Mejoras del Instrumento Vital"
version_introduced: "Alpha 0.1.0"
last_reviewed: "2026-05-15"
---

# Mejoras del Instrumento Vital
A lo largo de la campaña, los jugadores obtendrán recursos para mejorar su Instrumento Vital, en concreto Auralita Refinada.

## Ritmo de entrega de Auralita Refinada
La Auralita Refinada es el principal recurso de progresión de un Cantor. Sonos no usa niveles: cada Cantor invierte su Auralita Refinada en mejorar su Instrumento Vital y decide qué áreas quiere desarrollar.

La recomendación estándar es entregar **5 Auralita Refinada por Cantor al final de cada sesión**.

La Auralita Refinada es un recurso tangible: aunque se entregue por Cantor, los jugadores pueden compartirla entre ellos.

El DM puede ajustar la progresión de la campaña cambiando la cantidad entregada por sesión. Si sabe cuántas sesiones quiere que dure la campaña o un tramo concreto de progreso, puede usar esta fórmula:

```text
Auralita por Cantor por sesión = Coste objetivo de progreso / Número de sesiones deseadas
```

Por ejemplo, si el progreso objetivo cuesta 100 Auralita Refinada y el DM quiere alcanzarlo en 20 sesiones:

```text
100 / 20 = 5 Auralita Refinada por Cantor por sesión
```

Si el DM quiere dar Auralita Refinada extra, puede hacerlo al final de la sesión con premios de mesa como el jugador más gracioso, el momento más épico o la mejor tirada.

## Costes de referencia de progreso
Estos costes sirven como objetivos para que el DM use la fórmula anterior y calcule cuánta Auralita Refinada entregar por sesión.

Los costes asumen un Instrumento Vital inicial con **un atributo en C**, no incluyen compra de cartas, no incluyen Purificación de Desafinación, no incluyen mejoras de Dado de Instrumento, Silencio ni Vitalidad, y toman como referencia el coste base de las mejoras antes de posibles recuperaciones de Auralita o fallos.

| Objetivo de progreso | Cálculo | Coste objetivo | A 5 Auralita por sesión |
|---|---|---:|---:|
| **Desarrollo natural completo** | 68 en mejoras base y Resonancia + 26 para subir el atributo inicial de C a S + 10 de Despertar Armónico + 30 para subir el nuevo atributo de D a S | **134 Auralita** | **~27 sesiones** |
| **Instrumento extremo mediante corrupción** | 134 del desarrollo natural + 4 × (20 por repetir Despertar Armónico como Mejora Corrupta + 30 para subir ese atributo de D a S) | **334+ Auralita** | **~67+ sesiones** |

El desarrollo natural completo representa una referencia para las mejoras base no repetibles del Instrumento Vital. El Instrumento extremo mediante corrupción representa una referencia para llevar los 6 atributos del Instrumento Vital hasta S usando Mejoras Corruptas.

El símbolo **+** indica que el coste real puede aumentar por fallos, Desafinación, Purificación de Desafinación, mejoras repetibles de Vitalidad u otros costes derivados de forzar mejoras prohibidas. No existe un máximo absoluto cerrado para las inversiones repetibles.

## Luthiering para mejoras
Para mejorar el Instrumento Vital será necesario disponer de la Auralita Refinada necesaria además de un aliado PC/NPC que cuente con la habilidad "Luthiering".

Para relizar una mejora a un Instrumento vital se requerirá de una tirada de Habilidad de Luthiering. Los posibles outcomes serán:

| Categoría | Resultado |
|-----------|------------------------------------------------------|
| Tier 1    | La mejora ocurre pero ganas 1d4 de desafinación      |
| Tier 2    | La mejora ocurre                                     |
| Tier 3    | La mejora ocurre y recuperas la mitad de la Auralita |


## Mejoras
Cada mejora solo puede comprarse **una vez**, salvo que se indique lo contrario.

| Mejora                                                | Coste           |
| ----------------------------------------------------- | --------------- |
| **+1 Espacio de Rudimento**                           | **3 Auralita**  |
| **+1 Espacio de Rudimento adicional**                 | **5 Auralita**  |
| **+1 Espacio de Fundamento**                          | **4 Auralita**  |
| **+1 Espacio de Fundamento adicional**                | **6 Auralita**  |
| **Evolución de Espacio de Rudimento**                 | **5 Auralita**  |
| **Evolución de Espacio de Fundamento**                | **5 Auralita**  |
| **Despertar Armónico (Escalado  D en otro atributo)** | **10 Auralita** |
| **Purificación de Desafinación**                      | **2 Auralita**  |
| **+1 Resonancia (Hasta 4 veces)**                     | **10 Auralita** |
| **+2 Vitalidad máxima**                               | **5 Auralita**  |
| **+1 Hueco de Gema (hasta 3 veces)**                  | **7 Auralita**  |

La mejora de **+2 Vitalidad máxima** puede comprarse cualquier número de veces.

## Huecos de Gema
Un Instrumento Vital puede mejorarse para obtener hasta **3 Huecos de Gema**. Cada Hueco de Gema cuesta **7 Auralita Refinada** y requiere la tirada normal de **Luthiering** para mejoras del Instrumento Vital.

Las gemas son objetos físicos crafteables. Para crear una gema se necesita un **joyero**, la **receta** correspondiente y los **materiales** necesarios.

Insertar, retirar o cambiar una gema en un Hueco de Gema no requiere tirada, coste ni procedimiento especial, pero no puede hacerse durante el combate.

Un Instrumento Vital puede tener hasta **3 gemas equipadas** y no puede tener **gemas repetidas** al mismo tiempo.

Cada gema tiene su propio efecto, normalmente **pasivo**, indicado en la descripción de la gema.

## Escalado de Dado de Instrumento y Silencio
El Dado de Instrumento y el Silencio pueden mejorarse de manera individual y permanente mediante Auralita Refinada.

Ambas progresiones se compran por separado. Mejorar el Dado de Instrumento no mejora el Silencio, y mejorar el Silencio no mejora el Dado de Instrumento.

| Ruta  | Coste |
|:-----:|:-----:|
| D → C | 8     |
| C → B | 12    |
| B → A | 18    |
| A → S | 26    |

| Rango | Dado |
|:-----:|:----:|
| D     | 1d6  |
| C     | 1d8  |
| B     | 1d10 |
| A     | 1d12 |
| S     | 2d8  |

Un Cantor comienza normalmente con **rango C** en Dado de Instrumento y **rango C** en Silencio.

## Escalado  de Atributos de Instrumento Vital
Los Cantores también pueden usar la Auralita Refinada con el fin de mejorar los atributos de los Instrumentos Vitales para hacer de sus Rudimentos y Fundamentos habilidades más efectivas.

| Ruta  | Coste |
|:-----:|:-----:|
| D → C | 4     |
| C → B | 6     |
| B → A | 8     |
| A → S | 12    |

## Mejoras corruptas
Los Cantores pueden decidir que las mejoras convencionales no son suficiente y necesitan más poder. En ese caso pueden intentar forzar una mejora prohíbida. 

Como bien se indica en la sección mejoras, cada mejora puede comprarse solo una vez, sin embargo, con el doble de de coste de Auralita se puede forzar a repetir una mejora ya obtenida.

Este proceso es conocido como Corrupción del Instrumento Vital no todos los Luthiers están dispuestos a este trabajo dadas las consecuencias de fallar y su complejidad.

| Categoría | Resultado |
|-----------|----------------------------------------------------------------------|
| Tier 1    | La mejora no ocurre, tu instrumento se corrompe, durante 1d4 de turnos una mejora aleatoria se desactiva|
| Tier 2    | La mejora no ocurre                                                  |
| Tier 3    | La mejora ocurre y ganas 1d8 de Desafinación                         |
