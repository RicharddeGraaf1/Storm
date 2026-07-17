"""Externe testcorpora: paden op deze machine, netjes skippen als afwezig.

De grote corpora leven bewust buiten deze repo (Gemeentestad-oefenrepo,
vault raw/); alleen het mini-voorbeeld in standaard/voorbeelden reist mee.
Overschrijfbaar via de omgevingsvariabelen STORM_CORPUS_<NAAM>.
"""

import os
from pathlib import Path

_VAULT_RAW = Path(r"C:\GIT\OmgevingswetKnowledgeBase\vault_v1\raw")

CORPORA = {
    "gemeentestad_opdracht": Path(
        os.environ.get("STORM_CORPUS_GEMEENTESTAD",
                       r"C:\Testbestanden\GITHub\Gemeentestad\opdracht")),
    "consolidatie": Path(os.environ.get(
        "STORM_CORPUS_CONSOLIDATIE",
        _VAULT_RAW / "voorbeeldbestanden-stoptpod" / "Gemeentestad"
        / "Consolidatiebestanden" / "consolidatie")),
    "leiden": Path(os.environ.get(
        "STORM_CORPUS_LEIDEN",
        _VAULT_RAW / "voorbeeldbestanden-stoptpod" / "xml_omgevingsvisie_Leiden"
        / "intrekkenVervangen")),
    "imtr_dordrecht": Path(os.environ.get(
        "STORM_CORPUS_IMTR", _VAULT_RAW / "voorbeeldbestanden-imtr")),
    "imtr_sttr3": Path(os.environ.get(
        "STORM_CORPUS_STTR3",
        _VAULT_RAW / "voorbeeldbestanden-imtr" / "Voorbeeldbestanden STTR 3.0.0")),
}

MINI = Path(__file__).resolve().parents[1] / "standaard" / "voorbeelden" / "mini"
