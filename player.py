from __future__ import annotations

from typing import TYPE_CHECKING

from pygame.display import set_palette
from pygame.event import Event

import pygame as pg

import config


class Player(pg.sprite.Sprite):
    """игрок."""

    def __init__(
        self,
        sprites_group: pg.sprite.Group,
        center_coords: tuple[int, int],
    ) -> None:
        """конструктор игрока."""
        super().__init__()
        self.color = (255, 0, 0)
        self.image = pg.surface.Surface((100, 100))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.speed = 10
        self.x, self.y = center_coords
        self.rect.center = (self.x, self.y)

        self.k_up = config.K_UP
        self.k_down = config.K_DOWN
        self.k_left = config.K_LEFT
        self.k_right = config.K_RIGHT

        sprites_group.add(self)

    def update(self) -> None:
        """обновление логики."""
        self.move()

    def handle_events(self, events: list[pg.event.Event]) -> None:
        """реакция на события."""
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == self.k_up:
                    self.change_position(0, -self.speed)
                if event.key == self.k_down:
                    self.change_position(0, self.speed)
                if event.key == self.k_left:
                    self.change_position(-self.speed, 0)
                if event.key == self.k_right:
                    self.change_position(self.speed, 0)

    def change_position(self, d_x: int, d_y: int) -> None:
        """изменение координат."""
        self.x += d_x
        self.y += d_y

    def move(self) -> None:
        """движение."""
        self.rect.center = (self.x, self.y)
