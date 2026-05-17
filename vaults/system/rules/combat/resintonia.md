---
title: "Resintonía"
rules_status: canonical
source_section: "3.2.1 Resintonía"
version_introduced: "Alpha 0.1.0"
last_reviewed: "2026-05-17"
---

# Resintonía

Cuando un Cantor llega a 0 puntos de Vitalidad, abandona su forma cantora y vuelve a su raza base, quedando inconsciente en la casilla donde cayó.

La Resintonía es el sistema arcade de Sonos para gestionar la caída de los Cantores durante el combate. La party dispone de una bolsa común de Resintonizaciones, determinada por el modo de juego.

## Modo Arcade y Modo Hardcore

Por defecto, Sonos asume el enfoque **Arcade**, donde la caída, recuperación y posible derrota del grupo se gestionan mediante las reglas de Resintonía.

Como modo alternativo y clásico, el grupo puede jugar en **Modo Hardcore**. En Modo Hardcore, cuando un personaje muere, el combate no se reinicia: la muerte del personaje es definitiva y el jugador debe crear otro personaje.

## Bolsa de Resintonizaciones

Las Resintonizaciones pertenecen al grupo, no a personajes individuales. Si la bolsa común tiene varias Resintonizaciones disponibles, un mismo Cantor puede ser resintonizado varias veces usando esa misma reserva compartida.

La cantidad inicial depende del modo de juego:

| Modo | Resintonizaciones disponibles |
|------|--------------------------------|
| **Fácil** | Igual a la cantidad de jugadores |
| **Normal** | Igual a la mitad de la cantidad de jugadores; el DM y el grupo deciden si redondean hacia arriba o hacia abajo |
| **Difícil** | Igual que Normal, y además los Cantores inconscientes en raza base pueden morir si reciben golpes |
| **Extra difícil** | Igual que Difícil, pero los golpes recibidos en raza base no se limpian al ser Resintonizado |

## Cantor caído en raza base

Un Cantor caído en raza base queda inconsciente y no puede moverse ni actuar.

En modo Fácil y Normal, el Cantor caído permanece inconsciente mientras no sea resintonizado.

En modo Difícil y Extra difícil, un Cantor inconsciente en raza base puede recibir golpes. Si recibe 3 golpes de fuentes distintas, muere y el combate se pierde.

Un golpe cuenta aunque el daño final sea 0. Una misma fuente solo puede aportar 1 golpe al contador, aunque genere varios impactos. Por ejemplo, si un único hechizo dispara 3 misiles contra el Cantor caído, cuenta como 1 golpe.

En modo Difícil, el contador de golpes recibidos en raza base se limpia cuando el Cantor es resintonizado.

En modo Extra difícil, el contador de golpes recibidos en raza base no se limpia al ser resintonizado. Si el Cantor vuelve a caer más adelante, conserva los golpes acumulados previamente.

## Acción: Resintonizar

Un Cantor puede Resintonizar a un aliado caído si está en una casilla adyacente a él.

Para hacerlo, el Cantor que Resintoniza debe:

- gastar 1 PA;
- gastar toda su Resonancia restante, incluso si su Resonancia restante es 0;
- consumir 1 Resintonización de la bolsa común.

El Cantor resintonizado:

- recupera la consciencia;
- recupera su forma cantora;
- vuelve con la mitad de su Vitalidad máxima;
- conserva la Resonancia que tenía antes de llegar a 0 Vitalidad.

## Derrota por falta de Resintonizaciones

Si la bolsa común no tiene Resintonizaciones disponibles, el siguiente Cantor que caiga a 0 Vitalidad muere y el combate se pierde.

## Reinicio Arcade e inversión de Auralita Refinada

En Modo Arcade, cuando el grupo pierde un combate y debe reiniciarlo, el DM puede permitir que los jugadores inviertan Auralita Refinada acumulada antes de volver a intentar ese mismo combate.

Esta norma es la recomendación por defecto para mantener el ritmo arcade: una derrota puede dar lugar a una estrategia distinta en el siguiente intento gracias a una mejora comprada entre intentos. Aun así, sigue siendo opcional y queda a discreción del DM.

La Auralita Refinada que se puede gastar debe ser Auralita Refinada acumulada por vías normales. Perder un combate nunca otorga Auralita Refinada por sí mismo, y una recompensa asociada a ganar ese combate solo se obtiene cuando el combate se gana.

La inversión entre intentos sigue las reglas normales de mejoras disponibles para los Cantores. Esta ventana no implica por sí misma un reset de build ni permite recuperar Auralita Refinada ya invertida.

La narrativa de este reinicio queda a elección del DM. Puede representarse dentro del mundo, tratarse como una mecánica puramente arcade o no recibir explicación narrativa si la mesa lo prefiere.

## El Observador

En Modo Arcade, cada vez que el grupo pierde un combate y debe reiniciarlo, el Observador puede manifestarse antes de devolverlos al inicio del combate. Normalmente lo hace con un comentario, burla, queja o advertencia sobre la derrota.

El Observador es una presencia opcional de tono arcade. El DM puede desarrollarlo como una entidad real de la campaña, usarlo solo como recurso humorístico o ignorar su narrativa y aplicar únicamente la mecánica.

Cada vez que el grupo pierde un combate que debe reiniciarse, aumenta en 1 el contador de derrotas del Observador. Cuando el contador llega a 3, se reinicia a 0 y el siguiente intento de combate queda afectado por un **Capricho del Observador** durante todo ese intento.

Las derrotas no tienen que ser consecutivas: el contador mide combates perdidos con reinicio en Modo Arcade.

### Tabla de Caprichos del Observador

Cuando se active un Capricho del Observador, el DM tira 1d6 o elige un resultado apropiado para la mesa.

| d6 | Capricho | Efecto |
|---:|---|---|
| 1 | **Pulso caprichoso** | Cada vez que un ser use un Pulso o un ataque con objetivo, el objetivo se determina aleatoriamente entre todos los objetivos válidos dentro de alcance. |
| 2 | **Dirección equivocada** | Cada vez que un ser se mueve voluntariamente, el DM determina aleatoriamente la dirección real del movimiento. La distancia sigue siendo la elegida por quien se mueve. |
| 3 | **Resonancia inestable** | Cuando un Cantor vaya a ganar Resonancia al inicio de su turno, tira 2d6. El primer dado suma y el segundo dado resta. La Resonancia ganada es el resultado final, con mínimo 0. |
| 4 | **Estados cruzados** | Al inicio de cada ronda, cada jugador tira en la tabla de estados positivos y en la tabla de estados negativos, recibiendo un estado de cada tipo. Al inicio de la siguiente ronda, esos estados se limpian y se vuelve a tirar. |
| 5 | **Reset mal colocado** | Al inicio de cada ronda, los personajes aparecen en posiciones aleatorias distintas dentro de la escena de combate, decididas por el DM. |
| 6 | **Caos compuesto** | El DM tira dos veces en esta tabla y aplica ambos efectos. Si vuelve a salir 6, repite esa tirada hasta obtener otro resultado. |
