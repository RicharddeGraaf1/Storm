# STORM-specificatie (concept v0.2.0)

**STORM — STandaard Omgevingswet ReferentieModel**

Eén standaard, één namespace, één XSD die de inhoud van STOP (tekst), IMOW
(annotaties/objecten) en IMTR (toepasbare regels) in samenhang beschrijft.

Deze specificatie is de uitwerking van de ideeën uit
*"20211119 - mening toekomst standaard.pptx"* (werktitel destijds: **Rutopie**).

---

## 1. Ontwerpprincipes

Rechtstreeks overgenomen uit de presentatie, met de slide als bron:

| # | Principe | Bron (slide) |
|---|---|---|
| P1 | Vertrek vanuit het **CIMOW**: de objectgerichte interpretatie van IMOP + IMOW. | 4 |
| P2 | Een regeling bestaat uit **DocumentComponenten**; ieder DocumentComponent is een OP-element. De tekststructuur blijft dus STOP-vormig. | 5 |
| P3 | **Inline annoteren**: annotaties zijn attributen/elementen *op* de tekst-elementen zelf (artikel, lid, divisie, divisietekst), niet een parallel objectenbestand met verwijzingen terug. | 11, 15, 19 |
| P4 | IMOW wordt een **module binnen de standaard** (het "annotaties-deel"), niet een zelfstandig informatiemodel. | 10 |
| P5 | **Gebiedsaanwijzing schuift de GIO in**: type, naam en groep worden optionele velden bij de GIO. | 12, 16 |
| P6 | **Vervallen objecten**: Locatie (altijd herleidbaar tot een GIO-verwijzing), ActiviteitLocatieaanduiding (overlapt met IMTR-uitvoeringsregels), en alle tekst-verwijsobjecten: Regeltekst, JuridischeRegel, Tekstdeel, Divisie, DivisieTekst. | 12 |
| P7 | **Behouden OW-objecten**: Activiteit, Hoofdlijn, Pons, Regelingsgebied, Ambtsgebied — ondergebracht in het metadata-deel van het document. | 11, 18 |
| P8 | **Eenduidige Ow-referenties** in de tekst: `IntOwRef`/`ExtOwRef` als inline elementen. De karakterpositie is impliciet in de tekststructuur zelf — geen mogelijkheid tot meerdere interpretaties. | 11, 23 |
| P9 | **Expliciete cardinaliteiten**: doelgroep/regelType, locatieaanduiding en idealisatie zijn *verplicht* op een regel; thema is *optioneel*; objectspecifieke gegevens zijn "bij gebruik van dit object verplicht" (bgvdov). | 9 |
| P10 | Normen (omgevingsnorm/omgevingswaarde) blijven zoals in de huidige versie: objecten met waarden per locatie; de GIO heeft alle geometrische informatie al. | 17 |

**Doelgroep-notitie bij P9:** de verplichte "doelgroep van de regel"
(iedereen / ander BG / eigen BG) uit slide 6/9 valt in STORM samen met het
verplichte attribuut `regelType`: `regelVoorIedereen` → iedereen,
`instructieregel` → ander BG, `omgevingswaarderegel` → eigen BG.

---

## 2. Documentopbouw

Eén STORM-**pakket** = één regeling(versie): `storm.xml` + de GIO-GML-bestanden
in `gio/`, in één namespace `urn:storm:1.0`:

```xml
<Regeling xmlns="urn:storm:1.0" schemaversie="0.2.0">
  <Identificatie>      <!-- FRBR work/expression, soortWork, versienummer -->
  <Tekst>              <!-- STOP-vormige tekststructuur mét inline annotaties -->
  <OwObjecten>         <!-- P7: Activiteit, Hoofdlijn, Pons, Regelingsgebied -->
  <Geo>                <!-- verwijzingen naar de GML's + gebiedsaanwijzing (P5) -->
  <Exportregels>       <!-- IMOW-export-administratie (v0.2, zie §2.5) -->
  <ToepasbareRegels>   <!-- IMTR-module (zie §6) -->
</Regeling>
```

