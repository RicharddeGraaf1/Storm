# STORM volledig → compact: het normalisatie-regelboek

**Status:** ontwerp (2026-07-31) — uitwerking van open specificatie #2 uit
[varianten.md](varianten.md). Dezelfde dag herzien na toetsing tegen
**TPOD omgevingsplan §5.2.1.1**; die toetsing draaide één conclusie om (zie
[A-1](#a-1--aantekening-naast-inhoud-op-een-container)) en legde twee defecten
bloot ([N2](#n2--structuurlaag-twee-hernoemingen--defect) en
[A-2](#a-2--artikel-en-lid-status-naast-inhoud)).

`volledig → compact` is **lossy en eenrichtingsverkeer**. Dat is de bedoeling:
compact is de afvoerput waar de faithful variëteit van STOP/IMOW wordt
platgeslagen. Juist omdat het verlies gewild is, moet elke plek waar iets
sneuvelt hier staan — anders is het geen normalisatie maar een bug die niemand
ziet.

Terminologie: dit document gebruikt **volledig**; oudere stukken (waaronder
[../profiel-compact/elementgebruik.md](../profiel-compact/elementgebruik.md))
schrijven nog *complete*. Zie de uitgestelde rename in
[varianten.md](varianten.md#relatie-tot-eerdere-besluiten).

## Drie normen, niet één

De belangrijkste les uit de TPOD-toetsing: "de standaard" is geen enkelvoud.
Er liggen drie lagen over elkaar, en ze zeggen niet hetzelfde.

| Laag | Wat het voorschrijft | Wie handhaaft |
|---|---|---|
| **STOP-XSD** (IMOP-tekst) | Wat een geldig document mág zijn. Ruim. | De LVBB, hard, bij aanlevering |
| **TPOD** per documenttype | Wat een omgevingsplan / omgevingsverordening / waterschapsverordening / AMvB *moet* zijn. Veel strakker. | Grotendeels niet machinaal — daarom wijkt de praktijk af |
| **De praktijk** | Wat er feitelijk in het register staat | — |

Daaruit volgt de rolverdeling in STORM:

- **volledig spiegelt de STOP-XSD.** Faithful betekent: alles accepteren wat de
  LVBB accepteert. Een constructie afwijzen die in het register staat, is voor
  volledig een defect — ook als de TPOD hem verbiedt.
- **compact mag de TPOD afdwingen.** Dat is precies wat een normaliserende
  variant hoort te doen: de variëteit terugbrengen tot wat het toepassingsprofiel
  voorschrijft.
- Een regel die verder gaat dan de TPOD hoort in [register A](#register-a--waar-wij-strenger-zijn-dan-de-norm).
  Een constructie waar de praktijk van de TPOD afwijkt hoort in
  [register B](#register-b--waar-de-praktijk-afwijkt-van-de-norm).

**De TPOD-norm is niet voor elk documenttype dezelfde**, en dat is voor compact
bepalend. §5.2.1.1 geldt voor **Artikelstructuur** en staat vrijwel woordelijk
gelijk in de profielen voor omgevingsplan, omgevingsverordening,
waterschapsverordening en AMvB/MR. Documenten met **Vrijetekststructuur**
(omgevingsvisie, programma) vallen er niet onder: die kennen Divisie/Divisietekst,
en juist daar zijn `Tussenkop`, `Citaat` en `Kadertekst` wél toegestaan. Een
compact-regel die dat verschil negeert, sloopt in het ene documenttype wat in het
andere verboden is.

## Het meetcorpus

Alle tellingen in dit document zijn van **2026-07-31**, over een deelverzameling
van de DSO-downloadbundel van 2026-07-30: veertien bevoegde gezagen, 876
regelingversies, waarvan **261 uitgepakt** (43 unieke regelingen). Daarvan zijn
219 pakketten Artikelstructuur en 42 Vrijetekststructuur.

Dat corpus is klein en bewust scheef: het is geselecteerd op grootte-extremen en
lange versiereeksen, niet op representativiteit. Percentages hieronder zijn
richtinggevend, geen vaststelling. Zodra de volledige bundel op schijf staat
horen ze opnieuw gemeten.

## Invarianten

1. **Tekstbehoud** — de genormaliseerde tekstinhoud verandert niet. Elementen
   mogen verdwijnen of hernoemd worden; woorden niet.
2. **Schema-geldigheid** — de uitkomst valideert tegen `storm-compact.xsd`.
3. **TPOD-conformiteit** — de uitkomst voldoet aan de structuurnorm van het
   toepassingsprofiel van zijn documenttype. Nieuw sinds deze herziening, en de
   reden dat N2 een defect blijkt.
4. **Eén richting** — er is geen `compact → volledig`.
5. **Geen stille afwijking** — zie de twee registers.

Invariant 1 en 3 kunnen botsen; N2 is daar het voorbeeld van. Waar dat gebeurt
wint niet automatisch één van beide, maar wordt de keuze hier opgeschreven.

## De normalisaties

### N1 — Vocabulaire: de 10%-knip, gesplitst per structuurtype

Elementen onder 10% spreiding zitten niet in compact; documenten die ze gebruiken
worden gedegradeerd naar het dichtstbijzijnde equivalent. Banden en massabewijs:
[../profiel-compact/elementgebruik.md](../profiel-compact/elementgebruik.md).

**Herziening nodig.** Die meting liep over alle regelingtypen door elkaar heen,
terwijl de TPOD-norm per structuurtype verschilt. Drie elementen vallen daardoor
verkeerd:

| Element | Artikelstructuur | Vrijetekststructuur | Meting nu |
|---|---|---|---|
| `Tussenkop` | **verboden** (TPOD nr 12) | toegestaan in Divisietekst | 7,0% → onder de knip |
| `Kadertekst` | verboden (niet in de Inhoud-lijst) | toegestaan | 5,7% → onder de knip |
| `Citaat` | verboden | toegestaan | niet apart gemeten |

Voor Artikelstructuur is de knip hier niet streng genoeg maar overbodig: het
element hoort er sowieso niet te staan. Voor Vrijetekststructuur is de knip juist
te streng: hij degradeert iets dat het profiel expliciet toestaat. De knip moet
dus per structuurtype gelden, niet over het geheel.

### N2 — Structuurlaag: twee hernoemingen — **defect**

`elementgebruik.md` schrijft voor: `Titel` → `Hoofdstuk` en `Subsubparagraaf` →
`Subparagraaf`, want beide zitten onder de knip. **Beide hernoemingen leveren een
structuur op die de TPOD expliciet verbiedt.**

Uit Tabel 5 van §5.2.1.1:

- `Titel` staat onder `Hoofdstuk`. Hernoem je hem naar `Hoofdstuk`, dan staat er
  een Hoofdstuk in een Hoofdstuk — en Hoofdstuk "mag niet bevatten: **Hoofdstuk**".
- `Subsubparagraaf` staat onder `Subparagraaf`. Hernoem je hem naar
  `Subparagraaf`, dan staat er een Subparagraaf in een Subparagraaf — en
  Subparagraaf "mag niet bevatten: **Subparagraaf**".

Hernoemen kan dus niet. Wat wel kan is **de laag opheffen**: de kinderen één
niveau omhoog hangen (de `Afdeling`en van een `Titel` worden directe kinderen van
het `Hoofdstuk`; de `Artikel`en van een `Subsubparagraaf` van de `Subparagraaf`).
Dat is TPOD-conform, maar het kost de `Kop` van de opgeheven laag — en een
`Opschrift` is tekst, dus dat botst met invariant 1.

**Nog te beslissen.** Drie opties: (a) de laag opheffen en de Kop laten vallen —
schendt tekstbehoud; (b) de laag opheffen en het Opschrift vóór dat van de ouder
plakken — behoudt de tekst, verandert de ouder; (c) `Titel` en
`Subsubparagraaf` alsnog in compact opnemen — geen verlies, maar twee elementen
meer. Advies: **(c)**. Het zijn twee structuurelementen zonder eigen semantiek, ze
kosten niets in het schema, en beide alternatieven leveren verlies of vervuiling
op om een knip te halen die hier geen doel dient.

Dat advies wordt gesteund door de meting: over 43 unieke regelingen komt
`Subsubparagraaf` in 4 voor (9,3%) — pal op de knip, en op deze steekproef niet
te onderscheiden van "erboven". Structureel `Titel` in 1 van de 43 (19 keer, in 4
pakketten).

⚠️ Bij die telling hoort een waarschuwing die ook voor de oorspronkelijke meting
geldt: **`Titel` is in STOP twee verschillende elementen** — het structuurelement
onder `Hoofdstuk`, en de titel van een `Figuur`. In dit corpus staat `Titel` 1039
keer onder `Figuur` (67 pakketten) tegen 19 keer onder `Hoofdstuk` (4 pakketten).
Wie ze op elementnaam telt, meet een factor 50 te hoog.

### N3 — Regel-as: n:1 → 1:1

Volledig is faithful: één regeltekst kan meerdere `JuridischeRegel`-objecten
dragen; compact kent er één. Wat er met een regeltekst met meerdere gebeurt —
samenvoegen of de tekst splitsen — is **nog niet vastgesteld**.

### N4 — IMOW-administratie → herkomst

Volledig bewaart `Exportregels` met owId's, basisgeoId en gioWork. Compact bewaart
die administratie niet, maar zet het IMOW-nummer als **herkomst** op de
verwijzing. Zie [varianten.md](varianten.md#integrated--ontwerpkeuzes).

### N5 — Samengestelde gebiedsaanwijzingen platslaan

Genoemd in [varianten.md](varianten.md#twee-open-specificaties); de precieze regel
is **nog niet vastgesteld**.

### N6 — Status naast inhoud

Een container die een status-element draagt (`Vervallen`, `Gereserveerd`) én
kinderen heeft, verliest in compact zijn eigen status-element; de kinderen houden
het hunne.

**Dit is niet louter een opruimregel — het is de reparatie van een
TPOD-overtreding.** §5.2.1.1 nr 8 en de aanhef boven Tabel 5 staan slechts één
type uit de kolom "Mag bevatten" toe, en `Vervallen` staat in diezelfde kolom.
Nr 14 zegt bovendien dat een vervallen element "geen inhoud meer" heeft, en de
toelichting dat het element "kan worden **vervangen door** het element Vervallen".
Een `Subparagraaf` met `Vervallen` én acht artikelen voldoet daar niet aan.

**Grond (meting 2026-07-31).** 103 keer draagt een container een status naast
inhoud, in 63 van de 261 pakketten (93 daarvan op een structuurelement). In
**103 van de 103** dragen alle kinderen dezelfde status als de ouder. Er is dus
geen enkel geval waarin de ouder iets zegt dat de kinderen niet al zeggen: het
status-element op de ouder weglaten kost geen informatie, en de uitkomst is
TPOD-conform. Daarnaast staat er 6626 keer een status *zonder* inhoud; die
gevallen raakt deze regel niet.

Zou er ooit een geval opduiken waarin de kinderen een andere of geen status
dragen, dan is weglaten wél verlies en moet de status naar beneden gedistribueerd
worden. De conversie hoort dat te controleren en niet aan te nemen.

De invoerkant blijft ruim: compact **accepteert** de constructie en repareert hem.
Weigeren is iets anders — zie [B-1](#b-1--status-naast-inhoud).

---

## Register A — waar wij strenger zijn dan de norm

Een strengere regel is onzichtbaar. Een element dat we weglaten mist iemand
meteen; een constructie die we weigeren ziet er van buiten uit als een fout in de
bron, terwijl onze regel knelt. Elke regel hier draagt: wat de norm toestaat, wat
wij doen, waarop dat gegrond is, een telling, en het oordeel keuze-of-defect.

### A-1 — Aantekening naast inhoud op een container

**Herzien op 2026-07-31.** Dit stond hier eerst als "wij zijn strenger dan de
standaard". Dat was voorbarig: het klopt tegen de STOP-XSD en niet tegen de TPOD.

| | |
|---|---|
| **STOP-XSD staat toe** | `StructuurElement` = `Kop?` · `gStatus?` · `gStructuur*` — een `sequence`, geen `choice`, dus status én kinderen naast elkaar ([storm-tekst.xsd](../xsd/storm-tekst.xsd), regel 79–86). |
| **TPOD staat het niet toe** | §5.2.1.1 nr 8 + de aanhef boven Tabel 5: slechts één type uit "Mag bevatten", en `Vervallen`/`Gereserveerd` staan in die kolom. Nr 14: een vervallen element "heeft geen inhoud meer". |
| **De praktijk doet het toch** | Zie [B-1](#b-1--status-naast-inhoud). |
| **Oordeel** | **Geen strengere regel.** Wie de constructie afwijst volgt de TPOD; dat is strenger dan de XSD, niet dan de norm. Voor *volledig* geldt wel de faithful-plicht: accepteren, want het staat in het register. Voor *compact* is [N6](#n6--status-naast-inhoud) de afhandeling. |

### A-2 — `Artikel` en `Lid`: status naast inhoud

| | |
|---|---|
| **STOP-XSD staat toe** | Volgens [volledig-objectinventaris.md](volledig-objectinventaris.md#artikel--lid--grondt-opmerking-4), gegrond op de STOP 1.4.1-XSD, is `Artikel` = `Kop` + een choice met **`maxOccurs="2"`**. Twee opties naast elkaar, dus status én inhoud. |
| **TPOD staat het niet toe** | Tabel 5: `Artikel` mag bevatten `Lid`, `Inhoud`, `Gereserveerd`, `Vervallen` — één type daarvan. |
| **Wij doen** | `storm-tekst.xsd` geeft `Artikel` (regel 100–112) en `Lid` (114–126) een `xs:choice` **zonder** `maxOccurs`, dus precies één. |
| **Oordeel** | **Defect in volledig, juiste regel voor compact.** De strengheid zit op de verkeerde plek: volledig is de faithful spiegel en moet dragen wat de LVBB accepteert, ook voor documenttypen met een ander of geen toepassingsprofiel. Verplaats de eis naar compact en zet `maxOccurs="2"` in `storm-tekst.xsd`. |
| **Status** | ⚠️ te verifiëren tegen de IMOP-tekst-XSD zelf. Die staat niet in deze repo en ook niet in `raw/` van het kennismodel-vault; de `maxOccurs="2"` komt uit de objectinventaris en is niet onafhankelijk nagelezen. In de 261 gemeten pakketten kwam het geval niet voor: alle 103 waarnemingen zitten op containers, niet op `Artikel` of `Lid`. |

### Hoe je hier een regel bij zet

Verplicht: de passage uit STOP én uit het relevante TPOD, een waarneming uit echte
pakketten (bevoegd gezag, expressie, eId), een telling over het corpus, en het
oordeel keuze-of-defect. Zonder telling is het een vermoeden en hoort het bij de
open punten.

---

## Register B — waar de praktijk afwijkt van de norm

Compact moet hier doorheen kunnen. Dit is geen kwaliteitsoordeel over
bronhouders: het is de invoer die de conversie feitelijk krijgt. Alle tellingen
over de 219 Artikelstructuur-pakketten van het meetcorpus.

| | Constructie | TPOD | Gemeten |
|---|---|---|---|
| **B-1** | status naast inhoud | nr 8 + nr 14 | 103 keer in 63 pakketten |
| **B-2** | `Noot` / `Nootref` (voet- en eindnoten) | nr 16: niet toegestaan | 2716 keer in 89 pakketten |
| **B-3** | `Tussenkop` | nr 12: niet toegestaan | 2871 keer in 25 pakketten |
| **B-4** | `Redactioneel` | nr 15: niet toegestaan | 5 keer in 5 pakketten |
| **B-5** | `Artikel` direct onder `Titel` | Tabel 5: Titel mag geen Artikel bevatten | 2 keer |
| — | één lagerliggend type per element | nr 8 | **0 overtredingen** |

### B-1 — Status naast inhoud

Het zwaarste geval, omdat het rijksmateriaal is. In `gm0388` (Enkhuizen,
`nld@1-0`, het omgevingsplan van rechtswege, ongewijzigd) draagt
`chp_22__subchp_22.3__subsec_22.3.6__subsec_22.3.6.3` een `<Vervallen/>` naast de
artikelen 22.106 t/m 22.113, die zelf ook `<Vervallen/>` dragen. Hoofdstuk 22 is
de bruidsschat: dit komt van het Rijk en zit in elk omgevingsplan van rechtswege.

Daarmee is de constructie de facto onvermijdelijk. Een importeur die hem afwijst,
wijst elk omgevingsplan af — hoe TPOD-conform die weigering ook is. De import van
de SimplicIT-plansoftware doet dat (`aantekening-xor-inhoud`) en strandt er op
6 van de 10 gemeten gemeentelijke omgevingsplannen; hun volledige meting telt 194
geraakte pakketten. Voor compact is dat geen route: accepteren en repareren
([N6](#n6--status-naast-inhoud)).

### B-2 en B-3 — Noten en Tussenkoppen

Niet marginaal: `Noot` staat in 89 van de 219 Artikelstructuur-pakketten, met 2906
noten onder `Al` alleen al. `Tussenkop` in 25 pakketten. Beide zijn in
Vrijetekststructuur gewoon toegestaan (daar 419 resp. 361 keer, en dan conform) —
wat B-2 en B-3 direct verbindt met de splitsing die [N1](#n1--vocabulaire-de-10-knip-gesplitst-per-structuurtype) nodig heeft.

---

## Gaten in de TPOD zelf

Bij het toetsen bleek §5.2.1.1 op twee punten niet sluitend. Genoteerd omdat een
conversie die erop steunt moet weten waar de norm zwijgt of zichzelf tegenspreekt.

1. **De `Lid`-rij spreekt zichzelf tegen.** In Tabel 5 van het omgevingsplan-
   profiel staat bij `Lid` in "Mag bevatten" *Inhoud, Gereserveerd*, en in "Mag
   niet bevatten" *element Gereserveerd, element Vervallen*. Hetzelfde element in
   beide kolommen. De AMvB/MR-changelog laat zien dat dit met **WELT-152** is
   gerepareerd — daar staat nu alleen *Inhoud* — maar dezelfde correctie is niet
   doorgevoerd in het omgevingsplan- en het waterschapsverordening-profiel.
2. **`NogNietInWerking` komt in het omgevingsplan-profiel niet voor.** Nul
   treffers in het hele document, terwijl STOP het element kent en `storm-tekst.xsd`
   het in `gStatus` heeft. Of het is toegestaan is uit het profiel niet op te maken.

## Open punten

- **N2**: keuze (a)/(b)/(c) vaststellen. Advies (c).
- **N1**: de knip opnieuw meten per structuurtype in plaats van over het geheel.
- **N3** en **N5** zijn nog niet vastgesteld.
- **A-2** wacht op de IMOP-tekst-XSD; klopt de `maxOccurs="2"`, dan is het een
  schemafix in `storm-tekst.xsd`.
- Alle tellingen opnieuw draaien zodra de volledige downloadbundel op schijf staat
  (nu 261 van 3232 versies, 14 van 381 bevoegde gezagen).
- Compact zou een **TPOD-conformiteitsvalidator** kunnen dragen die register B
  rapporteert in plaats van weigert. Dat is precies de informatie die een
  bronhouder nergens anders krijgt.
