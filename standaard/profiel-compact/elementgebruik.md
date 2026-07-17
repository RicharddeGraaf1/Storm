# Elementgebruik IMOP-tekst — onderbouwing profiel compact

*Meting 2026-07-17 op de OCD-dev-DB: 1.939 vigerende regelingen van ~50
overheden (830k tekst-elementen, 499k inhoud-fragmenten ruwe STOP-XML).
Volledige analyse met methode en kanttekeningen in het kennismodel-vault:
`analysis/Elementgebruik IMOP-tekst in de praktijk (OCD-data).md`.*

## Richting: één standaard, compact als profiel

Geen tweede XSD (profiel-drift), maar het TPOD-patroon: **STORM-compact is
een restrictieprofiel op STORM** — een normatieve elementen-deellijst plus
een validator. Elk compact-document is automatisch een geldig STORM-document.

## Spreiding over 1.937 regelingen (inline-laag)

**Besluit gebruiker 2026-07-17: de knip ligt hard op 10% spreiding** —
elementen daaronder zitten niet in compact; voor documenten die ze
gebruiken bestaat de conversie `complete2compact` (zie onder).

| Band | Elementen | Profiel |
|---|---|---|
| ≥50% | Al, Begrip/Term/Definitie/Begrippenlijst, Lijst/Li/LiNummer, i, IntRef | **compact** (kern) |
| 10–50% | sup, ExtIoRef, br, **CALS-tabellen** (table/tgroup/tbody/colspec/row/entry/thead/title — 43,9%), strong, IntIoRef, Figuur/Illustratie, ExtRef, b, sub, Titel (figuur-titel), Bijschrift, Noot/NootNummer, Bron | **compact** |
| 1–10% | Tussenkop (7,0%), Aanhef (6,8%), Kadertekst (5,7%), Kop/Opschrift-inline (4,6%), Groep (4,1%), Lijstsluiting (3,0%) | **alleen complete** |
| <1% | InleidendeTekst, Lijstaanhef, Contact, InlineTekstAfbeelding, besluit-elementen (Considerans/Afkondiging/Sluiting/Slotformulering/Ondertekening/Dagtekening), Nootref, abbr | **alleen complete** |

De compact-set (~33 elementen + structuurlaag) dekt **±99,5% van alle
element-instanties** in het corpus.

Structuurlaag: alles in compact behalve **Titel** (structuurelement, 1,4%)
en **Subsubparagraaf** (1,2%) — de conversie hernoemt ze naar het
dichtstbijzijnde compact-equivalent (Hoofdstuk resp. Subparagraaf).

## De conversie complete → compact

Machineleesbaar profiel in `src/storm/profielen.py`
(`COMPACT_TEKST_ELEMENTEN` + `controleer_compact`); degradatieregels in
`src/storm/compact.py`; CLI: `storm complete2compact`. Invariant:
**tekstbehoud** — de genormaliseerde tekstinhoud verandert niet.

**Massabewijs (2026-07-17)**: alle 13.835 vigerende fragmenten met
sub-10%-elementen gedegradeerd → **99,94% compact-conform én XSD-geldig,
0 conversiefouten, 0 tekstveranderingen** (8 rest = bron-afwijkingen die
vóór conversie ook al ongeldig waren).

## Kanttekeningen

- Corpus-bias: ~50 overheden, slechts 6 AMvB's + 1 MR — rijke
  rijks-elementen (`Formule`) ontbreken in de data maar niet in de
  standaard. Frequentie is input, geen automatische knip.
- De besluit-elementen in de staart (alleen rijk/N2000) zijn eerder een
  datakwaliteits-signaal (besluitdelen in regelingtekst) dan een
  profiel-vraag.

## XSD-backlog die hieruit volgde

1. ~~CALS-tabellen~~ ✅ **v0.3** (incl. title/Bron, alle praktijk-attrs)
2. ~~Opmaak i/strong/b/u~~ ✅ **v0.3** (nestbaar; sup/sub ook)
3. ~~Titel, Noot + NootNummer + Nootref, Bron~~ ✅ **v0.3**
   (+ Subsubparagraaf, Illustratie@alt, vreemde-ns-attributen)
4. ~~Complete-vocabulaire: alle sub-10%-elementen~~ ✅ **v0.4**
   (Tussenkop, Kadertekst, Groep, Lijstaanhef/-sluiting, InleidendeTekst,
   Aanhef/Sluiting-familie, Contact, InlineTekstAfbeelding, abbr)

**Validatie v0.4 (2026-07-17)**: het complete-vocabulaire dekt nu **alle
499.000** vigerende inhoud-fragmenten; 99,98% valideert (124
bron-afwijkingen resteren, o.a. Begrippenlijst gevuld met lijst-items).
Regressie-fixtures: `tests/fixtures/praktijk/` (compact-laag) en
`tests/fixtures/staart/` (degradatie).


