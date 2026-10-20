"""F4 : titre et priorité d'un nouveau ticket (ébauche, remplie à l'étape I3)."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from ihm.vues.fenetre_base import FenetreBase

if TYPE_CHECKING:
    from acteurs.user import User
    from ihm.controleurs.controleur_principal import ControleurPrincipal


class VueNouveauTicket(FenetreBase):
    """Ébauche de F4 ; le constructeur est définitif."""

    def __init__(self, parent: tk.Misc, principal: ControleurPrincipal, user: User) -> None:
        super().__init__(parent, "Gestion des tickets — Nouveau ticket", [])
        self._principal: ControleurPrincipal = principal
        self._user: User = user
        ttk.Label(self, text="Fenêtre en construction : F4 Nouveau ticket").pack(padx=40, pady=40)
