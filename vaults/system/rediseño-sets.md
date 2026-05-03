# Rediseño de sets de habilidades

Documento de trabajo para el rediseño elemento a elemento. Cada elemento debe quedar como un set coherente de **2 fundamentos + 4 rudimentos**.

---

## Problemas globales (afectan a todas las cartas)

### Notación incorrecta: DA → DI
Todas las cartas usan `[DA]` y `[DA+AT]`. La notación correcta según las reglas es `[DI]` (Dado de Instrumento) y `[DI+AT]`. Corregir en cada carta al redesignarla.

### Fundamentos Activables sin documentar
Algunas cartas tienen `type: fundamento` pero coste no-cero y la etiqueta `***Activable.***`. No está claro si son una mecánica válida o un error de categorización. **Decidir antes de redesignar Disonancia y Síncopa.**

---

## Estado por elemento

---

### Armonía
**Situación actual:** 3 fundamentos + 7 rudimentos → sobran 1F y 3R

**Fundamentos existentes**
| Carta | Valoración | Qué hacer |
|---|---|---|
| Exceso de Armonía | ✅ Buena — esquirlas de curación reactivas | Conservar, revisar notación |
| Resonancia Compartida | ✅ Buena — gestión de Resonancia compartida | Conservar, revisar notación |
| Momentum Armónico | ⚠️ Interesante pero depende de que el Silencio bloquee, muy condicional | Revisar o reemplazar |

**Rudimentos existentes**
| Carta | Coste | Valoración | Qué hacer |
|---|---|---|---|
| Coro de Amparo | 2 | ✅ Escudo en área, claro y útil | Conservar, corregir DA→DI |
| A Viva Voz | 1 | ⚠️ Aura interesante pero "si te mueves, se cancela" penaliza mucho | Revisar condición |
| Purificación | 1 | ✅ Simple y necesario en un support | Conservar |
| Transfusión de Resonancia | 2 | ⚠️ Útil pero muy situacional — solo sirve si un aliado necesita Resonancia | Revisar |
| Último Acorde | 4 | ✅ Poderoso y temático — salvar a alguien de morir | Conservar |
| Acorde Reconfortante | 4 | ✅ Curación directa, clara | Conservar |
| Última oportunidad | 4 | ✅ Reacción de sacrificio, muy Armonía | Conservar |

**Propuesta de set:** Tres rudimentos de coste 4 es demasiado — el set no puede funcionar con poca Resonancia. Necesita al menos un rudimento de coste 0. Candidatos a eliminar o reducir coste: Transfusión de Resonancia, A Viva Voz.

**Mecánica central a definir:** ¿Escudos y protección? ¿Curación reactiva? ¿Resonancia compartida? Elegir uno y que los 6 lo refuercen.

---

### Ritmo
**Situación actual:** 3 fundamentos + 6 rudimentos → sobran 1F y 2R

**Fundamentos existentes**
| Carta | Valoración | Qué hacer |
|---|---|---|
| Tambores de Guerra | ✅ Doble Pulso — define el estilo agresivo de Ritmo | Conservar |
| Focus | ✅ Bonus a Rudimentos multiobjetivo en objetivo único — buen sinergista | Conservar |
| Inercia | ✅ Push pasivo al infligir daño — simple y siempre activo | Conservar |

Ritmo tiene los 3 fundamentos sólidos. Hay que elegir 2 para el set.

**Rudimentos existentes**
| Carta | Coste | Valoración | Qué hacer |
|---|---|---|---|
| Rotación | 0 | ✅ Daño repartido en área cuerpo a cuerpo, coste 0 | Conservar |
| Redoble | 0 | ⚠️ Encadenado aleatorio con riesgo de perder turno — se solapa con Cadena de Golpes | Revisar o elegir uno |
| BONK | 1 | ✅ Mecánica de cargas única, identidad propia | Conservar |
| Cadena de Golpes | 1 | ⚠️ Similar a Redoble en concepto (repetir ataques) | Revisar o elegir uno |
| Impulso Rítmico | 1 | ✅ Movimiento + daño, movilidad para un tanque | Conservar |
| Onda de Choque | 2 | ✅ Empuje en área — sinergia directa con Inercia | Conservar |

**Problema:** Redoble y Cadena de Golpes hacen lo mismo conceptualmente (atacar repetidamente pagando un coste). Elegir uno.

**Mecánica central sugerida:** Empujar y golpear — Inercia + Onda de Choque + Impulso Rítmico forman un núcleo coherente. Completar con daño sostenido.

---

### Síncopa
**Situación actual:** 3 fundamentos + 7 rudimentos → sobran 1F y 3R

**Fundamentos existentes**
| Carta | Valoración | Qué hacer |
|---|---|---|
| Dedo en la llaga | ⚠️ Fundamento con coste 3 — si es Activable, documentar; si no, pasar a rudimento | Aclarar tipo |
| Duelo final | ✅ Marcar objetivo, mecánica de duelista clara | Conservar, quizás reducir complejidad del texto |
| Riposte | ⚠️ Tiene coste 2 y requiere activación — debería ser rudimento | Reclasificar como rudimento |

