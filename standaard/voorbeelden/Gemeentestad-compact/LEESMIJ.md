# Gemeentestad — storm-compact

Gegenereerd uit `../Gemeentestad-volledig` met de transformatie
`volledig → compact` (`Storm-services/python/volledig_compact.py`). Valideert
tegen `../../xsd/storm-compact.xsd`.

Dit is de **vocabulaire-projectie**: dezelfde STOP-structuur als volledig, maar
gesnoeid tot de SimplicIT-ondersteuning (zie `../../specificatie/varianten.md`
en `compact-ontwerp.md`).

Wat de transform deed:

- **Tekst** verbatim overgenomen (opschrift-marks/verwijzingen behouden — niet
  platgeslagen).
- **Regels**: 14 `Regeltekst` + 21 `JuridischeRegel` (subtypes samengeklapt);
  `idealisatie` behouden (of Exact als default); `ActiviteitLocatieaanduiding`
  → `activiteitaanduiding` (activiteit + regelkwalificatie, **zonder locatie**).
- **Activiteiten** (16) met afgeleide `juridischeRegelRef`-backlinks.
- **Normen** (3): `Omgevingswaarde` samengeklapt in `Omgevingsnorm`; `Normwaarde`
  zonder `waardeInRegeltekst`.
- **Gebiedsaanwijzingen** (2), **Locaties** (21, minimaal: id + geometrieRef),
  **Regelingsgebied**, **Ponsen**.
- **Bestanden** (9): de geometrie uit de storm-gio's als `Bestand`-verwijzing.
- **Kaarten**: bewust weggelaten (geen SimplicIT-ondersteuning).
- **Metadata** → scalars op `Regeling` (naam/type/soortRegeling/bevoegdGezagCode/
  frbrWork).

Éénrichting-lossy: `compact → volledig` vereist generatie (Kaarten, locatie-
objectgraaf, verbatim metadata zijn weg).
