"""F8 : rapport d'exécution d'une session ou d'un lot (ébauche, remplie à l'étape I6)."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from ihm.vues.fenetre_base import FenetreBase

if TYPE_CHECKING:
    from sessions.rapport_execution import RapportExecution


class VueRapport(FenetreBase):
    """Ébauche de F8 ; le constructeur est définitif."""

    def __init__(self, parent: tk.Misc, rapport: RapportExecution, libelle: str) -> None:
        super().__init__(parent, f"Gestion des tickets — Rapport : {libelle}", [])
        self._rapport: RapportExecution = rapport
        self._libelle: str = libelle
        ttk.Label(self, text="Fenêtre en construction : F8 Rapport d'exécution").pack(
            padx=40, pady=40
        )
