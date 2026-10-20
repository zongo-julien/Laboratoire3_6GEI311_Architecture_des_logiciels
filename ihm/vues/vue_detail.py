"""F6 : détail d'un ticket (ébauche, remplie à l'étape I8)."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from ihm.vues.fenetre_base import FenetreBase

if TYPE_CHECKING:
    from modele.systeme_tickets import SystemeTickets
    from modele.ticket import Ticket


class VueDetail(FenetreBase):
    """Ébauche de F6 ; le constructeur est définitif."""

    def __init__(
        self, parent: tk.Misc, systeme: SystemeTickets, tickets: list[Ticket], index: int
    ) -> None:
        super().__init__(
            parent, f"Gestion des tickets — Ticket #{tickets[index].ticketID}", [systeme]
        )
        self._systeme: SystemeTickets = systeme
        self._tickets: list[Ticket] = list(tickets)
        self._index: int = index
        ttk.Label(self, text="Fenêtre en construction : F6 Détail d'un ticket").pack(
            padx=40, pady=40
        )
