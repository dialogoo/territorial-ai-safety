# Pilares e indicadores

El marco agrupa los indicadores en dos familias —**exposición y susceptibilidad** (lo que eleva el riesgo) y **resiliencia de la agencia** (lo que protege)— siguiendo la lógica introducida en [El modelo de resiliencia](06-resilience-model.md).

> El riesgo se lee como **Exposición × Susceptibilidad ÷ Resiliencia de la agencia**.

Cada indicador se define una sola vez, en el registro legible por máquina `analysis/registry/indicators.yml`, que alimenta tanto el cálculo ([La construcción del índice](09-constructing-the-index.md)) como el libro de códigos (ver el apéndice). La tabla siguiente se genera desde ese registro mediante `analysis/pipeline/render_book.py`, de modo que no puede contradecir al código.

{{#include ../generated/indicators-table.md}}

*TODO: justificar la validez de constructo de cada indicador — el vínculo entre el mecanismo y la medida.*

*TODO: resolver la fórmula anterior. Está afirmada aquí y no se deriva en ningún sitio; o la deriva el capítulo 06 o desaparece.*
