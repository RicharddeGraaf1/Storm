# STORM-varianten: volledig, integrated, compact

**Status:** ontwerp (2026-07-31) — het model en de dragende ontwerpkeuzes zijn
vastgesteld; de exacte XSD-veldindeling van *integrated* en het volledige
normalisatie-regelboek van *compact* worden bij de bouw afgerond.

STORM kent drie varianten van dezelfde regeling. Ze verschillen niet in
"grootte van het vocabulaire" maar langs **twee assen**:

- **as 1 — waar leeft de annotatie?** uit elkaar getrokken in zij-objecten
  (*volledig*) versus ingevouwen op het artikel (*integrated*);
- **as 2 — hoeveel behoud je?** faithful superset (*volledig*) versus
  genormaliseerde vorm (*integrated*, *compact*).

```
        volledig            faithful exchange- / downloadhub
        │   ▲                (n:1 regels per regeltekst; alle
        │   │                 IMOW-identiteiten expliciet)
 norma- │   │ verliesvrij
 liseert│   │ (widening)
        ▼   │
     integrated             authoring-hub voor de eigen plansoftware
        │                    (Rutopie; 1:1 regel per regeltekst;
        │                     annotatie op het artikel)
        ▼
      compact               normaliserende afvoerput
                             (1:1 + ≥10%-vocabulaire; lossy)
```

## De drie varianten

| Variant | Doel / consument | Structuurkenmerk | Regels per regeltekst |
|---|---|---|---|
| **volledig** | **downloadpakketten** aanleveren/uitleveren; 1-op-1 met STOP/IMOW/IMTR | IMOW-identiteiten expliciet in zij-blokken (`OwObjecten`, `Geo`, `Exportregels`) | **n:1** (faithful) |
| **integrated** | de **eigen plansoftware**: bewerken/redigeren | annotatie ingevouwen op `Artikel`/`Lid`; zij-objecten geminimaliseerd; IMOW-nummers als herkomst | **1:1** |
| **compact** | **transformatie-mechanisme**: variëteit platslaan | 1:1 + ≥10%-vocabulaire; lossy | **1:1** |

## Transformatie-lattice

De transformaties zijn **niet** allemaal verliesvrij; alleen `integrated →
volledig` is dat. De andere richtingen normaliseren (slaan de faithful
variëteit van de bronstandaarden plat).

| van ↓ / naar → | volledig | integrated | compact |
|---|---|---|---|
| **volledig** | — | ⚠️ normaliseert (n:1 → 1:1) | ⬇️ lossy |
| **integrated** | ✅ verliesvrij (widening) | — | ⬇️ lossy |
| **compact** | ❌ (alleen inflaten met defaults) | ❌ | — |

Praktisch:

- **Je eigen plannen publiceren**: authoring in *integrated* → *volledig* →
  download is een **verliesvrije** keten (jij bouwt 1:1 by construction; de
  IMOW-nummers reizen als herkomst mee, of worden bij export gemunt).
- **Een externe download bekijken/bewerken**: download → *volledig*
  (faithful) → *integrated* **normaliseert** een regeltekst met meerdere
  juridische regels naar 1:1 — precies het soort exotische variant dat ook
  *compact* opeet. *volledig* blijft de faithful bewaarplaats.

## Drie schema's

Omdat integrated de structuur hervormt en compact normaliseert, zijn dit
geen simpele XSD-restricties van elkaar. Er komen drie schema's boven op een
gedeelde type-bibliotheek:

- `storm-volledig.xsd` — ≈ de huidige `storm.xsd` (objecten expliciet)
- `storm-integrated.xsd` — artikel-centrisch, 1:1
- `storm-compact.xsd` — gereduceerd + genormaliseerd

