"""Contrôleur de la liste Admin (F2) : sans tkinter, testable sans écran."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from acteurs.admin import Admin
    from acteurs.user import User
    from ihm.controleurs.controleur_principal import ControleurPrincipal
    from modele.enums import Statut
    from modele.ticket import Ticket
    from sessions.lot_admin import LotAdmin


class ControleurAdmin:
    """Ébauche : constructeur et propriétés définitifs, méthodes remplies à l'étape I5."""

    def __init__(self, principal: ControleurPrincipal, admin: Admin) -> None:
        self._principal: ControleurPrincipal = principal
        self._admin: Admin = admin

    @property
    def principal(self) -> ControleurPrincipal:
        return self._principal

    @property
    def admin(self) -> Admin:
        return self._admin

    def tickets(self, statut: Statut | None = None) -> list[Ticket]:
        raise NotImplementedError("ControleurAdmin.tickets : étape I5")

    def actionsPossibles(self, tickets: list[Ticket]) -> dict[str, bool]:
        raise NotImplementedError("ControleurAdmin.actionsPossibles : étape I5")

    def preparerLot(
        self, action: str, tickets: list[Ticket], user: User | None = None
    ) -> LotAdmin:
        raise NotImplementedError("ControleurAdmin.preparerLot : étape I5")

    def appliquerLot(self, lot: LotAdmin) -> None:
        raise NotImplementedError("ControleurAdmin.appliquerLot : étape I5")
