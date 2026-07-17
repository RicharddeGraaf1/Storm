# Changelog — de STORM-standaard

Versiebeleid: semver op `xsd/storm.xsd`. Major = breaking voor bestaande
STORM-pakketten, minor = nieuwe optionele elementen/attributen, patch =
verduidelijking zonder schema-effect.

## 0.4.0 — 2026-07-17

**Complete + compact.** Besluit: de standaard kent één vocabulaire
(**complete**) en één restrictieprofiel (**compact**, knip = 10% spreiding
over de vigerende regelingen; besluit gebruiker 2026-07-17). Geen tweede
XSD; profiel + conversie in code.

- Complete-vocabulaire volgemaakt met de sub-10%-elementen: `Tussenkop`,
  `Kadertekst`, `Groep`, `Lijstaanhef`/`Lijstsluiting`, `InleidendeTekst`,
  `Aanhef` (+Considerans/Afkondiging), `Sluiting` (+Ondertekening/
  Slotformulering/Dagtekening), `Contact`, `InlineTekstAfbeelding`,
  `abbr`; structuur conform de staart-inventaris. Het vocabulaire dekt nu
  **alle** 499k vigerende inhoud-fragmenten (99,98% geldig).
- Vreemde-namespace-attributen (renvooi:, dso:) generiek toegestaan op de
  tekstlaag (anyAttribute op Tekstregel).
- Nieuw: machineleesbaar profiel compact (`src/storm/profielen.py`) en
  conversie `complete2compact` (`src/storm/compact.py`, CLI-werkwoord)
  met tekstbehoud-invariant; massabewijs: 13.835 staart-fragmenten →
  99,94% conform, 0 conversiefouten, 0 tekstveranderingen.
- Hernoemd: profiel-light → **profiel-compact**.

## 0.3.0 — 2026-07-17

Empirische dekking-uitbreiding op basis van de elementgebruik-analyse
(`profiel-light/elementgebruik.md`) en een praktijk-inventaris van 20.890
fragmenten; massavalidatie tegen 485k vigerende inhoud-fragmenten uit de
OCD-dev-DB: **99,99% geldig**.

- **CALS-tabellen**: `table` (title/Bron/tgroup), `tgroup`, `colspec`,
  `thead`/`tbody`, `row`, `entry` — attributen conform praktijk
  (frame/tabstyle/pgwide, namest/nameend/morerows/rotate, …); toegestaan
  in `Inhoud`, `Li` en `Definitie`.
- **Opmaak**: `i`, `b`, `u`, `strong` als nestbare Tekstregel-elementen;
  `sup`/`sub` idem (waren leaf-only).
- **Noot-familie**: `Noot` (id/type, NootNummer + Al/Lijst), `Nootref`.
- **`Bron`** (bronvermelding bij table en Figuur), **`Titel`** als
  figuur-titel én als structuurelement, **`Subsubparagraaf`**.
- `Illustratie@alt`; vreemde-namespace-attributen (renvooi:, dso:)
  toegestaan op Begrippenlijst/Figuur/Illustratie/table via anyAttribute.
- Bekende rest (54 van 485k fragmenten): bron-afwijkingen zoals een
  Begrippenlijst gevuld met lijst-items — bewust niet gemodelleerd.

## 0.2.0 — 2026-07-15

- **STORM-pakket**: geometrie en normwaarden leven in de GIO-GML-bestanden
  (`gio/` naast `storm.xml`); geen duplicatie meer in het document.
- `Geo/Gio` is een verwijzing (work/expressie/bestand) met alleen de
  gebiedsaanwijzing-velden erop.
- `Regel/Locatieaanduiding` optioneel: locatie destilleerbaar uit de
  IntIoRefs van het artikel/lid, of ambtsgebied-default.
- Nieuw `Exportregels`-compartiment: IMOW-identiteiten (`ImowLocatie`),
  norm-administratie (`ImowNorm` — waarden uit de GML) en de
  aanwijzing-fallback (`ImowGebiedsaanwijzing`).
- `OwObjecten/Norm` vervallen (afgeleid bij export).

## 0.1.0 — 2026-07-15

- Eerste versie: één namespace `urn:storm:1.0`; STOP-tekststructuur met
  inline annotaties (regelType/idealisatie/thema als attributen, `Regel`/
  `Tekstdeel` als verliesvrije dragers); IMOW als module; IMTR-module met
  STORM-native STTR-kern + verbatim ingebedde DMN-beslislogica.