**Rudimentos existentes**
| Carta | Coste | Valoración | Qué hacer |
|---|---|---|---|
| Corazón palpitante | 3 | ⚠️ Está en bucket ritmo con element sincopa — confuso | Reclasificar o reubicar |
| Puñalada Sincopada | 1 | ✅ Reacción que amplifica daño ajeno — muy Síncopa | Conservar |
| Rematar | 2 | ✅ Explotar daño ya recibido — identidad clara de asesino | Conservar |
| Danza Letal | 2 | ✅ Movilidad + daño de paso, temático | Conservar |
| Entrada Triunfal | 2 | ✅ Ejecución con movimiento — combo natural con Rematar | Conservar |
| Fuga | 1 | ⚠️ Daño + escape — funcional pero genérico, podría ser de cualquier rol | Revisar |
| Ejecución Oportunista | 2 | ✅ Explota estados negativos — sinergia con Dedo en la llaga | Conservar |

**Mecánica central sugerida:** Marcar → explotar. Duelo final marca, Rematar y Ejecución Oportunista explotan. Puñalada Sincopada y Danza Letal como herramientas de posicionamiento/reacción.

---

### Disonancia
**Situación actual:** 2 fundamentos + 6 rudimentos → fundamentos justos, 2R sobrantes

**Fundamentos existentes**
| Carta | Valoración | Qué hacer |
|---|---|---|
| Doble o Nada | ⚠️ Coste 3, Activable — mecánica interesante pero necesita clarificar tipo | Aclarar |
| Contagio | ⚠️ Coste 3, Activable — refleja daño verdadero con probabilidad | Aclarar |

**Rudimentos existentes**
| Carta | Coste | Valoración | Qué hacer |
|---|---|---|---|
| Interferencias cruzadas | 0 | ✅ Redirigir daño con coste propio — muy Disonancia | Conservar |
| Vínculo Corrupto | 0 | ✅ Compartir daño, mecánica de vínculo arriesgado | Conservar |
| Silencio Abrupto | M | ⚠️ Contrahechizo que te hace perder el turno — coste enorme, revisar si es jugable | Revisar |
| Desfase | 0 | ✅ Diferir daño, gestión de riesgo — elegante | Conservar |
| Ecos del pasado | 0 | ✅ Forzar repetir tirada con penalización propia — identidad clara | Conservar |
| Canción de Muerte | 0 | 🔴 Puede matar a todo el campo por coste 0 — desproporcionado | Reequilibrar coste o condición |

**Mecánica central sugerida:** Intercambiar consecuencias — dar y recibir a la vez, manipular quién recibe qué. Todo tiene un precio.

---

### Melodía
**Situación actual:** 3 fundamentos + 6 rudimentos → sobran 1F y 2R

**Fundamentos existentes**
| Carta | Valoración | Qué hacer |
|---|---|---|
| Pulsos Adulterados | ✅ Estado aleatorio en Pulsos — temático y activo en cada turno | Conservar |
| Alcance Mejorado | ⚠️ Muy genérico, podría ser de cualquier elemento | Revisar o reemplazar por algo más temático de Melodía |
| Dolor Selectivo | ⚠️ Evolucionado peor que la base (aleatorio vs control total) | Corregir Evolucionado |

**Rudimentos existentes**
| Carta | Coste | Valoración | Qué hacer |
|---|---|---|---|
| Sabor Agridulce | 3 | ✅ Zona de veneno persistente, temático | Conservar |
| Nota Punzante | 3 | ✅ Proyectil que atraviesa y acumula daño — elegante | Conservar |
| Lluvia de Notas | X | ⚠️ Element sincopa en bucket melodia — confuso; revisar pertenencia | Revisar |
| Aturdidora | M | ✅ Explosión con triple estado — poderosa, justifica coste M | Conservar |
| Mal de Ojo | M | ✅ Cadena de explosiones al morir — muy Melodía oscura | Conservar |
| Se Avecina Tormenta | X | ✅ Trampas en campo, setup claro | Conservar |

**Mecánica central sugerida:** Control de zonas y estados — colocar efectos en el tablero que el enemigo activa al moverse.

---

### Tempo
**Situación actual:** 2 fundamentos + 0 rudimentos → **diseño completo necesario**

**Fundamentos existentes**
| Carta | Valoración | Qué hacer |
|---|---|---|
| Y un, dos, tres... | ⚠️ Texto idéntico a Crescendo — uno es placeholder | Rediseñar uno de los dos |
| Crescendo | ⚠️ Texto idéntico a Y un, dos, tres... | Rediseñar uno de los dos |

La idea de "turno extra al neutralizar" es buena para uno de los dos. El otro necesita un concepto diferente dentro de Tempo (rapidez de reacción, iniciativa, anticipación).

**Rudimentos:** Crear 4 desde cero. Referencia de mecánicas de Tempo: interrupciones, stuns, ralentizar enemigos, robar iniciativa, reacciones fuera de turno.

---

## Orden de rediseño propuesto

1. **Armonía** — más cartas existentes aprovechables, buen punto de partida
2. **Ritmo** — similar, solo hay que elegir y limpiar
3. **Síncopa** — aclarar Activables, luego hay buen material
4. **Disonancia** — resolver Canción de Muerte y Activables
5. **Melodía** — el más cercano a funcionar
6. **Tempo** — rediseño completo al final

---

## Checklist de redesign por elemento

Para cada elemento, antes de cerrar el set:
- [ ] 2 fundamentos con coste 0 en frontmatter
- [ ] 4 rudimentos, al menos uno de coste 0 o 1
- [ ] Todos usan notación `[DI]` y `[DI+AT]`
- [ ] Mecánica central descrita en una frase
- [ ] Existe un combo natural de 2-3 habilidades
- [ ] Ningún Evolucionado es peor que la base
- [ ] Sin habilidades que hagan lo mismo entre sí
