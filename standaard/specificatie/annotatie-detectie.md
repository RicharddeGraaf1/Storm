# Annotatie-detectie: activiteit en regelkwalificatie uit de regeltekst

**Status:** ontwerp (2026-08-05). Begeleidt de plansoftware-feature
`SimplicIT_OW_plansoftware/docs/plans/activiteit-regelkwalificatie-detectie.md`
(review Thomas gevraagd).

## Waarom dit in de standaard hoort

Een activiteit heeft — anders dan een informatieobject — **geen inline-anker in
STOP**. Een informatieobject wordt in de lopende tekst genoemd met een
`IntIoRef` (zie `reference`-keten), waaruit de koppeling woord → GIO
deterministisch te lezen is. Een activiteit staat nergens in de lopende tekst
gemarkeerd; de koppeling regel → activiteit komt uit de `JuridischeRegel`-
annotatie op regeltekst-niveau.

Om een authoring-tool tóch te helpen bij het leggen van die koppeling — en bij
het bepalen van de **regelkwalificatie** (Verbod, Vergunningplicht, …) — bestaat
een heuristiek: match de activiteitnaam in de tekst, en leid de kwalificatie af
uit signaalwoorden. Omdat die afleiding anders per tool anders uitpakt, legt
STORM de tabel en het gedrag hier vast: **herleidbaar, niet per implementatie
verschillend.**

## De keyword-tabel (regelkwalificatie)

Langste keyword wint (zo gaat "niet toegestaan" naar Verbod, niet naar
Toegestaan). De regelkwalificatie is een IMOW-waardelijst-URI; de autoritatieve
basis is die uit de gepubliceerde omgevingsplannen zelf:
`http://standaarden.omgevingswet.overheid.nl/activiteitregelkwalificatie/id/concept/`
(dus `…/activiteitregelkwalificatie/id/concept/Toegestaan`, `…/Verbod`, enz.).

> **Let op** — de oude frontend-detectie gebruikte een andere basis
> (`…/id/concept/Regelkwalificatie/`) die niet met de DSO-waardelijst
> overeenkomt. Bij de port (zie het plansoftware-plan) de **autoritatieve** URI
> hierboven aanhouden, niet de oude constante.

| regelkwalificatie | signaalwoorden (langste eerst) |
|---|---|
| `Verbod` | niet toegestaan, niet is toegestaan, verboden |
| `Vergunningplicht` | omgevingsvergunning, vergunningplichtig, vergunningplicht, vergunning |
| `Meldingsplicht` | meldingsplichtig, meldingsplicht, melding, melden |
| `Informatieplicht` | informatieplicht, informeren |
| `Gebod` | verplicht, is gehouden, dient te, moet |
| `Toegestaan` | is toegestaan, toelaatbaar, toegestaan, mag |

De activiteit-match zelf is een woordgrens-match (`\b…\b`) van de bekende
activiteitnamen tegen de platte tekst van het artikel/lid, langste-eerst,
gededupliceerd op activiteit-identificatie.

## Herkomst en het suggestie-principe

Detectie **stelt voor**, de gebruiker bevestigt — net zoals de import bij een
informatieobject het expliciete `IntIoRef`-anker leest en de heuristiek alleen
voor nieuw getypte tekst bijspringt. Daarom draagt elke afgeleide annotatie een
herkomst. In `storm-integrated` is dat het optionele `herkomst`-attribuut op
`ActiviteitAanduiding` en `InformatieobjectAanduiding`:

| `herkomst` | betekenis |
|---|---|
| `voorstel` | door detectie gezet, nog niet bevestigd |
| `bevestigd` | door detectie gezet én door de gebruiker bevestigd |
| `handmatig` | door de gebruiker zelf gezet; **afwezig attribuut = handmatig** |

Invariant: herdetectie mag alleen een `voorstel` vervangen. `bevestigd` en
`handmatig` blijven met rust — een handmatige keuze wordt nooit overschreven.

De expliciete `JuridischeRegel`-bron uit een importpakket telt als `bevestigd`
(het is de autoritatieve bron), de heuristiek voegt daarnaast alleen
`voorstel`-aanduidingen toe.

## Doorwerking in de varianten

- **integrated** — draagt `herkomst` op de annotatie (dit document + schema).
- **compact / volledig** — het `herkomst`-attribuut is een authoring-begrip
  (voorstel-vs-bevestigd) dat hoort bij de 1:1-annotatievorm van *integrated*.
  De doorgifte door `compact ↔ integrated` en de detectie zelf horen bij de
  bouwfase van het plansoftware-plan; zolang geen bron `herkomst` levert, blijft
  de bestaande roundtrip verliesvrij (attribuut afwezig).

## Vorm A — waar leeft de waarheid, en de inline-spans

De activiteit-verwijzing vanuit de juridische regel is in DSO een **trio**: de
`ActiviteitLocatieaanduiding` = *activiteit + regelkwalificatie + locatie*
(regelkwalificatie en locatie horen bij elkaar — een activiteit kan op de ene
locatie toegestaan en op de andere vergunningplichtig zijn). Dat trio is de
**waarheid** en staat:

- in **compact** op `activiteitaanduiding`
  (`identificatie` = de ALA-id, `activiteit`, `locatieaanduiding`,
  `regelkwalificatie`), één per ALA;
- in **integrated** op `ActiviteitAanduiding`
  (`identificatie`, `activiteitIdentificatie`, `regelkwalificatie`, `locatieRef`,
  `herkomst`) op het artikel/lid — de naam is resolveerbaar uit de Activiteit-pool.

Dit trio round-trippt **verliesvrij** door `compact ↔ integrated` (op de
inherente n:1→1:1 na — meerdere juridische regels per regeltekst kunnen niet op
één artikel-annotatie).

**Inline-spans (span-ankers).** Anders dan een informatieobject heeft een
activiteit géén inline-anker in STOP. Toch wil de editor het activiteitwoord én
het signaalwoord kunnen markeren. Vorm A doet dat met **twee `Mark`-kinds in
integrated** die alleen een `ref` naar `ActiviteitAanduiding@identificatie`
dragen — géén eigen data:

| `Mark/@kind` | staat op | `@ref` |
|---|---|---|
| `activiteitRef` | de activiteitnaam-span | → `ActiviteitAanduiding@identificatie` |
| `regelkwalificatie` | het signaalwoord ("verboden", "melding", …) | → dezelfde `ActiviteitAanduiding@identificatie` |

Zo is de kwalificatie **niet gedupliceerd** (ze staat op de aanduiding, niet op
de mark) en is de koppeling nooit ambigu, ook niet in een lid met meerdere
activiteiten: beide marks wijzen naar dezelfde aanduiding.

**Round-trip-eigenschap van de span.** De marks zijn inherent niet-STOP, dus ze
overleven `→ compact` niet (compact/STOP heeft geen inline activiteit-anker). De
**data** blijft heel (die staat op de aanduiding); de **span** wordt bij
`compact →` opnieuw geplaatst via naam-/keyword-match (dezelfde detectie als
hierboven). De span is dus best-effort, de data verliesvrij. Voorbeeld:
`voorbeelden/Gemeentestad-integrated`.