Een document declareert zijn variant één keer op de root (`@variant` +
`xsi:schemaLocation` naar het juiste profiel-XSD). Elementnamen blijven
**gelijk** over de varianten (bv. `OwObjecten`): een document valideert tegen
precies één schema, dus dezelfde naam mag per variant een andere inhoud
hebben. Geen variant-achtervoegsels op elementnamen — dat zou transformaties
tot hernoemen dwingen en de renvooi/diff met schijnverschillen vervuilen.

## Twee open specificaties

1. **De losslessness-keten `integrated → volledig → download`.** Dit is de
   dragende garantie; die wordt met de rondreis-discipline (canonieke
   vergelijking) bewezen. Voorwaarde: integrated draagt de oorspronkelijke
   IMOW-identiteiten als optionele **herkomst** (`@owId` e.d.) mee, zodat de
   terugweg exact dezelfde nummers oplevert. Daarnaast documenteren we
   expliciet **wat `volledig → integrated` normaliseert** (multi-regel-teksten
   e.d.), zodat het verlies bekend en verantwoord is.
2. **Het normalisatie-regelboek van compact.** "1:1 regel per regeltekst"
   deelt het met integrated; compact voegt de ≥10%-vocabulaire-reductie toe,
   plus het platslaan van samengestelde gebiedsaanwijzingen e.d. Dit regelboek
   bepaalt precies wat compact opeet.

## Integrated — ontwerpkeuzes

Het principe: **los het `Exportregels`-blok op** door de verwijzingen op de
regel-annotatie van het artikel te hangen; leid de IMOW-administratie bij
`→ volledig` weer af. Vastgesteld:

- **Eén `Regel` per regeltekst** (1:1). Attributen op de regel: `soort`,
  `idealisatie`, `thema`, en `owId` als **herkomst** (alleen aanwezig bij een
  geïmporteerd plan; leeg bij vers redigeren, dan gemunt bij export).
- **Locatie = expliciete `gioRef`** op de regel (geen destillatie uit
  IntIoRefs; die destillatie was een reconstructie-truc voor downloads). De
  leesbare `IntIoRef` in de lopende tekst blijft staan; de machine-locatie
  staat expliciet.
- **Geen `<Norm>`-element.** Type, eenheid, waarde én richting
  (ten hoogste / ten minste) zitten al in de norm-GIO; de regel verwijst er
  alleen naar (`soort="omgevingswaarderegel"` markeert dat het een normregel
  is). Het IMOW-nummer van de norm reist als herkomst op die verwijzing mee.
- **IMOW-nummers**: *volledig* bewaart de volledige administratie
  (`Exportregels`: `ImowLocatie`/`ImowNorm`/`ImowGebiedsaanwijzing` met
  owId's/basisgeoId/gioWork). *integrated* en *compact* bewaren die
  administratie niet, maar plaatsen het **IMOW-nummer als herkomst** op de
  betreffende verwijzing (locatie, norm, gebiedsaanwijzing).
- **Gedeelde pool** houdt één naam (`OwObjecten`) en krimpt in integrated tot
  vooral `Activiteit`-definities; de GIO-catalogus (`Geo`),
  `Ambtsgebied`/`Regelingsgebied`/`Pons` en `Hoofdlijn` blijven gedeeld omdat
  ze n:m of regeling-breed zijn.
- **Extern blijft extern**: geometrie en normwaarden in de GML; op het artikel
  staat alleen de verwijzing, nooit de waarde (v0.2-besluit tegen duplicatie).

## Relatie tot eerdere besluiten

- Dit **vervangt** de framing van 2026-07-17 ("één vocabulaire *complete* +
  gegenereerd restrictieprofiel *compact*"). Compact is nu een
  transformatie-output met eigen invarianten, niet louter een deelverzameling;
  en er zijn drie varianten, geen twee.
- De term **volledig** vervangt **complete** in code, CHANGELOG en CLI
  (uitgestelde rename).
- Geometrie/normwaarden blijven in de GML (v0.2); integrated voegt alleen
  verwijzingen inline toe.
