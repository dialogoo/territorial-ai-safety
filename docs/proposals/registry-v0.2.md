# Propuesta: registro de indicadores v0.2

**Estado:** propuesta, pendiente de aprobación · **Fecha:** 2026-08-17 · **Afecta a:** `analysis/registry/indicators.yml`

`CLAUDE.md` establece que los indicadores, las ponderaciones y las direcciones son decisiones de
investigación y no ediciones de código: se proponen, no se editan. Este documento es la propuesta.
Nada del registro cambia hasta que esté aprobado o enmendado por escrito.

## El problema

El registro actual (v0.1.0) tiene **seis indicadores en dos pilares**, todos con `weight: 1.0` y
todos con `source: TBD`.

| pilar | indicadores actuales |
|---|---|
| `exposure` | `intermediation_depth`, `channel_concentration`, `labor_leverage_exposure` |
| `resilience` | `polycentric_governance`, `civic_density`, `channel_redundancy` |

El white paper de AI SAFE EARTH, en su sección 10, define **seis factores**: cinco capacidades que
suman y una vulnerabilidad que resta. Al cruzarlos con el registro aparecen tres desajustes.

### 1. Faltan dos factores

- **Apertura y pluralismo.** Es el quinto factor y el white paper es explícito sobre su función:
  sin él, los otros cuatro pueden medir exactamente lo contrario de lo que pretenden. Un pueblo
  homogéneo dominado por una élite local puntúa alto en decisión «distribuida» entre los de
  siempre, propiedad «local» del cacique y densidad cívica de asociaciones que excluyen. Sin este
  factor el índice no distingue una comunidad resiliente de una comunidad opresiva. El registro
  no tiene ningún indicador para él.
- **Propiedad local.** De quién son la economía, los medios y la infraestructura. También ausente.

### 2. Riesgo de circularidad entre los dos pilares

El white paper compromete que la exposición se mida **con observables propios** y nunca como el
inverso definicional de la resiliencia; si no, los dos pilares son una sola variable con el signo
cambiado. Hoy `channel_concentration` (exposición) y `channel_redundancy` (resiliencia) están
peligrosamente cerca de ser esa misma variable. La propuesta debe separarlas por fuente de dato,
no solo por nombre.

### 3. El esquema no puede expresar cómo se mide un indicador

Los campos disponibles son `id`, `name`, `pillar`, `direction`, `weight`, `source`, `rationale`.
No hay forma de declarar unidad, añada, cobertura, licencia ni normalización. El lado conceptual
del registro es real; el lado de medición está vacío.

## Lo que se propone

### A. Estructura: seis factores dentro de dos pilares

Los dos pilares se conservan —son la forma en que se combina el índice— y los seis factores del
white paper se convierten en un nivel intermedio explícito, de modo que cada indicador declare a
qué factor pertenece:

| factor (white paper §10) | pilar | indicadores |
|---|---|---|
| Decisión distribuida | `resilience` | `polycentric_governance` |
| Redundancia de canales | `resilience` | `channel_redundancy` |
| Densidad cívica | `resilience` | `civic_density` |
| Propiedad local | `resilience` | **nuevo** |
| Apertura y pluralismo | `resilience` | **nuevo** (probablemente más de uno) |
| Exposición a la captura | `exposure` | `intermediation_depth`, `channel_concentration`, `labor_leverage_exposure` |

*TODO: proponer los indicadores concretos de los dos factores nuevos, cada uno con una fuente
española candidata verificada. Pendiente de la búsqueda de datos de la fase 4; no se inventan
aquí.*

### B. Esquema: campos nuevos por indicador

```yaml
- id: civic_density
  name: Civic and cooperative density
  name_es: Densidad cívica y cooperativa
  pillar: resilience
  factor: civic_density          # NUEVO — el factor del white paper §10
  direction: positive
  weight: 1.0
  unit: asociaciones por 1.000 habitantes   # NUEVO
  source: TBD
  source_url: TBD                # NUEVO
  vintage: TBD                   # NUEVO — año de referencia del dato
  coverage: TBD                  # NUEVO — provincia / municipio
  licence: TBD                   # NUEVO
  normalization: minmax          # NUEVO — explícito, no implícito en el código
  rationale: ...
```

`name_es` y unas etiquetas `pillars_es` / `factors_es` permiten que `render_book.py` genere la
tabla del libro en español sin que el pipeline invente nombres: hoy las celdas salen en inglés
dentro de prosa española precisamente porque el pipeline no debe traducir por su cuenta.

### C. Ponderaciones

Todo a 1.0 es una decisión sin declarar. El white paper compromete que **ninguna ponderación se
publique sin su análisis de sensibilidad al lado**, así que la propuesta de pesos debe llegar
junto al capítulo 10, no antes.

*TODO: proponer el esquema de ponderación y su justificación cuando el capítulo de robustez
tenga el análisis de sensibilidad.*

### D. Nombre del índice

`meta.index_name` es hoy `Territorial AI-Safety Index`, un nombre que ya no se usa. El white paper
lo llama **Índice de Seguridad Territorial en IA**. El libro se llama **AI Safe Territory**.

Propuesta: `index_name: Índice AI Safe Territory`, con `index_name_en: AI Safe Territory Index`.
Mantiene el nombre propio del proyecto y evita reintroducir la denominación antigua.

## Qué hay que decidir

1. ¿Se acepta el nivel intermedio `factor` con los seis factores del white paper?
2. ¿Se aceptan los campos nuevos de medición y los campos bilingües?
3. ¿Se acepta el nombre del índice?
4. Los indicadores de **propiedad local** y **apertura y pluralismo** se proponen cuando existan
   fuentes españolas verificadas para ellos, o se declara el hueco en el libro si no las hay.
