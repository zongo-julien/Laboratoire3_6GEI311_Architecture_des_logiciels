"""Contrôleur de l'éditeur de description (F5) : sans tkinter, testable sans écran."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ihm.controleurs.controleur_principal import ControleurPrincipal
    from sessions.session_edition import SessionEdition


class ControleurEdition:
    """Un seul par session (registre du ControleurPrincipal) : survit à la fermeture de F5.

    Constructeur, session, estCreation et texteBrouillon sont définitifs ;
    les autres méthodes sont remplies à l'étape I3.
    """

    def __init__(self, principal: ControleurPrincipal, session: SessionEdition) -> None:
        self._principal: ControleurPrincipal = principal
        self._session: SessionEdition = session
        # Calculé une seule fois : après appliquer(), le ticket entre dans le dépôt
        # et le test basculerait.
        self._estCreation: bool = not principal.systeme.contient(session.ticket)
        self._texteBrouillon: str = ""

    @property
    def session(self) -> SessionEdition:
        return self._session

    @property
    def estCreation(self) -> bool:
        """Vrai pour une session de création : son ticket était hors du dépôt."""
        return self._estCreation

    @property
    def texteBrouillon(self) -> str:
        """Texte tapé dans F5, gardé pendant la pause."""
        return self._texteBrouillon

    def ajouterImages(self, chemins: list[str]) -> list[str]:
        raise NotImplementedError("ControleurEdition.ajouterImages : étape I3")

    def commenter(self, texte: str) -> None:
        raise NotImplementedError("ControleurEdition.commenter : étape I3")

    def annulerDerniere(self) -> str:
        raise NotImplementedError("ControleurEdition.annulerDerniere : étape I3")

    def mettreEnPause(self, texte: str) -> None:
        raise NotImplementedError("ControleurEdition.mettreEnPause : étape I3")

    def abandonner(self) -> None:
        raise NotImplementedError("ControleurEdition.abandonner : étape I3")

    def appliquer(self, texte: str) -> None:
        raise NotImplementedError("ControleurEdition.appliquer : étape I3")
