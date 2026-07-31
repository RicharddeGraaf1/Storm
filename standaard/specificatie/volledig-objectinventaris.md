# storm-volledig — objectinventaris (gegrond op STOP 1.4.1 + IMOW 2.0)

**Status:** ontwerp/review (2026-07-31). Dit is de gegronde inventaris waarop
`storm-volledig.xsd` wordt gespiegeld. Elke class/property/relatie hieronder is
verbatim uit de bron-XSD's gehaald (geen inferentie); `⚠️` markeert
onzekerheden of bron-eigenaardigheden.

**Bronnen** (in `raw/`):
- STOP-tekst: `standaard-stop-1.4.1/stop/1.4.1/imop-tekst.xsd`
- IMOW 2.0: de 12 XSD's onder `standaard-imow-2.0/IMOW/` (owobject, opobject,
  regels, regelsoplocatie, locatie, gebiedsaanwijzing, regelingsgebied, pons,
  vrijetekst, kaart, symbolisatie, datatypenalgemeen)

## Ontwerpprincipe (de kern van "volledig")

`storm-volledig` is een **faithful spiegel** in één namespace (`urn:storm:1.0`):
alle bronelementen naast elkaar, zónder transformatie. Concreet betekent dat
een **gelaagde** opzet die de bron-realiteit volgt:

1. **Tekstlaag (STOP)** — *pure tekst, géén annotatie erop.* Geen inline
   `Regel`/`Tekstdeel`-dragers, geen `agAnnotatie` op Artikel/Lid. (Dat inline
   vouwen is juist `integrated`.)
2. **Objectlaag (IMOW)** — de annotaties als **eigen objecten** die via `wId`
   naar de tekst wijzen en via `xlink:href`-refs naar elkaar.
3. **Geo blijft extern** — een `Locatie` verwijst met `GeometrieRef` naar een
   externe geometrie (GML/GIO); de STORM-pakketvorm (`storm.xml` + `gio/`)
   blijft.
4. **IMTR-laag** — toepasbare regels (STTR-kern + DMN verbatim), zoals in de
   huidige `ToepasbareRegels` (nog te finaliseren tegen de voorbeelden).

Namespace-collaps: de bron-namespaces (`owobject`, `opobject`, `regels`,
`regelsoplocatie`, `locatie`, `gebiedsaanwijzing`, `kaart`, `symbolisatie`,
`vrijetekst`, `datatypenalgemeen`, `pons`, `regelingsgebied` + STOP-tekst)
worden alle één `urn:storm:1.0`. Elementnamen blijven **verbatim**.

---

## Laag 1 — STOP-tekst (imop-tekst.xsd, ns `…/stop/imop/tekst/`)

STOP gebruikt géén abstracte types of substitutiegroepen; structuur loopt via
benoemde model-groups (`mg…`) en attributegroups (`ag…`). Verbatim-namen
hieronder.

### Regeling-structuurtypes (4) — grondt opmerking #3
- **RegelingCompact** — `RegelingOpschrift` · `Lichaam` · bijlagen
- **RegelingVrijetekst** — `RegelingOpschrift` · `Lichaam`{ Divisie/Divisietekst 1..∞ } · `Bijlage*`
- **RegelingKlassiek** — `RegelingOpschrift?` · `Aanhef?` · `Lichaam` · `Sluiting?` · bijlagen
- **RegelingTijdelijkdeel** — `RegelingOpschrift` · `Lichaam`{ `Conditie` · … } · bijlagen
  - ⚠️ verbatim **kleine d**: `RegelingTijdelijkdeel`.

### Structuurhiërarchie (binnen Lichaam)
`Lichaam` → `mgLichaamStructuur` = choice van `Boek+`/`Deel+`/`Hoofdstuk+`/
`Paragraaf+`/`Afdeling+`/`Titel+`/(`Artikel`|`WijzigArtikel`|`Redactioneel`)*.
Containers (Boek, Deel, Hoofdstuk, Afdeling, Titel, Paragraaf, Subparagraaf,
Subsubparagraaf): elk `Kop` (verplicht) + `mgStatusElementen?` + diepere
containers of bladeren. Hiërarchie is grotendeels vrij/recursief.
- ⚠️ verbatim: `Titel` (niet "Titeldeel"), `Subparagraaf`, `Subsubparagraaf`.

### Artikel / Lid — grondt opmerking #4
- **Artikel** — `Kop` (verplicht) + choice(maxOccurs 2) over
  `Gereserveerd` | `Vervallen` | `NogNietInWerking` | `Inhoud` | `Lid+`.
  Attr o.a. `categorieKlassiek`.
