---
title: "Resintonía"
rules_status: canonical
source_section: "3.2.1 Resintonía"
version_introduced: "Alpha 0.1.0"
last_reviewed: "2026-05-15"
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
