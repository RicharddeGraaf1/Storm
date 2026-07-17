# STORM — STandaard Omgevingswet ReferentieModel

Eén standaard (één namespace `urn:storm:1.0`, één XSD) die STOP-tekst,
IMOW-annotaties en IMTR-toepasbare-regels in samenhang beschrijft.
Uitwerking van de presentatie "20211119 - mening toekomst standaard.pptx"
(werktitel *Rutopie*).

**Deze repo bevat alleen de standaard zelf** — het normatieve product.
De transformaties (van/naar de DSO-formaten) en de renvooiservice leven in
een aparte repo: [Storm-services](https://github.com/RicharddeGraaf1/Storm-services).

## Inhoud

```
standaard/
├── xsd/storm.xsd              het schema (semver, zie CHANGELOG.md)
├── specificatie/             STORM-specificatie.md (patronen + mappingtabellen)
├── CHANGELOG.md              versiegeschiedenis van het schema
├── profiel-compact/          onderbouwing van het compact-profiel (10%-knip)
└── voorbeelden/
    ├── mini/                 klein handgemaakt pakket (storm.xml + gio/)
    └── Gemeentestad/         volledig voorbeeld uit de Gemeentestad-oefencasus
tools/valideer.py             self-check: valideert alle voorbeelden (lxml)
```

## Een STORM-pakket

Een STORM-pakket is `storm.xml` naast een `gio/`-map (en optioneel `io/`):

- **`storm.xml`** — de regeling: tekststructuur met inline annotaties
  (regelType/idealisatie/thema als attributen), de OW-objecten, de
  geo-verwijzingen, de exportregels en — bij een aanlevering — de
  LVBB-envelop.
- **`gio/*.gml`** — de geometrie én de normwaarden leven hier (niet
  gedupliceerd in `storm.xml`); regel-locaties worden gedestilleerd uit de
  IntIoRefs in de tekst.
- **`io/`** — niet-geo informatieobjecten (bv. PDF-bijlagen).

Zie [standaard/specificatie/STORM-specificatie.md](standaard/specificatie/STORM-specificatie.md).

## Valideren

Elk voorbeeld draagt een `xsi:schemaLocation` naar het online schema
(raw GitHub), zodat het in bv. Oxygen direct valideert. Open
`standaard/voorbeelden/Gemeentestad/storm.xml` om het te zien.

Self-check van de hele repo:

```powershell
pip install lxml
python tools/valideer.py
```

## Profielen

De standaard kent één vocabulaire (**complete**, dekt alle vigerende
praktijk-fragmenten) en één restrictieprofiel (**compact**, knip = 10%
spreiding over de vigerende regelingen). Het compact-profiel is een
restrictie, geen tweede XSD; de onderbouwing staat in
[standaard/profiel-compact/](standaard/profiel-compact/). De conversie
`complete → compact` zit in de tooling (Storm-services).

## Versie

Standaard **v0.5.0** — zie [standaard/CHANGELOG.md](standaard/CHANGELOG.md).
Versiebeleid: semver op `xsd/storm.xsd`.
