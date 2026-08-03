# Gemeentestad — storm-integrated

Gegenereerd uit `../Gemeentestad-compact` met de transformatie
`compact → integrated` (`Storm-services/python/compact_integrated.py`).
Valideert tegen `../../xsd/storm-integrated.xsd`.

Dit is de **structuur-hervorming** (zelfde vocabulaire, andere vorm — zie het
variantenprincipe in `../../specificatie/varianten.md`):

- **Annotatie gevouwen**: de losse `Regeltekst`/`JuridischeRegel`-objecten (met
  `artikelOfLid`-ref) zijn samengevouwen tot `owRegeltekstIdentificatie` +
  `owJuridischeRegelIdentificatie` + `ActiviteitAanduiding` + `Thema` **op het
  `Artikel`/`Lid`**. n:1 → 1:1: bij meerdere regels per regeltekst wint de eerste.
- **Tekst hervormd**: STOP-tekst → `ContentBlok`/`TekstRun`+`Mark`
  (`Al` → `Alinea`, `Lijst` → `Lijst`/`Item`, `table` → `Tabel`,
  `Begrippenlijst` → `Begrippenlijst`); inline `IntRef`/`sup`/… → `Mark`s;
  `Kop`-child-elementen → attributen (`label`/`nummer`) + `Opschrift`-runs.
- **Pools**: `Activiteit`/`Omgevingsnorm`/`Gebiedsaanwijzing`/… van
  child-elementen → integrated-attributen; locaties als `locatieRef`-strings;
  geometrie als `Bestand`.

Deze variant is 1-op-1 op `SimplicIT.Domain.Project` en gaat via
`integrated_json.py` verliesvrij naar/uit de Project-wire-JSON. Daarmee is de
keten **`download → volledig → compact → integrated → JSON`** rond.
