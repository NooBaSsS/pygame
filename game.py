"""модуль игры."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import App

import pygame as pg

from player import Player


class Game:
    """Игра."""

    def __init__(self, app: App) -> None:
        """Игра."""
        self.screen = app.screen
        self.width, self.height = self.screen.get_size()
        self.sprites = pg.sprite.Group()
        self.player = Player(
            self.sprites,
            (
                self.width // 2,
                self.height // 2,
            ),
        )

    def handle_events(self, events: list[pg.event.Event]) -> None:
        """реакция на события."""
        self.player.handle_events(events)

    def update(self) -> None:
        """обновление."""
        self.sprites.update()

    def render(screen: pg.surface):
        """отрисовка группы спрайтов на экране."""
        self.sprites.draw(screen)
