---
title: "Estadísticas de Negociación"
rules_status: canonical
source_section: "4.1 Estadísticas de Negociación"
version_introduced: "Alpha 0.1.0"
last_reviewed: "2026-05-10"
---

# Estadísticas de Negociación

Cada PNJ durante una negociación tiene cuatro estadísticas temporales:

| Estadística | Descripción |
|------------|-------------|
| **Interés** | Escala 0-5. Nivel de disposición del PNJ a hacer un acuerdo. Si llega a 5, el PNJ hace su oferta final. Si cae a 0, la negociación termina sin acuerdo. |
| **Paciencia** | Escala 0-5. Cantidad de esfuerzo que el PNJ está dispuesto a dedicar. Al llegar a 0, hace su oferta final y la negociación termina. |
| **Motivaciones** | Al menos 2. Argumentos que invocan estas motivaciones requieren un test de dificultad media. Cada motivación solo puede ser apelada una vez. |
| **Escollos** | Al menos 1. Argumentos que mencionen estos elementos causan automáticamente fallo y reducen Interés y Paciencia en 1. |
