# Handoff — AI Safe Territory

## Dónde está el proyecto

El repositorio es el libro de investigación de **AI Safe Territory**, un proyecto bajo el paraguas
de la organización **AI SAFE EARTH**. No confundir: la organización tiene su white paper; este
libro hace el método que aquel documento anuncia y difiere explícitamente aquí.

La maquinaria está bien montada y el libro está casi vacío. Un registro único
(`analysis/registry/indicators.yml`) alimenta la prosa y el cálculo, las tablas generadas se
commitean y CI falla si se desfasan, y la identidad v2 de AI SAFE EARTH ya está aplicada al tema.
Lo que falta es escribir.

Al empezar esta sesión el libro tenía ~1.000 palabras en total, de las cuales 328 eran el prefacio
y 168 la lista de referencias: 15 de 18 páginas eran stubs idénticos. Todo número publicado son
datos aleatorios de demostración, correctamente etiquetados como tales.

## Qué se hizo en esta sesión (2026-08-17)

**Identidad.** Se aplicó la marca v2 al tema de mdBook: emblema del proyecto en el masthead de la
barra lateral, favicons, wordmark en la portada, componentes de identidad (`ase-label`,
`ase-plate`, `ase-scalebar`), y los assets copiados a `src/assets/brand/`.

**Plan de escritura.** Acordado el ciclo de trabajo: Oscar escribe los briefs de todos los
capítulos → revisamos la narrativa y reorganizamos → Oscar reescribe los briefs que cambien →
Claude redacta los borradores → Oscar edita y valida capítulo a capítulo.

**Fase 0 ejecutada.** El libro es ahora español (fuente de verdad; el inglés será traducción), los
nombres antiguos están retirados, hay 18 briefs precargados esperando y una propuesta de registro
sobre la mesa.

**Commit y push.** Un único commit (`c2eb948`, 91 archivos) que además cierra la migración desde
Quarto: se borran el árbol `.qmd`, `_quarto.yml`, la caché `_freeze` y los SCSS de marca. Hubo que
rebasar sobre dos commits que ya estaban en remoto (`b967a83`, `2422b6b`, del 10 de agosto) que
renombraban «territorial AI safety» a «AI Safe Territory» dentro de los archivos Quarto; el
conflicto se resolvió manteniendo los borrados, porque ese mismo renombrado ya está aplicado en
`book.toml` y en `src/index.md`. No se perdió nada.

**El sitio NO se ha actualizado.** El job de build de CI pasó; el de deploy fue rechazado. La causa
son ajustes del repositorio, no el código —ver el bloqueo abajo—. El sitio en vivo sigue sirviendo
la versión Quarto antigua desde la rama `gh-pages`.

## Decisiones tomadas

- **Idioma:** español canónico, inglés como traducción, montada después de que la espina dorsal
  esté estable. mdBook 0.4.52 no tiene modo multilingüe: serán dos builds desde una sola raíz,
  español en la raíz del sitio e inglés en `/en/`.
- **Nombre:** **AI Safe Territory** en todas partes, también en prosa española. Ni «Territorial AI
  Safety», ni «AI Safe Territories», ni «AI Safe Earth» (esa es la organización).
- **Orden:** espina dorsal fina en todas las páginas primero, después profundizar.
- **Unidad del piloto:** dos niveles, provincias (NUTS-3) y un puñado de municipios a mano.
- **Voz:** primera persona en los capítulos del marco; impersonal y procedimental en Metodología y
  apéndices, que deben leerse como un libro de códigos ejecutable por otro.
- **Extensión:** 1.200–2.000 palabras por capítulo.
- **Fuentes:** se busca y se verifica en abierto, y toda cita llega con enlace, publicación y
  localizador. Lo que no tenga fuente verificada se queda como `*TODO:*`.

## Lo que está bloqueado esperando a Oscar

1. **Publicación.** Dos ajustes en Settings del repositorio, que Oscar hace a mano:
   - **Pages → Build and deployment → Source:** hoy es *Deploy from a branch* (`gh-pages`). Debe
     ser **GitHub Actions**. El README ya lo documentaba como paso único y nunca se hizo.
   - **Environments → `github-pages` → Deployment branches:** hoy solo permite `gh-pages`. Hay que
     añadir **`main`**, o el deploy se rechaza igualmente («Branch main is not allowed to deploy to
     github-pages due to environment protection rules»).

   Después, *Actions → Publish book →* la ejecución fallida *→ Re-run failed jobs*.
2. **Los 18 briefs** en `docs/briefs/`. Es el paso 1 del ciclo y nada se redacta sin ellos.
3. **La propuesta de registro** `docs/proposals/registry-v0.2.md`. El registro no se toca sin
   aprobación escrita: faltan indicadores para dos de los seis factores del white paper —apertura
   y pluralismo, y propiedad local— y el nombre del índice sigue siendo el antiguo.