**v0.2-kernkeuzes** ([[Gebruikersinput#2026-07-15 STORM-ontwerpkeuzes]]):
geometrie en normwaarden leven in de GIO-GML's zelf (geen duplicatie in
storm.xml); de regel-locatie wordt waar mogelijk **gedestilleerd uit de
IntIoRefs in de tekst**; Omgevingsnorm/Normwaarde zijn geen STORM-inhoud
maar worden als **exportregels** gegenereerd bij de transformatie naar IMOW.

### 2.1 Tekst met inline annotaties

De tekststructuur volgt STOP (Lichaam, Hoofdstuk, Afdeling, Paragraaf,
Artikel, Lid, Divisie, Divisietekst, Kop, Inhoud, Al, Lijst, Begrippenlijst,
Bijlage, toelichtingen), maar in de STORM-namespace en verrijkt:

```xml
<Artikel eId="chp_2__art_2.3" wId="gm0297_1__chp_2__subchp_2.2__art_2.3"
         regelType="regelVoorIedereen" idealisatie="exact">
  <Kop>…</Kop>
  <Regel owId="nl.imow-gm0297.juridischeregel.2019000001"
         soort="regelVoorIedereen" idealisatie="exact">
    <Locatieaanduiding>
      <GioRef ref="nl.imow-gm0297.gebiedengroep.Bedrijfcategorie2"/>
    </Locatieaanduiding>
    <ActiviteitToedeling activiteitRef="nl.imow-gm0297.activiteit.2019000241"
                         kwalificatie="…/activiteitregelkwalificatie/id/concept/Toegestaan"
                         owId="nl.imow-gm0297.activiteitlocatieaanduiding.2019000001">
      <Locatieaanduiding><GioRef ref="…"/></Locatieaanduiding>
    </ActiviteitToedeling>
  </Regel>
  <Inhoud>
    <Al>Het is toegestaan om <IntOwRef ref="nl.imow-gm0297.activiteit.2019000241">
    bedrijfstypen van categorie 2 uit te oefenen</IntOwRef> binnen …</Al>
  </Inhoud>
</Artikel>
```

Twee lagen, bewust:

1. **Attributen op Artikel/Lid/Divisietekst** (`regelType`, `idealisatie`,
   `thema`) — dit is de Rutopie-ideaalvorm (slide 11, 15). Ze worden gezet
   wanneer de annotatie eenduidig is voor het hele tekst-element.
2. **`Regel`-kindelementen** — de volledige, verliesvrije drager. Meerdere
   `Regel`-elementen per artikel/lid zijn toegestaan (IMOW staat immers
   meerdere juridische regels per regeltekst toe). Het `owId`-attribuut
   bewaart de oorspronkelijke IMOW-identificatie zodat een conversie
   heen-en-terug bit-voor-bit dezelfde objecten oplevert.

Als een artikel precies één `Regel` heeft, zijn de attributen op het artikel
en die op de `Regel` per definitie gelijk.

### 2.2 Vrijeteksstructuur

Conform slide 7 krijgen `Divisie` en `Divisietekst` de attributen `thema` en
`idealisatie`, en de kindelementen `HoofdlijnRef` (duiding aan een hoofdlijn)
en `Gebiedsaanwijzing` via de GIO (P5).

### 2.3 OwObjecten

| STORM-element | Herkomst (IMOW) | Opmerking |
|---|---|---|
| `Activiteit` | `rol:Activiteit` | naam, groep, bovenliggende/gerelateerde refs |
| `Hoofdlijn` | `vt:Hoofdlijn` | soort + naam |
| `Pons` | `p:Pons` | locatieaanduiding |
| `Regelingsgebied` | `rg:Regelingsgebied` | locatieaanduiding |

`Norm` is in v0.2 **geen** OwObject meer: de GIO draagt naam (`normlabel`),
type (`normID`), eenheid (`eenheidID`) en de waarde per locatie
(`kwantitatieveNormwaarde`) al — slide 17, empirisch bevestigd op de
Gemeentestad-GML's. Zie §2.5.

### 2.4 Geo (v0.2)

De GML-bestanden zíjn de geo-bron; storm.xml verwijst alleen:

```xml
<Gio work="/join/id/regdata/gm0297/2019/Bouwhoogte"
     expressie=".../nld@2019-06-18;3520" bestand="gio/Bouwhoogte.gml"/>
```

| STORM-element | Herkomst | Opmerking |
|---|---|---|
| `Gio` | GIO-GML (STOP imop-geo) | work/expressie + relatief bestandspad; géén geometrie-duplicatie |
| `Gio/Gebiedsaanwijzing` | `ga:Gebiedsaanwijzing` | P5: type/naam/groep als velden bíj de GIO waar de aanwijzing op rustte; `locatieRef` = export-hint |
| `Ambtsgebied` | `l:Ambtsgebied` | bestuurlijke-grenzen-verwijzing (geen GML) |

### 2.5 Exportregels (v0.2)

Transformatie-metadata die de IMOW-export nodig heeft maar die STORM niet
als inhoud beschouwt:

- `ImowLocatie` — de IMOW-identiteiten van Gebied/Gebiedengroep, met hun
  `basisgeoId`/leden en het `gioWork` waarmee ze 1-op-1 corresponderen
  (de drager van de IntIoRef-destillatie).
- `ImowNorm` — het norm-object: alleen `soort` en `groep` (die kent de GIO
  niet) plus de identiteiten; naam/type/eenheid/waarden komen bij export
  **uit de GML** zodra `gioWork` gezet is. `waardeInRegeltekst` en
  kwalitatieve waarden (geen GIO-drager) staan wél expliciet.
- `ImowGebiedsaanwijzing` — fallback voor aanwijzingen zonder herleidbare
  GIO (bv. consolidaties zonder GIO-metadata).

**Locatie-destillatie.** Een `Regel` zonder `Locatieaanduiding` geldt op de
GIO's waar zijn artikel/lid via `IntIoRef → ExtIoRef → work` naar verwijst;
een artikel zonder IntIoRefs geldt op het ambtsgebied. De conversie zet de
expliciete `Locatieaanduiding` alleen waar tekst en regel-locatie afwijken.
Empirie Gemeentestad: 7/21 regels destilleerbaar, 4/21 ambtsgebied-default,
10/21 expliciet (één artikel bevat vaak meerdere regels met elk een eigen
deel-werkingsgebied).

---

## 3. Mapping STOP ↔ STORM

| STOP (imop/tekst) | STORM | Richting |
|---|---|---|
| Alle tekst-elementen (`Lichaam`, `Hoofdstuk`, …, `Al`, `Lijst`, `IntIoRef`, `ExtIoRef`, …) | Zelfde elementnaam in `urn:storm:1.0` | verliesvrij, beide kanten |
| `@eId`, `@wId` | idem | verliesvrij |
| `data:ExpressionIdentificatie` | `Identificatie` | verliesvrij |
| — | `@regelType`, `@idealisatie`, `@thema`, `Regel`, `HoofdlijnRef` | alleen in STORM; worden bij STORM→STOP **gestript** (STOP kent geen inline annotatie) |

`IntIoRef`/`ExtIoRef` (de tweetraps GIO-verwijzing in STOP-tekst) blijven in
v0.1.0 verbatim behouden. De Rutopie-ideaalvorm — direct een `GioRef` inline —
staat op de open-puntenlijst (§7).

## 4. Mapping IMOW ↔ STORM

| IMOW-objecttype | STORM | Toelichting |
|---|---|---|
| `r:Regeltekst` | **vervalt** (P6) | het artikel/lid ís het ankerpunt; `owId` op `Regel` + `wId` op het tekst-element volstaan om het object te reconstrueren |
| `r:RegelVoorIedereen` | `Regel @soort="regelVoorIedereen"` op het artikel/lid | idealisatie → attribuut; artikelOfLid-ref → impliciet (positie in de boom) |
| `r:Instructieregel` | `Regel @soort="instructieregel"` | + optionele `@instrument` / `@taakuitoefening` (bgvdov, slide 9) |
| `r:Omgevingswaarderegel` | `Regel @soort="omgevingswaarderegel"` + `NormRef` | |
| `r:ActiviteitLocatieaanduiding` | `ActiviteitToedeling` binnen `Regel` | kwalificatie + eigen locatie; het zelfstandige object vervalt (P6) |
| `r:locatieaanduiding` / `l:LocatieRef` | gedestilleerd uit IntIoRefs, of expliciete `Locatieaanduiding/GioRef` | v0.2: de tekst is de primaire bron (§2.5) |
| `ga:Gebiedsaanwijzing` | velden op de `Gio` (P5) | de regel houdt een expliciete `GebiedsaanwijzingRef` (owId) zodat de koppeling verliesvrij terugvertaalt |
| `l:Gebied` / `l:Gebiedengroep` | `Exportregels/ImowLocatie` | v0.2: identiteits-administratie; de geometrie zelf leeft in de GML |
| `l:Ambtsgebied` | `Geo/Ambtsgebied` | |
| `rol:Activiteit` | `OwObjecten/Activiteit` | P7 |
| `rol:Omgevingsnorm` / `rol:Omgevingswaarde` | **exportregel** (`Exportregels/ImowNorm`) | v0.2: naam/type/eenheid/waarden komen bij export uit de GIO-GML (slide 17); alleen soort/groep/identiteiten + niet-GIO-waarden staan in STORM |
| `p:Pons`, `rg:Regelingsgebied`, `vt:Hoofdlijn` | `OwObjecten/…` | P7 |
| `vt:Divisie` / `vt:Divisietekst` | **vervallen** (P6) | het tekst-element ís het ankerpunt; `owId` op Divisie(tekst) reconstrueert het object |
| `vt:Tekstdeel` | `Tekstdeel`-element op Divisie(tekst) | analoog aan `Regel`: thema/idealisatie als attribuut, hoofdlijnaanduiding/locatie/gebiedsaanwijzing als kinderen; bij één tekstdeel ook als attributen op het tekst-element zelf |

**Reconstructie-garantie.** Elk STORM-element dat een IMOW-object vervangt
draagt het oorspronkelijke `owId`. De conversie STORM→IMOW genereert daarmee
exact de oorspronkelijke identificaties; voor nieuw (in STORM) geschreven
content genereert de converter deterministische id's uit `bevoegdGezag` +
`wId`.

## 5. Cardinaliteiten (P9, slide 9)

| Gegeven | Cardinaliteit in STORM |
|---|---|
| `Regel@soort` (≙ doelgroep) | **verplicht** |
| `Regel/Locatieaanduiding` | **verplicht-of-destilleerbaar** (v0.2): expliciet alléén als de locatie niet volgt uit de IntIoRefs van het artikel of de ambtsgebied-default (§2.5) |
| `Regel@idealisatie` | **verplicht** |
| `@thema` | optioneel |
| `@instrument`/`@taakuitoefening` (instructieregel) | bgvdov |
| `Gio/Gebiedsaanwijzing` (type, naam, groep) | bgvdov: alle drie verplicht zodra het element gebruikt wordt |
| `Norm` (naam, type), `Normwaarde` (waarde, locatie) | bgvdov |
| `ActiviteitToedeling` (activiteitRef, kwalificatie) | bgvdov |

## 6. IMTR-module

Slide 12 constateert dat `ActiviteitLocatieaanduiding` overlapt met de
uitvoeringsregels uit IMTR. STORM trekt die lijn door: toepasbare regels
horen bij de **Activiteit** en leven in hetzelfde document, onder
`ToepasbareRegels/ToepasbareActiviteit`.

Gebouwd en getoetst op echte STTR-bestanden (Dordrecht-produktie in STTR
v1.0 én de officiële voorbeeldset STTR 3.0.0, beide DMN 1.2 met
STTR-extensienamespaces).

**Ontwerpkeuze — native kern, DMN verbatim.** STTR bestaat uit twee lagen:

1. De **STTR-extensies** (regelgroepen, uitvoeringsregels/vragen,
   geo-verwijzingen, toelichtingen) — die worden **STORM-native**, want dit
   is de laag die aan het kennismodel raakt.
2. De **DMN-beslislogica** (decision tables, information requirements) —
   die blijft **verbatim ingebed** in `Beslislogica`. DMN is al een open
   OMG-standaard; die heruitvinden voegt niets toe.

De native laag is daarmee een *projectie* van de ingebedde DMN: wie de
vragen wijzigt, moet ook de beslislogica bijwerken (bekend hiaat; de
projectie is bedoeld voor bevraging en kennismodel-koppeling, de DMN blijft
de bron voor uitvoering).

**De bruggen naar de rest van STORM** (en dit is de kern van P6):

- `bedr:functioneleStructuurRef` bevat de **IMOW-activiteit-id**
  (`nl.imow-….activiteit.…`) → `ToepasbareActiviteit@activiteitRef` wijst
  direct naar de `Activiteit` in `OwObjecten`. Ook de soort
  (conclusie / indieningsvereisten / maatregelen) wordt eruit afgeleid.
- `uitv:geoVerwijzing/uitv:locatie@identificatie` bevat een
  **IMOW-locatie-id** → `Uitvoeringsregel/GioRef` wijst direct naar de
  `Gio` in `Geo`. De toepasbare regel "weet" dus in STORM native op welke
  kaartlaag hij zijn antwoord haalt.

**Let op**: de `namespace` van een STTR-bestand
(`http://toepasbare-regels.omgevingswet.overheid.nl/<nummer>`) is per
bevoegd gezag, niet per bestand — meerdere toepasbare-regelbestanden delen
hem. Identificatie van een bestand = namespace + naam.

## 7. Open punten

1. **IntIoRef → GioRef**: de tweetraps STOP-verwijzing (IntIoRef → ExtIoRef →
   GIO) platslaan naar een directe inline `GioRef` (Rutopie-ideaal, slide 23).
   v0.2 gebruikt de keten al als bron voor de regel-locatie (§2.5); het
   platslaan van de verwijzing zelf staat nog open.
2. **IMTR native laag is een projectie** (§6): wijzigingen in de vragen
   werken niet automatisch door in de ingebedde DMN. Volgende stap zou een
   consistentie-check zijn (elke uitvoeringsregel-vraag ↔ dmn:inputData).
3. **Mutaties/consolidatie**: STORM v0.1.0 beschrijft één regelingversie.
   Het STOP-mutatiemechanisme (RegelingMutatie, was-wordt) is buiten scope;
   slide 21 signaleert al dat achteraf annoteren spanning geeft met
   inline annotaties.
4. **Symbolisatie** (owSymbolisatieItem/owKaart) — bewust buiten het model
   gehouden; presentatie is geen inhoud.
5. ~~**Tabellen** — nog niet in het XSD~~ — **opgelost in v0.3**: de
   elementanalyse op OCD-data toonde CALS-tabellen in 43,9% van de
   vigerende regelingen; de familie (table/tgroup/colspec/thead/tbody/
   row/entry) zit nu in het schema, massagevalideerd tegen 485k
   praktijk-fragmenten (99,99% geldig). Zie `standaard/CHANGELOG.md`.
6. **Waardelijsten**: STORM verwijst nu naar de bestaande
   `standaarden.omgevingswet.overheid.nl`-URI's; een eigen geïntegreerd
   waardelijstenregister is een logische vervolgstap.
