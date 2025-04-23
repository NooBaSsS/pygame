from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

import pygame as pg


class Player(pg.sprite.Sprite):
    """игрок"""

    def __init__(self, game: Game) -> None:
        """конструктор игрока"""
        super().__init__()
        self.game = game
        self.color = (255, 0, 0)
        self.image = pg.surface.Surface((100, 100))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)
        self.game.sprites.add(self)

    def update(self) -> None:
        """обновление логики"""
