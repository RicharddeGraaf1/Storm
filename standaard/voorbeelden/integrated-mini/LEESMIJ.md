# integrated-mini — storm-integrated

Klein hand-voorbeeld van de **integrated**-variant (`../../xsd/storm-integrated.xsd`).
Valideert met lxml (XSD 1.0) en `xmlschema` (XSD 1.1).

storm-integrated is **1-op-1 gemodelleerd op het SimplicIT.Domain.Project**-model,
zodat `integrated ↔ SimplicIT` een mechanische mapping is en de variant exact
dekt wat de plansoftware ondersteunt. Zie de veld-mapping in
`Storm-services/TRANSFORMATIE-ARCHITECTUUR.md` §4a.

Kenmerken die dit voorbeeld toont:

- **Annotatie ÓP de regel** (het integrated-patroon): `Artikel`/`Lid` dragen
  `owRegeltekstIdentificatie` / `owJuridischeRegelIdentificatie` +
  `ActiviteitAanduiding` + `Thema` — geen aparte juridische-regel-objecten.
- **ContentBlok/TekstRun-laag**: `Alinea` met `TekstRun`s en een `Mark`
  (`kind="intRef"`) voor inline-verwijzing; `Begrippenlijst` in een `Bijlage`.
- **OW-objecten als platte pools** op `Regeling`: `Activiteiten`,
  `Omgevingsnormen`(+`Normwaarde`/`LocatieRef`), `Gebiedsaanwijzingen`,
  `Ambtsgebied`, `Regelingsgebied`, `Ponsen`, `Hoofdlijnen`. Locaties zijn
  string-refs; geometrie zit als `Bestand` (verwijzing, inhoud extern/GridFS).

NB: `Regelingsgebied`/`Ponsen`/`Hoofdlijnen` staan hier ingevuld — die draagt
storm-volledig ook, terwijl de huidige SimplicIT-DSO-import ze leeg laat (een
`volledig → SimplicIT`-adapter kan ze dus vullen).
