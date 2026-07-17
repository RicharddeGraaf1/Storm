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
storm download2storm <bronmap> <doel.xml> [--imtr <map-met-dmn-of-zips>]

# STORM-pakket -> STOP-tekst + IMOW-deelbestanden + STTR-DMN's
storm storm2download <storm.xml> <doelmap>

# STORM-pakket -> LVBB-aanleverpakket (besluit, GIO's+wrappers, OW,
# manifesten; hashes worden herberekend) [--zip]
storm storm2bhkv <storm.xml> <doelmap>

# STORM-pakket -> KV-TR-aanlever-ZIPs (manifest+opdracht+DMN per bestand)
storm storm2imtr <storm.xml> <doelmap>

# STORM-complete -> profiel compact (tekstbehoud)
storm complete2compact <storm.xml> <doel.xml>

# verliesvrijheid bewijzen
storm rondreis <bronmap> <doelmap> [--imtr <map>]

pytest            # mini-voorbeeld + externe corpora (skipt wat ontbreekt)
```

Alle documenten dragen een `xsi:schemaLocation` naar het online schema
(raw GitHub), zodat ze in bv. Oxygen direct valideren.

## Stand (2026-07-17)

- Standaard **v0.4.0**: STORM-pakket = `storm.xml` + `gio/*.gml`; inline
  annotaties; regel-locatie gedestilleerd uit IntIoRefs; normen als
  exportregels afgeleid uit de GIO-GML; DMN-beslislogica verbatim ingebed.
- **Complete + compact**: één vocabulaire (dekt álle 499k vigerende
  praktijk-fragmenten, 99,98% geldig) + restrictieprofiel compact
  (knip = 10% spreiding) met conversie `storm complete2compact`
  (tekstbehoud bewezen op 13.835 fragmenten — zie
  `standaard/profiel-compact/`).
- **Aanleverlaag (fase 1)**: `storm2bhkv` reconstrueert het complete
  LVBB-aanleverpakket (besluit envelop-verliesvrij via het
  `Envelop`-compartiment, GIO's byte-verbatim, wrapper-hashes
  herberekend, manifesten gegenereerd); `storm2imtr` levert
  KV-TR-ZIPs. Beide richtingen in tests bewezen op de
  Gemeentestad-aanlevering.
- Transformaties `download2storm`/`storm2download` werkend en verliesvrij
  bewezen op vier corpora (omgevingsplan regelstructuur, consolidatie-
  fallback, omgevingsvisie vrijetekst, 9 echte STTR-bestanden).
- Fase 1 (gepland): aparte bhkv/imtr-adapters met ZIP/manifest-laag.
- Fase 2–4 (gepland): diffkern → STOP-renvooi, OW-diff, GIO-renvooi,
  samenloop-detectie.

Herkomst: uitwerking van "20211119 - mening toekomst standaard.pptx"
(werktitel *Rutopie*); eerste iteraties in `schemaTestsRichard/storm`.