- **Lid** — `LidNummer` (verplicht) + choice(maxOccurs 2) over
  `Vervallen` | `NogNietInWerking` | `Inhoud`. **Geen** `Gereserveerd`.
- De status-opties zijn **lege child-elementen** (geen attribuut):
  `Vervallen`, `Gereserveerd`, `NogNietInWerking`.

### Divisie-tak (vrijetekst)
- **Divisie** — `Kop` · status · `InleidendeTekst?` · (Divisie|Divisietekst)*
- **Divisietekst** — `Kop?` · choice(Gereserveerd|Vervallen|NogNietInWerking|Inhoud)

### Kop / blok / inline (samengevat)
- **Kop**: keuze van `Label`/`Nummer`/`Opschrift` (+ `Subtitel?`).
- **Inhoud**: `Al` | `Groep` | `Lijst` | `Figuur` | `Tussenkop` | `Formule` |
  `Citaat` | `table` (CALS) | `Kadertekst` | `Begrippenlijst`.
- **Inline**: `i`/`b`/`u`/`strong`, `sup`/`sub`, `abbr`, `br`,
  `InlineTekstAfbeelding`, `Noot`/`Nootref`, `Contact`; refs
  `IntRef`/`ExtRef`/`IntIoRef`/`ExtIoRef` (de IntIoRef→ExtIoRef-keten).
- **Identificatie**: `agAKN` = `wId` + `eId` (beide required) op vrijwel elke
  container. Vreemde-namespace-attributen landen via `agAlgemeen`
  (`anyAttribute ##other`) — dit is de haak waar in de download de
  IMOW-annotatie-verwijzingen op de tekst hangen.
- **Mutatie/besluit-laag** (RegelingMutatie, WijzigArtikel, VoegToe/Vervang/
  Verwijder, BesluitCompact/Klassiek, publicatiebladen) bestaat ook — zie
  open beslissing D2 over scope.

---

## Laag 2 — IMOW-objecten (verbatim per class)

Legenda: `→ X` = verwijzing (in de bron via `xlink:href`-Ref-element).
Erfelijkheid via `: Base`. Cardinaliteit `min..max`.

### Abstracte bases
- **OWobject** (abstract) — `status?` (enum `beëindigen`), `procedurestatus?`
  (enum `ontwerp`). Superklasse van bijna alles.
- **OPRegeltekst** (abstract) — `status?`, `procedurestatus?`, **`@wId`
  (required)** = de koppeling naar de STOP-tekst (artikel/lid/formele inhoud).

### Regel-objecten (regels-ns)
- **Regeltekst** (: OPRegeltekst) — `identificatie` (NEN3610ID),
  `gerelateerdeRegeltekst*` → Regeltekst. Draagt `@wId` → STOP-artikel/lid.
  *De kleinste eenheid van bij elkaar horende juridische regels met één
  werkingsgebied.*
