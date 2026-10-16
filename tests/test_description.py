from __future__ import annotations

import unittest
from pathlib import Path

from description.fabrique_description import FabriqueDescription

dossierRessources = Path(__file__).resolve().parent.parent / "ressources"


class TestDescription(unittest.TestCase):
    """Propriétés typeArtefact et contenu des éléments de description."""

    def testTypeArtefactDesTroisTypes(self) -> None:
        for typeArtefact, fichier in (
            ("texte", "description_bug.txt"),
            ("image", "capture_ecran.png"),
            ("video", "demo_bug.mp4"),
        ):
            with self.subTest(typeArtefact=typeArtefact):
                element = FabriqueDescription.creer(typeArtefact, str(dossierRessources / fichier))
                element.traiter()
                self.assertEqual(element.typeArtefact, typeArtefact)

    def testContenuDuTexte(self) -> None:
        chemin = dossierRessources / "description_bug.txt"
        element = FabriqueDescription.creer("texte", str(chemin))
        element.traiter()
        self.assertEqual(element.contenu, chemin.read_text(encoding="utf-8"))