## Avisos

- **No borrar la rama `gh-pages`** hasta que el sitio nuevo se vea bien: es el rollback, contiene
  el HTML de la versión Quarto.
- Lo que saldrá publicado es honesto pero muy delgado: prefacio, dos capítulos de metodología a
  medias y 15 páginas que dicen «Borrador — capítulo aún sin escribir». Todo número del sitio está
  etiquetado como dato aleatorio de demostración. Es el estado esperado de un documento vivo en
  v0.x, pero conviene saberlo antes de que la URL empiece a servirlo.
- El capítulo 07 afirma la fórmula `Exposición × Susceptibilidad ÷ Resiliencia` y nadie la deriva.
  O la deriva el 06 o desaparece.
- Ningún capítulo posee hoy el diseño de validación ni la predicción registrada, y el white paper
  los promete en público. Decidir dónde viven en la fase 2.

```json
{
  "project": "ai safe territory",
  "org": "ai safe earth",
  "status": "amber",
  "updated": "2026-08-17",
  "deadline": null,
  "people": ["oscar"],
  "plans": [
    { "name": "book", "path": "docs/briefs/", "status": "active" },
    { "name": "registry-v0.2", "path": "docs/proposals/", "status": "active" }
  ],
  "phases": [
    { "name": "Fase 0 — andamiaje", "status": "done", "start": "2026-08-17", "end": "2026-08-17", "plan": "book",
      "decisions": [
        { "date": "2026-08-17", "text": "Español como fuente de verdad, inglés como traducción posterior" },
        { "date": "2026-08-17", "text": "El libro se llama AI Safe Territory; AI SAFE EARTH es la organización" },
        { "date": "2026-08-17", "text": "Piloto a dos niveles: provincias NUTS-3 y un puñado de municipios" },
        { "date": "2026-08-17", "text": "Toda cita con enlace, publicacion y localizador verificables" },
        { "date": "2026-08-17", "text": "Migracion desde Quarto cerrada en el mismo commit; conflicto de rebase resuelto manteniendo los borrados de _quarto.yml e index.qmd" },
        { "date": "2026-08-17", "text": "No borrar la rama gh-pages: es el rollback del sitio hasta validar la publicacion nueva" }
      ] },
    { "name": "Fase 1 — espina dorsal", "status": "planned", "start": null, "end": null, "plan": "book", "decisions": [] },
    { "name": "Fase 2 — revision y reorganizacion", "status": "planned", "start": null, "end": null, "plan": "book", "decisions": [] },
    { "name": "Fase 3 — borradores completos", "status": "planned", "start": null, "end": null, "plan": "book", "decisions": [] },
    { "name": "Fase 4 — datos reales", "status": "planned", "start": null, "end": null, "plan": "book", "decisions": [] },
    { "name": "Fase 5 — edicion en ingles", "status": "planned", "start": null, "end": null, "plan": "book", "decisions": [] }
  ],
  "blockers": [
    { "text": "El sitio no se publica: Pages sigue en modo rama gh-pages y el entorno github-pages no permite deploy desde main. Dos ajustes en Settings", "severity": "high", "owner": "oscar", "since": "2026-08-17" },
    { "text": "Los 18 briefs de capitulo estan vacios; nada se redacta sin ellos", "severity": "high", "owner": "oscar", "since": "2026-08-17" },
    { "text": "Propuesta de registro v0.2 pendiente de aprobacion; faltan indicadores para apertura y pluralismo y para propiedad local", "severity": "medium", "owner": "oscar", "since": "2026-08-17" },
    { "text": "Sin datos reales: data/processed/indicators.csv no existe y las 6 fuentes son TBD", "severity": "medium", "owner": "oscar", "since": "2026-08-17" }
  ],
  "nextSteps": [
    { "title": "Cambiar Pages a GitHub Actions y permitir deploy desde main, y relanzar el workflow", "est": 0.5, "owner": "oscar", "phase": "Fase 0 — andamiaje", "plan": "book" },
    { "title": "Escribir los briefs de los 18 capitulos", "est": 3, "owner": "oscar", "phase": "Fase 1 — espina dorsal", "plan": "book" },
    { "title": "Aprobar o enmendar la propuesta de registro v0.2", "est": 1, "owner": "oscar", "phase": "Fase 1 — espina dorsal", "plan": "registry-v0.2" },
    { "title": "Redactar la espina dorsal de las 18 paginas, 400-600 palabras cada una", "est": 4, "owner": "claude", "phase": "Fase 1 — espina dorsal", "plan": "book" }
  ],
  "sessions": [
    { "date": "2026-08-17", "model": "opus-5", "credits": null, "person": "oscar", "hours": 3 }
  ]
}
```
