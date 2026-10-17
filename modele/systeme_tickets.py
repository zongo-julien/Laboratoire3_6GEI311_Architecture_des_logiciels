from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from acteurs.user import User
    from modele.ticket import Ticket


class SystemeTickets:
    """Dépôt central des tickets."""

    def __init__(self) -> None:
        self._tickets: list[Ticket] = []

    @property
    def tickets(self) -> list[Ticket]:
        return list(self._tickets)

    def ajouterTicket(self, ticket: Ticket) -> None:
        self._tickets.append(ticket)

    def retirerTicket(self, ticket: Ticket) -> None:
        self._tickets.remove(ticket)

    def contient(self, ticket: Ticket) -> bool:
        return ticket in self._tickets

    def ticketsDe(self, user: User) -> list[Ticket]:
        """Tickets dont l'utilisateur est le créateur."""
        return [ticket for ticket in self._tickets if ticket.creator is user]

    def ticketsAssignesA(self, user: User) -> list[Ticket]:
        """Tickets dont l'utilisateur est l'assigné courant.

        Comprend aussi les tickets TERMINE ou FERME : l'assigné y est conservé
        pour la traçabilité. La vue filtre par statut si nécessaire.
        """
        return [ticket for ticket in self._tickets if ticket.assignedUser is user]
