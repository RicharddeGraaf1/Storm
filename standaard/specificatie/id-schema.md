# Id-schema: uId in integrated, wId in de STOP-vorm

**Status:** ontwerp (2026-08-07).

## Waarom

STOP identificeert tekstelementen met een paar `eId`/`wId` (attributeGroup
`agAKN`, beide required). `wId` is de stabiele work-id, opgebouwd als
**`{bg-code}_{guid}__{eId}`**; `eId` is het structuurpad (`chp_2__art_2.3`).
Niet elk element is identificeerbaar: `entry` (Cel), `row` (Rij), `Conditie` en
`Alinea` gebruiken `agAlgemeen` en dragen **geen** eId/wId.

`storm-integrated` is de authoring-vorm en gebruikt daar één **`uId`** voor —
de guid uit de wId. Zo hoeft de editor niet met de lange, positie-afhankelijke
wId te werken, en kan een `uId` óók op elementen zitten die STOP niet
identificeert (Conditie, entry, tr).

## Regel

- **integrated** draagt op elk element een `uId` (de guid/workpart). Op de
  identificeerbare elementen staat daarnaast `eId` (het structuurpad); `wId`
  komt in integrated niet voor.
- **`uId ↔ wId`** in de transformatie van/naar de STOP-vorm (compact/volledig):
  - **naar STOP**: `wId = {bg-code}_{uId}__{eId}` — behalve op de elementen
    zonder eId (`entry`, `row`, `Conditie`, `Alinea`): die krijgen géén wId.
    Regel: **een element krijgt een wId dan-en-slechts-dan als het een eId
    heeft** (samen uit agAKN). Top-level ids zonder bg-prefix (`body`,
    `longTitle`, toelichting-`artrecital…`) hebben `uId == eId` → `wId == uId`.
  - **uit STOP**: `uId` = het workpart-deel van de wId — de wId met de bekende
    `eId` van achteren en de `{bg-code}_` van voren gestript. (Niet blind op
    `__` splitsen: eId's bevatten zelf `__`.)
- **bg-code** komt uit `Regeling@bevoegdGezagCode`.

Zo is de heen-en-weer exact: `wId → uId → wId` reproduceert de originele wId
byte-voor-byte (geverifieerd op Gemeentestad: 175/176 structurele wIds; de ene
rest is een losse, al bestaande gap in de `ArtikelsgewijzeToelichting`-wrapper
die zijn eigen id niet meedraagt — los van dit id-schema).

## uId-waarden

- Uit een **geïmporteerde** regeling: het workpart van de bron-wId. In een
  hand-voorbeeld als Gemeentestad is dat één gedeelde sequence (`1`); in
  productie is het een **per-element GUID**.
- Bij **authoring** (nieuw element in de plansoftware): een verse GUID.

## Elementen zonder eId/wId (uId-only)

`Alinea`, `Rij`/`row`, `Cel`/`entry`, `Conditie`. Zie voor de STOP-onderbouwing
de kennisbank: *eId en wId van tekstelementen in tabellen* + `imop-tekst.xsd`
(`agAlgemeen` vs `agAKN`). `Figuur` is **wél** identificeerbaar in STOP (agAKN) —
die krijgt dus gewoon `uId → wId`, geen uitzondering.
