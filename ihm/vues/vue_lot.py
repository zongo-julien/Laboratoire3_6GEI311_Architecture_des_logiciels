"""F7 : confirmation d'un lot d'opérations de l'Admin (ébauche, remplie à l'étape I6)."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from ihm.vues.fenetre_base import FenetreBase

if TYPE_CHECKING:
    from ihm.controleurs.controleur_admin import ControleurAdmin
    from modele.ticket import Ticket


class VueLot(FenetreBase):
    """Ébauche de F7 ; le constructeur est définitif."""

    def __init__(
        self, parent: tk.Misc, controleur: ControleurAdmin, action: str, tickets: list[Ticket]
    ) -> None:
        super().__init__(
            parent, "Gestion des tickets — Confirmation du lot", [controleur.principal.systeme]
        )
        self._controleur: ControleurAdmin = controleur
        self._action: str = action
        self._tickets: list[Ticket] = list(tickets)
        ttk.Label(self, text="Fenêtre en construction : F7 Confirmation du lot").pack(
            padx=40, pady=40
        )
