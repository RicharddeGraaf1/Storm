"""Alle voorbeeldpakketten in standaard/voorbeelden valideren tegen het
schema en dragen de online xsi:schemaLocation (Oxygen-valideerbaar)."""

import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from storm.rondreis import valideer
from storm.storm_common import STORM, STORM_XSD_URL, XSI

VOORBEELDEN = sorted(
    (Path(__file__).resolve().parents[1] / "standaard" / "voorbeelden")
    .glob("*/storm.xml"))


@pytest.mark.parametrize("pad", VOORBEELDEN, ids=lambda p: p.parent.name)
def test_voorbeeld_valideert(pad):
    assert valideer(pad) == []


@pytest.mark.parametrize("pad", VOORBEELDEN, ids=lambda p: p.parent.name)
def test_voorbeeld_heeft_online_schemalocation(pad):
    regeling = ET.parse(pad).getroot()
    locatie = regeling.get(f"{{{XSI}}}schemaLocation")
    assert locatie == f"{STORM} {STORM_XSD_URL}"


def test_er_zijn_voorbeelden():
    assert len(VOORBEELDEN) >= 2  # mini + Gemeentestad
