# STORM-varianten: volledig, integrated, compact

**Status:** ontwerp (2026-07-28) — het model is vastgesteld; de veld-indeling
van *integrated* en het normalisatie-regelboek van *compact* worden nog
uitgewerkt.

STORM kent drie varianten van dezelfde regeling. Ze verschillen niet in
"grootte van het vocabulaire" maar langs **twee assen**:

- **as 1 — waar leeft de annotatie?** uit elkaar getrokken in zij-objecten
  (*volledig*) versus ingevouwen op het artikel (*integrated*);
- **as 2 — hoeveel behoud je?** volle regeling (*volledig*/*integrated*)
  versus genormaliseerde reductie (*compact*).

```
   volledig  ⇄ verliesvrij ⇄  integrated
  (hub voor download-          (hub voor de eigen plansoftware,
   pakketten; DSO-trouw,        Rutopie; alles op het artikel,
   objecten expliciet)          ergonomisch bewerken)
        \                        /
         \   lossy normalisatie /
          ↓                    ↓
                compact
   (uniforme reductie: ≥10%-vocabulaire én structurele
    normalisatie zoals "één juridische regel per regeltekst";
    slaat de exotische varianten uit de bronstandaarden plat)
```

## De drie varianten

| Variant | Doel / consument | Structuurkenmerk |
|---|---|---|
| **volledig** | aanleveren/uitleveren van **downloadpakketten**; 1-op-1 mapping naar STOP/IMOW/IMTR | alle IMOW-identiteiten expliciet in zij-blokken (`OwObjecten`, `Geo`, `Exportregels`); dicht bij de bronformaten |
| **integrated** | de **eigen plansoftware**: bewerken/redigeren | annotatie ingevouwen op `Artikel`/`Lid`; zo min mogelijk zij-objecten; IMOW-identiteiten afgeleid bij export |
| **compact** | **transformatie-mechanisme**: variëteit platslaan | genormaliseerd (o.a. één regel per regeltekst) + ≥10%-vocabulaire; lossy |

## Transformatie-lattice

| van ↓ / naar → | volledig | integrated | compact |
|---|---|---|---|
| **volledig** | — | ✅ verliesvrij | ⬇️ lossy |
| **integrated** | ✅ verliesvrij | — | ⬇️ lossy |
| **compact** | ❌ (alleen inflaten met defaults) | ❌ | — |

- **volledig ↔ integrated** dragen dezelfde informatie in een andere vorm →
  een verliesvrije bijectie. Elk is de hub van zíjn eigen workflow.
- **alles → compact** is een lossy normalisatie. Compact is een afvoerput:
  je gaat er naartoe om de rommelige variëteit van de echte standaarden
  uniform te maken; verliesvrij terug hoeft niet.

## Drie schema's

Omdat integrated de structuur hervormt en compact normaliseert, zijn dit
geen simpele XSD-restricties van elkaar. Er komen drie schema's boven op een
gedeelde type-bibliotheek:

- `storm-volledig.xsd` — ≈ de huidige `storm.xsd` (objecten expliciet)
- `storm-integrated.xsd` — artikel-centrisch (in ontwerp)
- `storm-compact.xsd` — gereduceerd + genormaliseerd

Een document declareert zijn variant (via `xsi:schemaLocation` naar het
juiste profiel-XSD en/of een `@variant`-attribuut op `Regeling`), zodat een
afnemer weet welk vocabulaire hij mag verwachten.

## Twee open specificaties

1. **De bijectie volledig ↔ integrated.** Dit is de dragende claim; die
   wordt met dezelfde rondreis-discipline als de DSO-round-trips bewezen
   (canonieke vergelijking, verliesvrij in beide richtingen). Voorwaarde
   voor verliesvrijheid: integrated draagt de oorspronkelijke
   IMOW-identiteiten als optionele *provenance* (`@owId` e.d.) mee, zodat
   `integrated → volledig → download` exact dezelfde owId's oplevert.

2. **Het normalisatie-regelboek van compact.** "Eén juridische regel per
   regeltekst" is er één van; verder o.a. het platslaan van meerdere
   `Regel`-dragers per lid, samengestelde gebiedsaanwijzingen en de
   <10%-vocabulaire-staart. Dit regelboek bepaalt precies wat compact
   "opeet".

## Integrated — ontwerprichting (wordt geschetst)

Het principe: **los het `Exportregels`-blok op** door de IMOW-identiteiten
op de regel-annotatie van het artikel te hangen, en **leid ze bij export
weer af**. Wat gedeeld is (n:m of regeling-breed) houdt een kleine pool:

- **blijft gedeeld**: `Activiteit`-definities (door veel regels gebruikt),
  de GIO-catalogus (`Geo`), `Ambtsgebied`/`Regelingsgebied`/`Pons`,
  `Hoofdlijn`.
- **vouwt op het artikel**: locatie-, norm- en gebiedsaanwijzing-verwijzing
  per regel; de `ImowLocatie`/`ImowNorm`/`ImowGebiedsaanwijzing`-identiteiten
  worden bij `integrated → volledig` afgeleid (groeperen op gedeelde GIO,
  owId's uit provenance of vers gemunt).
- **blijft extern**: geometrie en normwaarden in de GML; op het artikel
  staat alleen de *verwijzing* naar de GIO, niet de waarde (conform het
  v0.2-besluit tegen duplicatie).

De veld-indeling (welke velden als attribuut vs. kind-element, granulariteit
van de regel per lid) wordt in samenspraak uitgewerkt.

## Relatie tot eerdere besluiten

- Dit **vervangt** de framing van 2026-07-17 ("één vocabulaire *complete* +
  gegenereerd restrictieprofiel *compact*"). Compact is nu een
  transformatie-output met eigen invarianten, niet louter een deelverzameling.
- De term **volledig** vervangt **complete** in code, CHANGELOG en CLI
  (uitgestelde rename).
- Geometrie/normwaarden blijven in de GML (v0.2); integrated voegt alleen
  verwijzingen inline toe.
