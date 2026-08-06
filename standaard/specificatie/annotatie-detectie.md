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
Toegestaan). URI-basis:
`http://standaarden.omgevingswet.overheid.nl/regelkwalificatie/id/concept/`.

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
