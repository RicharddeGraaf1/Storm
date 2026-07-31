# Gemeentestad — storm-volledig

Faithful storm-volledig-pakket, gegenereerd uit de échte Gemeentestad-bron
(STOP-besluit + IMOW-deelbestanden + GIO-wrappers uit de oefen-opdracht), niet
uit de integrated `storm.xml`. Platte map. Valideert tegen
`../../xsd/storm-volledig.xsd` (+ de storm-gio's tegen `../../xsd/storm-gio.xsd`).

Inhoud:

- **`storm-volledig.xml`**
  - **Metadata** (`urn:storm:data`): besluit- + regeling-metadata verbatim
    (`BesluitMetadata`, `Procedureverloop`, `ConsolidatieInformatie`,
    `RegelingMetadata`) — nodig voor verliesvrij `volledig ↔ download`.
  - **Tekstlaag** (`urn:storm:tekst`): regelingstructuur, 22 artikelen.
  - **Objectlaag** (`urn:storm:ow`): 14 Regelteksten, 21 juridische regels,
    16 activiteiten, 14 gebieden + 6 gebiedengroepen + ambtsgebied,
    2 gebiedsaanwijzingen, 3 normen met 6 normwaarden, regelingsgebied, pons.
- **`*.storm-gio.xml`** (`urn:storm:gio`): per GIO één zelfstandig bestand dat
  de informatieobject-metadata + symbolisatie + de geometrie bundelt (voorheen
  verspreid over de `AanleveringInformatieObject`-wrapper en het losse `.gml`).
  `storm-volledig.xml` verwijst er via `GeometrieRef` (basisgeo:id) naar.
- **`manifest.xml`**: gecombineerd (STOP `manifest.xml` + IMOW `manifest-ow.xml`).

Bewust nog **niet** meegenomen (schema v0.6.0 eerste-pass):
`Kaart`/`SymbolisatieItem`, de inline-opmaak binnen de tekst (`Al` draagt hier
platte tekst), en de niet-geo IO (`Regdata.pdf`). De besluit/mutatie-tekstlaag
is leeg (geconsolideerde regeling).

Gegenereerd met de kiem van `download2volledig`.
