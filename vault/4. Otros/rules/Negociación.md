---
dg-publish: true
---
# Negociación

La negociación es un sistema de resolución de encuentros donde los Cantores intentan convencer a un PNJ para que realice una acción específica. A diferencia del combate, la negociación se basa en argumentos persuasivos, no en amenazas directas de violencia.

## Estadísticas de Negociación

Cada PNJ durante una negociación tiene cuatro estadísticas temporales:

| Estadística | Descripción |
|------------|-------------|
| **Interés** | Escala 0-5. Nivel de disposición del PNJ a hacer un acuerdo. Si llega a 5, el PNJ hace su oferta final. Si cae a 0, la negociación termina sin acuerdo. |
| **Paciencia** | Escala 0-5. Cantidad de esfuerzo que el PNJ está dispuesto a dedicar. Al llegar a 0, hace su oferta final y la negociación termina. |
| **Motivaciones** | Al menos 2. Argumentos que invocan estas motivaciones requieren un test de dificultad media. Cada motivación solo puede ser apelada una vez. |
| **Escollos** | Al menos 1. Argumentos que mencionen estos elementos causan automáticamente fallo y reducen Interés y Paciencia en 1. |

## Actitud Inicial del PNJ

| Actitud      | Descripción                                                      | Interés | Paciencia |
| ------------ | ---------------------------------------------------------------- | ------- | --------- |
| **Hostil**   | Abiertamente opuesto. Apenas dispuesto a escuchar.               | 1       | 2         |
| **Suspicaz** | Duda de los motivos pero está dispuesto a escuchar.              | 2       | 2         |
| **Neutral**  | Sin opinión formada. Preferiría estar en otra parte.             | 2       | 3         |
| **Abierto**  | Dispuesto a escuchar y ayudar, si no pides demasiado.            | 3       | 3         |
| **Amigable** | Te considera un aliado. Dispuesto a dar el beneficio de la duda. | 3       | 4         |
| **Confiado** | Tiene razones para creerte. Ayudará si no lo arruinas.           | 3       | 5         |

## Idioma y Paciencia

Si uno o más Cantores pueden comunicarse en el idioma nativo del PNJ, aumenta su Paciencia +1 (máximo 5). Si tres o más pueden hacerlo, aumenta +2.

## Hacer Argumentos

Un Cantor hace un argumento para convencer al PNJ. Este argumento puede:
- Apelar a una de sus Motivaciones
- Ofrecer algo a cambio
- Convencer al PNJ de que es en su propio interés

### A) *Apelando a una Motivación*

**Dificultad: Media** | **Test: Razón, Intuición o Presencia + Habilidad interpersonal**

| Resultado  | Efecto                  |
| ---------- | ----------------------- |
| **Tier 1** | Paciencia 1             |
| **Tier 2** | Interés +1, Paciencia 1 |
| **Tier 3** | Interés +1              |

### B) *Sin Motivación ni Escollo*

**Dificultad: Difícil** | **Test: Razón, Intuición o Presencia + Habilidad interpersonal**

| Resultado | Efecto |
|-----------|--------|
| **Tier 1** | Interés 1, Paciencia 1 |
| **Tier 2** | Paciencia 1 |
| **Tier 3** | Interés +1, Paciencia 1 |
| **Natural 19-20** | Paciencia se mantiene |

### C) *Usando un Escollo*

El argumento **falla automáticamente**. Interés 1, Paciencia 1.

### *D) Atrapado en una Mentira*

Si un argumento falla y el PNJ descubre que fue mentira, además de los efectos de fallo: Interés -1 adicional.

## Oferta del PNJ

Tras cada argumento, el PNJ responde con una oferta basada en su Interés actual:

| Interés | Respuesta | Oferta |
|---------|-----------|--------|
| **5** | "Sí, y..." | Todo lo solicitado + extras adicionales |
| **4** | "Sí" | Todo lo solicitado tal como se pidió |
| **3** | "Sí, pero..." | Lo solicitado a cambio de una pequeña petición adicional |
| **2** | "No, pero..." | Alternativa menor a lo solicitado en lugar del acuerdo |
| **1** | "No" | Rechazo sin contraoferta. Pueden continuar argumentos si queda Paciencia. |
| **0** | "No, y..." | Fin de negociación. El PNJ busca dañar a los Cantores. |

## Motivaciones y Escollos

| Motivación | Descripción | Escollo | Descripción Escollo |
|-----------|-----------|---------|----------|
| **Benevolencia** | El PNJ cree en compartir con otros. Los argumentos que muestren cómo el acuerdo beneficiará a personas que le importan son efectivos. | Cinismo | El PNJ no cree que nadie merezca algo sin ganárselo. |
| **Descubrimiento** | El PNJ quiere aprender, explorar o descubrir secretos. Los argumentos sobre conocimiento único son efectivos. | Miedo a lo desconocido | Prefiere la ignorancia a la incertidumbre. |
| **Libertad** | El PNJ quiere autonomía, para sí o para otros. Los argumentos sobre mantener o ganar libertad son efectivos. | Orden absoluto | Cree que se necesita autoridad para evitar el caos. |
| **Codicia** | El PNJ desea riqueza y recursos. Los argumentos sobre ganancia material son efectivos. | Ideales por encima de todo | Se ofende ante intentos de compra. |
| **Autoridad Superior** | El PNJ es leal a un ser, organización o fuerza mayor. Los argumentos que alinean el acuerdo con los intereses de esa autoridad son efectivos. | Independencia radical | Rechaza servir a cualquiera. |
| **Justicia** | El PNJ quiere que los buenos sean recompensados y los malvados castigados (según su código). Los argumentos que lo posicionan al lado del bien son efectivos. | Cinismo moral | Cree que la justicia no existe. |
| **Legado** | El PNJ desea fama eterna y que se recuerde. Los argumentos sobre su gloria futura son efectivos. | Humildad | Ve el legado personal como vanidad. |
| **Paz** | El PNJ quiere calma y tranquilidad. Los argumentos que le permiten mantener su statu quo son efectivos. | Sed de emoción | Odia el aburrimiento y quiere drama. |
| **Poder** | El PNJ desea autoridad e influencia. Los argumentos que aumenten su poder son efectivos. | Rechazo a la autoridad | No quiere gobernar ni ser gobernado. |
| **Protección** | El PNJ quiere proteger algo o a alguien a toda costa. Los argumentos que ayuden a su protección son efectivos. | Indiferencia | No siente responsabilidad por otros. |
| **Juerga** | El PNJ quiere diversión, socialización y placer. Los argumentos que le permiten disfrutar son efectivos. | Sobriedad | Ve la diversión como pérdida de tiempo. |
| **Venganza** | El PNJ quiere dañar a quien le ha herido. Los argumentos que permiten su venganza son efectivos. | Perdón | Cree que la venganza no resuelve nada. |

## Continuidad de la Negociación

- Si el Interés es 1-4 y la Paciencia > 0, los Cantores pueden hacer más argumentos.
- Si el Interés es 5 o la Paciencia llega a 0, el PNJ hace su oferta final.
- Si el Interés cae a 0, la negociación termina sin acuerdo posible.
- Los Cantores pueden rechazar cualquier oferta y terminar la negociación en cualquier momento.
