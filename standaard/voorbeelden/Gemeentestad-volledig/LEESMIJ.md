# Gemeentestad — storm-volledig

Faithful storm-volledig-pakket, gegenereerd uit de échte Gemeentestad-bron
(STOP-besluit + IMOW-deelbestanden uit de oefen-opdracht), niet uit de
integrated `storm.xml`. Platte map: `storm-volledig.xml` + `manifest.xml` +
de GIO-GML's. Valideert tegen `../../xsd/storm-volledig.xsd`.

Inhoud (gespiegeld uit de bron):

- **Tekstlaag** (`urn:storm:tekst`): de regelingstructuur (hoofdstukken,
  22 artikelen, leden, koppen, inhoud).
- **Objectlaag** (`urn:storm:ow`): 14 Regelteksten, 21 juridische regels,
  16 activiteiten, 14 gebieden + 6 gebiedengroepen + ambtsgebied,
  2 gebiedsaanwijzingen, 3 normen met 6 normwaarden, regelingsgebied, pons —
  gekoppeld aan de tekst via `wId` en aan elkaar via `@ref`.
- **Geometrie**: extern in de GML's (`Locatie → GeometrieRef → basisgeo:id`).

Bewust nog **niet** meegenomen in deze eerste generatie (schema is v0.6.0
eerste-pass): `Kaart`/`SymbolisatieItem`, en de inline-opmaak binnen de
tekst (`Al` draagt hier platte tekst). De besluit/mutatie-laag is leeg
(dit is de geconsolideerde regeling).

Gegenereerd met de kiem van `download2volledig`.
