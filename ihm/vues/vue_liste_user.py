"""F3 : tickets créés, assignés et brouillons d'un utilisateur (ébauche, étape I7)."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from ihm.vues.fenetre_base import FenetreBase

if TYPE_CHECKING:
    from ihm.controleurs.controleur_user import ControleurUser


class VueListeUser(FenetreBase):
    """Ébauche de F3 ; le constructeur est définitif."""

    def __init__(self, parent: tk.Misc, controleur: ControleurUser) -> None:
        super().__init__(
            parent, f"Gestion des tickets — {controleur.user.name} (User)",
            [controleur.principal.systeme],
        )
        self._controleur: ControleurUser = controleur
        ttk.Label(self, text="Fenêtre en construction : F3 Mes tickets").pack(padx=40, pady=40)
