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
Omdat we een verliesvrije **mirror** willen (renvooi vergelijkt op wId), is
`uId = de wId **letterlijk**` — geen reconstructie, niets eraf. Import neemt over
wat in de data staat; een kale guid zou niet volstaan omdat de historische
positie in een gemuteerde wId niet uit `guid + huidige eId` te reconstrueren is.
De uId kan óók op elementen zitten die STOP niet identificeert (Conditie, entry,
tr).

## Regel

- **integrated** draagt op elk element een `uId`. Op de identificeerbare
  elementen staat daarnaast `eId` (het huidige structuurpad); `wId` komt in
  integrated niet voor.
- **`uId ↔ wId`** is een **identiteit** in de transformatie van/naar de STOP-vorm:
  - **naar STOP**: `wId = uId` — behalve op de elementen zonder eId (`entry`,
    `row`, `Conditie`, `Alinea`): die krijgen géén wId. Regel: **een element
    krijgt een wId dan-en-slechts-dan als het een eId heeft** (samen uit agAKN).
  - **uit STOP**: `uId = wId`.

Zo is de heen-en-weer **byte-exact** by construction: `wId → uId → wId` is de
identiteit, óók voor gemuteerde documenten waar de wId-positie van de huidige
eId afwijkt.

## uId-waarden

- Uit een **geïmporteerde** regeling: de bron-wId zelf, letterlijk (bv.
  `gm0297_1__chp_1`, of in productie `{bg}_{guid}__{historisch-pad}`).
- Bij **authoring** (nieuw element): de plansoftware maakt een wId met een verse
  **GUID**: `{bg}_{guid}__{eId}`. Alleen dán zit er een GUID in de uId; bij
  import hanteren we simpelweg wat er in de data zit.

## Elementen zonder eId/wId (uId-only)

`Alinea`, `Rij`/`row`, `Cel`/`entry`, `Conditie`. Zie voor de STOP-onderbouwing
de kennisbank: *eId en wId van tekstelementen in tabellen* + `imop-tekst.xsd`
(`agAlgemeen` vs `agAKN`). `Figuur` is **wél** identificeerbaar in STOP (agAKN) —
die krijgt dus gewoon `uId → wId`, geen uitzondering.
