"""Contrôleur de la liste User (F3) : sans tkinter, testable sans écran."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from acteurs.user import User
    from ihm.controleurs.controleur_principal import ControleurPrincipal
    from modele.ticket import Ticket
    from sessions.session_edition import SessionEdition


class ControleurUser:
    """Ébauche : constructeur et propriétés définitifs, méthodes remplies à l'étape I7."""

    def __init__(self, principal: ControleurPrincipal, user: User) -> None:
        self._principal: ControleurPrincipal = principal
        self._user: User = user

    @property
    def principal(self) -> ControleurPrincipal:
        return self._principal

    @property
    def user(self) -> User:
        return self._user

    def ticketsCrees(self) -> list[Ticket]:
        raise NotImplementedError("ControleurUser.ticketsCrees : étape I7")

    def ticketsAssignes(self) -> list[Ticket]:
        raise NotImplementedError("ControleurUser.ticketsAssignes : étape I7")

    def brouillons(self) -> list[SessionEdition]:
        raise NotImplementedError("ControleurUser.brouillons : étape I7")

    def peutSupprimer(self, ticket: Ticket) -> bool:
        raise NotImplementedError("ControleurUser.peutSupprimer : étape I7")

    def peutSoumettre(self, ticket: Ticket) -> bool:
        raise NotImplementedError("ControleurUser.peutSoumettre : étape I7")

    def supprimer(self, ticket: Ticket) -> None:
        raise NotImplementedError("ControleurUser.supprimer : étape I7")

    def soumettre(self, ticket: Ticket) -> None:
        raise NotImplementedError("ControleurUser.soumettre : étape I7")

    def nouveauTicket(self) -> None:
        raise NotImplementedError("ControleurUser.nouveauTicket : étape I7")

    def editer(self, ticket: Ticket) -> None:
        raise NotImplementedError("ControleurUser.editer : étape I7")
