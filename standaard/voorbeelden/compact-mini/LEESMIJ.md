# compact-mini — storm-compact (aanzet)

Klein hand-voorbeeld van de **compact**-variant (`../../xsd/storm-compact.xsd`).
Valideert met lxml.

compact = **de structuur/vorm van volledig** (gelaagd, IMOW-objecten, ref-based,
sectioneel) **∩ de elementondersteuning van SimplicIT**. Zie het ontwerp in
`../../specificatie/compact-ontwerp.md`.

Dit voorbeeld toont:

- **Volledig-vorm behouden**: aparte `Tekst`-laag (STOP-vocabulaire via
  `storm-tekst`) + `CompactObjecten` met secties (`Regels`/`Activiteiten`/
  `Normen`/`Gebiedsaanwijzingen`/`Locaties`/`Regelingsgebied`/`Bestanden`);
  `Regeltekst` + `JuridischeRegel` als aparte objecten met `artikelOfLid`-ref.
- **SimplicIT-snoei**: één `JuridischeRegel` (geen subtypes), alleen
  `activiteitaanduiding`(activiteit + regelkwalificatie) + `thema` op de regel;
  geen `idealisatie`/per-regel locatie-/gebieds-/kaart-/norm-koppeling. Norm
  zonder `waardeInRegeltekst`. `Locatie` minimaal (`identificatie` +
  `geometrieRef`). **Geen `Kaarten`.** Geometrie als `Bestand`-verwijzing.

Aanzet — open punten (regel n:1↔1:1, locatie-modellering, verdere tekst-curatie)
staan in de ontwerpnota.
