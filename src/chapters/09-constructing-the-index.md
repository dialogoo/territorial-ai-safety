# La construcción del índice

El compuesto se construye siguiendo el manual de la OCDE y el JRC ([OECD & JRC 2008](../references.md#oecd2008composite)): normalizar cada indicador, ponderarlo y agregarlo. Cada decisión es deliberada y queda registrada; [Robustez](10-robustness.md) comprueba después cuánto depende el ranking de ellas.

El pipeline está **dirigido por el registro**: lee el mismo `indicators.yml` que el resto del libro, así que el método aquí descrito *es* el método que se ejecuta.

```python
{{#include ../../analysis/pipeline/demo_index.py:demo}}
```

Al ejecutarlo produce:

{{#include ../generated/demo-index.md}}

<div class="callout callout-important">

**Datos de demostración.** La tabla anterior son datos aleatorios. Todavía no se está evaluando ningún territorio. Los resultados reales aparecerán cuando `data/processed/indicators.csv` esté poblado (ver [Pilares e indicadores](07-pillars-and-indicators.md) y el apéndice de datos).

</div>

*TODO: sustituir la normalización min-max y la agregación lineal por la normalización elegida y una opción geométrica; documentar las ponderaciones.*
