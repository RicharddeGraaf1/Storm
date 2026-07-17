# STORM — STandaard Omgevingswet ReferentieModel

Eén standaard (één namespace, één XSD) die STOP-tekst, IMOW-annotaties en
IMTR-toepasbare-regels in samenhang beschrijft — plus de transformaties
van en naar de bestaande DSO-formaten en (in aanbouw) een renvooiservice.

Architectuur en fasering: [ARCHITECTUUR.md](ARCHITECTUUR.md).
De standaard zelf: [standaard/](standaard/) (XSD v0.2.0, specificatie,
mini-voorbeeldpakket).

## Quickstart

```powershell
pip install -e .[test]

# LVBB-uitlevering of BHKV-aanlevering -> STORM-pakket
storm download2storm <bronmap> <doel.xml> [--imtr <map-met-dmn>]

# STORM-pakket -> STOP-tekst + IMOW-deelbestanden + STTR-DMN's
storm storm2download <storm.xml> <doelmap>

# verliesvrijheid bewijzen
storm rondreis <bronmap> <doelmap> [--imtr <map>]

pytest            # mini-voorbeeld + externe corpora (skipt wat ontbreekt)
```

## Stand (2026-07-17)

- Standaard **v0.4.0**: STORM-pakket = `storm.xml` + `gio/*.gml`; inline
  annotaties; regel-locatie gedestilleerd uit IntIoRefs; normen als
  exportregels afgeleid uit de GIO-GML; DMN-beslislogica verbatim ingebed.
- **Complete + compact**: één vocabulaire (dekt álle 499k vigerende
  praktijk-fragmenten, 99,98% geldig) + restrictieprofiel compact
  (knip = 10% spreiding) met conversie `storm complete2compact`
  (tekstbehoud bewezen op 13.835 fragmenten — zie
  `standaard/profiel-compact/`).
- Transformaties `download2storm`/`storm2download` werkend en verliesvrij
  bewezen op vier corpora (omgevingsplan regelstructuur, consolidatie-
  fallback, omgevingsvisie vrijetekst, 9 echte STTR-bestanden).
- Fase 1 (gepland): aparte bhkv/imtr-adapters met ZIP/manifest-laag.
- Fase 2–4 (gepland): diffkern → STOP-renvooi, OW-diff, GIO-renvooi,
  samenloop-detectie.

Herkomst: uitwerking van "20211119 - mening toekomst standaard.pptx"
(werktitel *Rutopie*); eerste iteraties in `schemaTestsRichard/storm`.
