# storm-compact — ontwerp (aanzet)

**Status:** aanzet (2026-08-01).

## Principe

`compact` = **de structuur/vorm van `volledig`** (gelaagd, IMOW-objecten,
ref-based, sectioneel — géén artikel-inline zoals `integrated`) **∩ de
element­ondersteuning van SimplicIT** (`SimplicIT.Domain.Project`). Oftewel: neem
de faithful DSO-vorm en snoei die tot exact wat de plansoftware kan dragen.

Zo is compact een **realistische, DSO-vormige uitwisselkern** die zowel de
volledige DSO-structuur als de plansoftware "begrijpen". Compact is de
**normaliserende, lossy afvoerput**: `volledig → compact` en
`integrated → compact` kunnen wél; terug niet (behalve door generatie).

## Wat blijft, wat sneuvelt, wat klapt samen

| volledig | in compact? | reden (SimplicIT-ondersteuning) |
|---|---|---|
| gelaagde vorm (tekst-laag + object-laag + secties) | **blijft** | dit is de "structuur van volledig" |
| `Regeltekst` + `JuridischeRegel` als aparte objecten met `artikelOfLid`-ref | **blijft** (vorm) | SimplicIT kent `OwRegeltekstIdentificatie` + `OwJuridischeRegelIdentificatie` |
| 3 regel-subtypes (`RegelVoorIedereen`/`Instructieregel`/`Omgevingswaarderegel`) | **klapt samen** tot één `JuridischeRegel` | SimplicIT maakt geen subtype-onderscheid |
| `idealisatie`, per-regel `locatieaanduiding`/`gebiedsaanwijzing`/`kaartaanduiding`/`omgevingsnormaanduiding` | **weg** | SimplicIT draagt ze niet op de regel |
| `ActiviteitLocatieaanduiding` (activiteit + regelkwalificatie + **locatie**) | **snoeit** tot `activiteitaanduiding` (activiteit + regelkwalificatie) | SimplicIT `ActiviteitAanduiding` heeft geen locatie |
| `Activiteit` | **blijft** (+ `juridischeRegelRef` back-link) | 1:1 aanwezig |
| `Omgevingsnorm` **én** `Omgevingswaarde` | **klapt samen** tot `Omgevingsnorm`; `Normwaarde` zonder `waardeInRegeltekst` | SimplicIT heeft alleen `Omgevingsnorm`+`Normwaarde` |
| `Gebiedsaanwijzing`, `Ambtsgebied`, `Regelingsgebied`, `Pons`, `Hoofdlijn` | **blijft** | 1:1 aanwezig |
| `Locaties` (`Gebied`/`Punt`/`Lijn`/groepen met `noemer`/`hoogte`/geometrie) | **snoeit** tot minimale `Locatie` (`identificatie` + `geometrieRef`) | SimplicIT: locatie = ref + GML-bytes (GridFS), geen locatie-objectgraaf |
| `Kaart`/`SymbolisatieItem` | **weg** | SimplicIT kent geen kaarten |
| verbatim STOP-metadata (procedure/consolidatie/…) | **weg**, alleen scalars (`naam`/`type`/`bevoegdGezagCode`/`frbr*`/…) | SimplicIT houdt alleen identiteit over |
| geometrie (GIO-GML) | **`Bestand`-verwijzing** | SimplicIT: GML in GridFS als `BestandRef` |
| tekst-laag (STOP verbatim, incl. CALS/inline) | **strikt** i.p.v. wildcard: alleen de STOP-elementen die SimplicIT parseert | SimplicIT `StopXmlParser` → `ContentBlok`-model |

## Vorm

- Namespace `urn:storm:compact`; **hergebruikt** `storm-basis` (`Ref`/`NEN3610ID`)
  en de tekst-vocabulaire van `storm-tekst` (strikte `Tekst`-wrapper i.p.v. de
  wildcard die `volledig` gebruikt).
- `Regeling` (envelop, minimale metadata-attrs) → `Tekst` + `CompactObjecten`.
- `CompactObjecten`: `Regels` (`Regeltekst` + `JuridischeRegel`), `Activiteiten`,
  `Normen`, `Gebiedsaanwijzingen`, `Locaties` (minimaal), `Regelingsgebied`,
  `Pons`, `Hoofdlijnen`, `Bestanden`. **Geen** `Kaarten`.

## Opschrift blijft rijk (verwijzingen behouden)

SimplicIT kent **geen opgeslagen "bewerkbaar"-vlag** op het opschrift. Bij een
pull bewaart de `StopXmlParser` juist de content-marks (`IntRef`/`ExtRef`/`sup`/
`sub`) op de opschrift-runs; de editor rendert een opschrift dan **read-only**
zodra er marks op staan (bewuste tussenmaatregel: een plat-tekst-edit zou de
geïmporteerde verwijzing vernietigen). Het nummer-deel is server-waarheid
(auto-nummering). Bron: SimplicIT `StopXmlParser.ParseOpschrift`,
`document-component-kop.component.ts`, `docs/plans/.../opmaak-in-opschriften.md`.

**Gevolg voor compact:** het opschrift MOET zijn verwijzingen/opmaak kunnen
dragen — anders valt weg wat het read-only-gedrag stuurt. compact doet dat al:
via `storm-tekst` is `Kop.Opschrift` een rijke `Tekstregel` (inline `IntRef`/
`ExtRef`/`sup`/`sub`) met een apart `Nummer`. Dus **opschrift niet platslaan** in
`volledig → compact`; de marks blijven behouden. (Zie het marked-up opschrift in
`compact-mini`.)

## Open punten (te bevestigen)

1. **Regel n:1 vs 1:1** — compact houdt de *vorm* van volledig (aparte objecten
   met ref), maar SimplicIT is 1:1. Aanzet: één `JuridischeRegel` per
   `artikelOfLid` toestaan (n:1 structureel mogelijk, 1:1 als conventie).
2. **Locatie** — minimale `Locatie{identificatie, geometrieRef}` als brug, of
   locaties helemaal als losse refs + `Bestanden` (zoals SimplicIT)? Aanzet: het
   eerste, om de sectionele volledig-vorm te bewaren.
3. **tekst-curatie** — nu hergebruikt via `storm-tekst`; verdere snoei tot exact
   de SimplicIT-`ContentBlok`-set (bv. `Tussenkop` eruit) is een verfijning.
