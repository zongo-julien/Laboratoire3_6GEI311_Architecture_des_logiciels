"""F5 : éditeur de la description d'un ticket (ébauche, remplie à l'étape I3)."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from ihm.vues.fenetre_base import FenetreBase

if TYPE_CHECKING:
    from ihm.controleurs.controleur_edition import ControleurEdition


class VueEdition(FenetreBase):
    """Ébauche de F5 ; le constructeur est définitif."""

    def __init__(self, parent: tk.Misc, controleur: ControleurEdition) -> None:
        super().__init__(
            parent, f"Gestion des tickets — Ticket #{controleur.session.ticket.ticketID}", []
        )
        self._controleur: ControleurEdition = controleur
        ttk.Label(self, text="Fenêtre en construction : F5 Éditeur de description").pack(
            padx=40, pady=40
        )
