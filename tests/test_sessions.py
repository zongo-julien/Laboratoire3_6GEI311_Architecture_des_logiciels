from __future__ import annotations

import unittest
from typing import TYPE_CHECKING

from acteurs.user import User
from modele.enums import Priorite
from modele.exceptions import SessionIndisponibleException
from modele.systeme_tickets import SystemeTickets
from modele.ticket import Ticket
from sessions.lot_admin import LotAdmin

if TYPE_CHECKING:
    from modele.enums import Statut
    from sessions.session_edition import SessionEdition


def instantane(ticket: Ticket) -> tuple[Statut, str | None, int, int]:
    """Statut, assigné, nombre de commentaires et d'éléments du ticket."""
    assigne = ticket.assignedUser.name if ticket.assignedUser is not None else None
    return (ticket.status, assigne, len(ticket.comments), ticket.description.nombreElements)


class TestAbandonSession(unittest.TestCase):
    """abandonner() renonce à toute la session d'édition avant application."""

    def setUp(self) -> None:
        systeme = SystemeTickets()
        createur = User(1, "Abdoul Razack", "abdoul.razack@uqac.ca", systeme)
        self._ticket: Ticket = Ticket(1, "Bug de connexion", Priorite.HAUTE)
        createur.createTicket(self._ticket)
        self._session: SessionEdition = createur.ouvrirSessionEdition(self._ticket)

    def testTicketInchangeApresAbandon(self) -> None:
        avant = instantane(self._ticket)
        self._session.ajouterCommentaire("Le bug se reproduit sur Chrome.")
        self._session.ajouterTexteSaisi("Étapes pour reproduire le bug.")
        self.assertTrue(self._session.estOuverte)
        self._session.abandonner()
        self.assertEqual(instantane(self._ticket), avant)
        self.assertEqual(self._session.modificationsEnAttente, [])
        self.assertFalse(self._session.estOuverte)

    def testAbandonPossibleEnPause(self) -> None:
        self._session.ajouterCommentaire("Commentaire en attente")
        self._session.mettreEnPause()
        self._session.abandonner()
        self.assertFalse(self._session.estEnPause)
        self.assertFalse(self._session.estOuverte)
        self.assertEqual(self._session.modificationsEnAttente, [])

    def testOperationsRefuseesApresAbandon(self) -> None:
        self._session.abandonner()
        for operation, action in (
            ("ajout", lambda: self._session.ajouterCommentaire("Ajout après abandon")),
            ("ajout", lambda: self._session.ajouterTexteSaisi("Texte après abandon")),
            ("annulation", self._session.annulerDerniere),
            ("mise en pause", self._session.mettreEnPause),
            ("reprise", self._session.reprendre),
            ("application", self._session.appliquer),
        ):
            with self.subTest(operation=operation):
                with self.assertRaises(SessionIndisponibleException) as contexte:
                    action()
                self.assertEqual(
                    str(contexte.exception),
                    f"Session d'édition abandonnée : {operation} impossible",
                )

    def testAbandonRefuseApresAppliquer(self) -> None:
        self._session.ajouterCommentaire("Commentaire appliqué")
        self._session.appliquer()
        self.assertFalse(self._session.estOuverte)
        with self.assertRaises(SessionIndisponibleException):
            self._session.abandonner()
        self.assertEqual(len(self._ticket.comments), 1)

    def testAbandonRefuseEnDouble(self) -> None:
        self._session.abandonner()
        with self.assertRaises(SessionIndisponibleException):
            self._session.abandonner()

    def testLotAdminSansAbandonner(self) -> None:
        self.assertFalse(hasattr(LotAdmin, "abandonner"))