- **JuridischeRegel** (abstract : OWobject) — `identificatie`, `idealisatie`
  (waardelijst), `artikelOfLid` → Regeltekst (1..1), `thema*` (**0..∞** — grondt
  opmerking #1), `locatieaanduiding` → Locatie (1..∞), `gebiedsaanwijzing?` →
  Gebiedsaanwijzing, `kaartaanduiding?` → Kaart.
  - **RegelVoorIedereen** — `+ activiteitaanduiding*` (elk: → Activiteit +
    `ActiviteitLocatieaanduiding`), `omgevingsnormaanduiding?` → Omgevingsnorm.
  - **Instructieregel** — `+ instructieregelInstrument*`,
    `instructieregelTaakuitoefening*`, `omgevingsnormaanduiding?` → Omgevingsnorm.
  - **Omgevingswaarderegel** — `+ omgevingswaardeaanduiding?` → Omgevingswaarde.
  - ⚠️ Precies deze drie subtypes; er is **geen** los "Omgevingsnormregel".
    Dit "soort" is dus het **subtype**, niet een attribuut — grondt opmerking
    #5 (hoort nooit bij Divisie/vrije tekst).
- **ActiviteitLocatieaanduiding** (: OWobject) — `identificatie`,
  `activiteitregelkwalificatie` (waardelijst), `locatieaanduiding` → Locatie
  (1..∞).

### Normen & activiteit (regelsoplocatie-ns)
- **Norm** (abstract : OWobject) — `identificatie`, `naam`, `type` (Typenorm
  ⚠️ URI wijst in de XSD naar `Omgevingsnormgroep`), `eenheid?` (WaardeEenheid),
  `normwaarde` → Normwaarde (1..∞).
  - **Omgevingsnorm** — `+ groep` (Omgevingsnormgroep).
  - **Omgevingswaarde** — `+ groep` (Omgevingswaardegroep).
- **Normwaarde** (kaal, geen base) — `identificatie`, `kwalitatieveWaarde?`,
  `kwantitatieveWaarde?` (decimal), `waardeInRegeltekst?` (fixed
  "waarde staat in regeltekst"), `locatieaanduiding` → Locatie (1..∞).
- **Activiteit** (: OWobject) — `identificatie`, `naam`, `groep`
  (Activiteitengroep), `gerelateerdeActiviteit*` → Activiteit,
  `bovenliggendeActiviteit` → Activiteit (**1..1, verplicht**).

### Locaties (locatie-ns)
- **Locatie** (abstract : OWobject) — `identificatie`, `noemer?`.
  - **Gebied** — `+ hoogte?` (WaardeEenheid), `geometrie` → **GeometrieRef** (1).
  - **Punt** — `+ geometrie` → GeometrieRef, `hoogte?`.
  - **Lijn** — `+ hoogte?`, `geometrie` → GeometrieRef.
  - **Gebiedengroep** — `+ groepselement` → Gebied (1..∞). Geen eigen geometrie.
  - **Puntengroep** — `+ groepselement` → Punt (1..∞).
  - **Lijnengroep** — `+ groepselement` → Lijn (1..∞).
  - **Ambtsgebied** — `+ bestuurlijkeGrenzenVerwijzing` (`bestuurlijkeGrenzenID`
    `GM|PV|WS|LND…`, `domein` `NL.BI.BestuurlijkGebied`, `geldigOp`). Geen
    eigen geometrie.
- ⚠️ **GeometrieRef** heeft alleen `xlink:href` — het XSD legt het id-mechanisme
  (basisgeo:id vs gml:id vs GIO-work) **niet** vast; dat komt uit de
  aanleverspec/voorbeeld (in de praktijk `basisgeo:id`).

### Gebiedsaanwijzing / Regelingsgebied / Pons
- **Gebiedsaanwijzing** (: OWobject) — `identificatie`, `type`
  (TypeGebiedsaanwijzing), `naam`, `groep` (Gebiedsaanwijzinggroep),
  `locatieaanduiding` → Locatie (1..∞).
- **Regelingsgebied** (: OWobject) — `identificatie`, `locatieaanduiding` →
  Locatie (**1..1**).
- **Pons** (: OWobject) — `identificatie`, `locatieaanduiding` → Locatie
  (**1..1**). ⚠️ Er is géén `PonsWaarde`-class.

### Vrijetekst-objecten (vrijetekst-ns)
- **Tekstdeel** (: OWobject) — de vrijetekst-tegenhanger van de juridische
  regel. `identificatie`, `idealisatie?`, `thema*`, `divisieaanduiding` →
  (Divisie | Divisietekst) (**1..1, verplicht** — koppeling naar de tekst),
  `hoofdlijnaanduiding*` → Hoofdlijn, `kaartaanduiding*` → Kaart,
  `locatieaanduiding*` → Locatie, `gebiedsaanwijzing*` → Gebiedsaanwijzing.
  **Draagt géén `soort`** (grondt opmerking #5).
- **Divisie** (: OPRegeltekst) — `identificatie`; `@wId` → STOP-Divisie.
- **Divisietekst** (: OPRegeltekst) — `identificatie`; `@wId` →
  STOP-Divisietekst.
- **Hoofdlijn** (: OWobject) — `identificatie`, `soort`, `naam`,
  `gerelateerdeHoofdlijn*` → Hoofdlijn.

### Kaart & symbolisatie
- **Kaart** (: OWobject) — `identificatie`, `naam`, `nummer?`, `uitsnede` →
  Kaartextent, `kaartlagen` → Kaartlaag (1..∞).
- **Kaartlaag** (: OWobject) — `identificatie`, `naam?`, `niveau` (integer),
  `activiteitlocatieweergave*` → ActiviteitLocatieaanduiding, `normweergave*`
  → Omgevingsnorm|Omgevingswaarde, `gebiedsaanwijzingweergave*` →
  Gebiedsaanwijzing.
- **Kaartextent** (kaal) — `minX/minY/maxX/maxY` (decimal).
- **SymbolisatieItem** (kaal, géén OWobject) — `symboolcode` (pattern
  `[a-z]{2,4}[0-9]{3}`), `activiteitLocatieaanduidingSymbolisatie*`,
  `gebiedsaanwijzingSymbolisatie*`, `normwaardeSymbolisatie*`.

### Datatypes (datatypenalgemeen-ns)
- **NEN3610ID** (simpleType) — `nl.imow-(gm|pv|ws|mnre)…​.<objecttype>.<lokaalID>`;
  het objecttype-deel somt alle IMOW-objecttypen op. ⚠️ bronhouder-codes
  `gm|pv|ws|mnre` (Rijk = `mnre`) — wijkt af van `GM|PV|WS|LND` in
  BestuurlijkeGrenzenVerwijzing.
- **WaardeEenheid** — `waarde` (decimal) + `eenheid` (waardelijst-URI).
- **Waardelijsten** (alle `xs:anyURI` met omgevingswet-domeinpattern):
  Idealisatie, Thema, Instrument, Adressaat, Activiteitregelkwalificatie,
  Activiteitengroep, Typenorm, Omgevingsnormgroep, Omgevingswaardegroep,
  TypeGebiedsaanwijzing, Gebiedsaanwijzinggroep, Eenheid.

---

## Koppel-ketens (samengevat)

- **JuridischeRegel → tekst**: `artikelOfLid` → Regeltekst → `@wId` → STOP
  Artikel/Lid.
- **Tekstdeel → tekst**: `divisieaanduiding` → Divisie/Divisietekst → `@wId` →
  STOP Divisie(tekst).
- **regel → locatie**: `locatieaanduiding` → Locatie(-subklasse).
- **regel → activiteit**: alleen `RegelVoorIedereen.activiteitaanduiding` →
  Activiteit + ActiviteitLocatieaanduiding.
- **regel → norm**: `omgevingsnormaanduiding`/`omgevingswaardeaanduiding`;
  normwáárden en hun locaties zitten op `Normwaarde`.
- **locatie → geometrie**: `GeometrieRef` → externe GML/GIO (basisgeo:id, niet
  in XSD afgedwongen).

---

## Hoe je 5 review-opmerkingen hierin landen

1. **thema meervoudig** — faithful: `thema` is 0..∞ op JuridischeRegel én
   Tekstdeel. ✔ (in volledig geen attribuut op de tekst, maar veld op het object)
2. **owJuridischeRegelId vs owRegeltekstId** — het zijn **twee objecten**:
   `Regeltekst` (`identificatie` + `@wId`) en `JuridischeRegel`
   (`identificatie`). In volledig geen ambiguïteit; het "owId"-vraagstuk
   verdwijnt omdat de objecten expliciet zijn. ✔
3. **structuur klassiek/tijdelijkdeel** — `@structuur` = compact | vrijetekst |
   klassiek | tijdelijkdeel (4). ✔
4. **Artikel Vervallen** — + Gereserveerd + NogNietInWerking (3 status-child­
   elementen). ✔
5. **RegelSoort niet bij Divisie** — "soort" = het JuridischeRegel-subtype
   (alleen regelstructuur); vrije tekst gebruikt `Tekstdeel` zonder soort. In
   volledig staat annotatie sowieso niet op de tekst, dus de gedeelde
   `agAnnotatie` verdwijnt. ✔

---

## Open beslissingen vóór ik de XSD schrijf

- **D1 — refs**: de bron gebruikt `xlink:href`-Ref-elementen. In één namespace
  kan dat simpeler met een STORM-eigen `@ref`. Literal `xlink:href` houden
  (maximaal faithful) of `@ref` (schoner)?
- **D2 — scope besluit/mutatie**: neemt volledig alleen de *geconsolideerde
  regeling* (leestekst) + IMOW-objecten, of óók de STOP-besluit/mutatie-laag
  (RegelingMutatie, WijzigArtikel, publicatiebladen)? Advies: leestekst +
  objecten; de aanlever/besluit-administratie blijft in het bestaande
  `Envelop`-compartiment (verbatim), niet volledig gemodelleerd.
- **D3 — objectpool-indeling**: alle IMOW-objecten in één `OwObjecten`-blok
  met thematische sub-secties (regels / normen / activiteiten / locaties /
  gebiedsaanwijzingen / vrijetekst / kaarten), of losse top-level blokken?
  Advies: één `OwObjecten` met thematische sub-secties.
- **D4 — geometrie**: pakketvorm `storm.xml` + `gio/` behouden (Locatie →
  GeometrieRef → GML), conform v0.2? Advies: ja.
