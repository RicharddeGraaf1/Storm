# Id-schema: uId in integrated, wId in de STOP-vorm

**Status:** ontwerp (2026-08-07). Keuze: **mirror** (byte-verliesvrij), zodat
renvooi (versie-vergelijking op wId) blijft kloppen.

## Waarom

STOP identificeert tekstelementen met een paar `eId`/`wId` (attributeGroup
`agAKN`, beide required). `wId` is de stabiele work-id, opgebouwd als
**`{bg-code}_{work-id}`**, waarbij `work-id` voor een nieuw element `{guid}__{eId}`
is — maar in een **gemuteerd** document de **historische** positie vasthoudt,
die kan afwijken van de huidige `eId` (`eId` is de huidige expressie-positie).
Niet elk element is identificeerbaar: `entry` (Cel), `row` (Rij), `Conditie` en
`Alinea` gebruiken `agAlgemeen` en dragen **geen** eId/wId.

`storm-integrated` is de authoring-vorm en gebruikt daar één **`uId`** voor.
Omdat we een verliesvrije **mirror** willen (renvooi vergelijkt op wId), draagt
de uId de **work-positie mee**: `uId = wId zonder de redundante `{bg-code}_`-
prefix`. Een kale guid zou niet volstaan — de historische positie in een
gemuteerde wId is niet uit `guid + huidige eId` te reconstrueren. De uId kan
óók op elementen zitten die STOP niet identificeert (Conditie, entry, tr).

## Regel

- **integrated** draagt op elk element een `uId`. Op de identificeerbare
  elementen staat daarnaast `eId` (het huidige structuurpad); `wId` komt in
  integrated niet voor.
- **`uId ↔ wId`** in de transformatie van/naar de STOP-vorm (compact/volledig):
  - **naar STOP**: `wId = {bg-code}_{uId}` — behalve op de elementen zonder eId
    (`entry`, `row`, `Conditie`, `Alinea`): die krijgen géén wId. Regel: **een
    element krijgt een wId dan-en-slechts-dan als het een eId heeft** (samen uit
    agAKN). Niet-geprefixte top-level ids (`body`, `longTitle`, toelichting-
    `artrecital…`) hebben `uId == eId` → `wId == uId` (geen prefix).
  - **uit STOP**: `uId` = de wId met de `{bg-code}_`-prefix gestript (of de wId
    zelf als die niet geprefixt is).
- **bg-code** komt uit `Regeling@bevoegdGezagCode`.

Zo is de heen-en-weer **byte-exact**: `wId → uId → wId` reproduceert de originele
wId precies, óók voor gemuteerde documenten waar de wId-positie van de huidige
eId afwijkt.

## uId-waarden

- Uit een **geïmporteerde** regeling: de bron-wId minus bg-prefix — dus incl.
  de (evt. historische) work-positie. In Gemeentestad `1__chp_1`; in productie
  `{guid}__{historisch-pad}`.
- Bij **authoring** (nieuw element): een verse GUID plus de huidige eId
  (`{guid}__{eId}`), zodat de wId `{bg}_{guid}__{eId}` ontstaat.

## Elementen zonder eId/wId (uId-only)

`Alinea`, `Rij`/`row`, `Cel`/`entry`, `Conditie`. Zie voor de STOP-onderbouwing
de kennisbank: *eId en wId van tekstelementen in tabellen* + `imop-tekst.xsd`
(`agAlgemeen` vs `agAKN`). `Figuur` is **wél** identificeerbaar in STOP (agAKN) —
die krijgt dus gewoon `uId → wId`, geen uitzondering.
