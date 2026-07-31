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
  - **Tekstlaag** (`urn:storm:tekst`): de STOP-tekst **verbatim** — deepcopy met
    alleen de namespace hernoemd naar `urn:storm:tekst`. Alles blijft behouden:
    22 artikelen, de 4 bijlagen, de artikelgewijze toelichting, tabellen,
    inline-opmaak (`i`/`b`/`IntRef`/`Noot`/…), en alle `eId`/`wId`. Faithful,
    dus permissief gevalideerd (`Tekst` = `xs:any` skip).
  - **Objectlaag** (`urn:storm:ow`): 14 Regelteksten, 21 juridische regels,
    16 activiteiten, 14 gebieden + 6 gebiedengroepen + ambtsgebied,
    2 gebiedsaanwijzingen, 3 normen met 6 normwaarden. `Regelingsgebied`, `Pons`
    en `Kaarten` (met de welstandskaart) zijn eigen secties direct onder
    `OwObjecten`.
- **`*.storm-gio.xml`** (`urn:storm:gio`): per GIO één zelfstandig bestand dat
  de informatieobject-metadata + symbolisatie + de geometrie bundelt (voorheen
  verspreid over de `AanleveringInformatieObject`-wrapper en het losse `.gml`).
  `storm-volledig.xml` verwijst er via `GeometrieRef` (basisgeo:id) naar.
- **`manifest.xml`**: gecombineerd (STOP `manifest.xml` + IMOW `manifest-ow.xml`).

Bewust nog **niet** meegenomen: de niet-geo IO (`Regdata.pdf`). De
besluit/mutatie-tekstlaag is leeg (geconsolideerde regeling).
`SymbolisatieItem` is in de laatste IMOW vervallen en zit niet in het model.
`Regelingsgebied`/`Pons` staan als `0..1` in de `xs:all` van `OwObjecten`
(XSD 1.0-beperking); meerdere per regeling is een latere stap.

Gegenereerd met `naar_volledig.py` (kiem van `download2volledig`). De
`download → volledig`-richting is informatie-behoudend geverifieerd op 261
echte geconsolideerde downloadpakketten (zie `Storm-services`
`python/download_roundtrip.py`).
