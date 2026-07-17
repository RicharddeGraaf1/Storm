#!/usr/bin/env python3
"""Valideer alle voorbeeldpakketten tegen het STORM-schema.

Zelfstandig hulpje voor de standaard-repo: heeft alleen lxml nodig, niet de
transformatie-tooling (die leeft in de repo Storm-services). Draai vanuit de
repo-root:

    python tools/valideer.py

Exitcode 0 = alles geldig; 1 = minstens één voorbeeld faalt.
"""
from __future__ import annotations

import sys
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
XSD = ROOT / "standaard" / "xsd" / "storm.xsd"
VOORBEELDEN = sorted((ROOT / "standaard" / "voorbeelden").glob("*/storm.xml"))


def main() -> int:
    schema = etree.XMLSchema(etree.parse(str(XSD)))
    fout = False
    for pad in VOORBEELDEN:
        doc = etree.parse(str(pad))
        naam = pad.parent.name
        if schema.validate(doc):
            print(f"OK   {naam}")
        else:
            fout = True
            print(f"FOUT {naam}")
            for f in schema.error_log:
                print(f"     regel {f.line}: {f.message}")
    if not VOORBEELDEN:
        print("Geen voorbeelden gevonden.", file=sys.stderr)
        return 1
    return 1 if fout else 0


if __name__ == "__main__":
    raise SystemExit(main())
