"""F2 : liste de tous les tickets pour l'Admin (ébauche, remplie à l'étape I5)."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from ihm.vues.fenetre_base import FenetreBase

if TYPE_CHECKING:
    from ihm.controleurs.controleur_admin import ControleurAdmin


class VueListeAdmin(FenetreBase):
    """Ébauche de F2 ; le constructeur est définitif."""

    def __init__(self, parent: tk.Misc, controleur: ControleurAdmin) -> None:
        super().__init__(
            parent, f"Gestion des tickets — {controleur.admin.name} (Admin)",
            [controleur.principal.systeme],
        )
        self._controleur: ControleurAdmin = controleur
        ttk.Label(self, text="Fenêtre en construction : F2 Liste Admin").pack(padx=40, pady=40)
