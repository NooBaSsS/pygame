import pygame as pg

from player import Player


class Game:
    def __init__(self) -> None:
        self.sprites = pg.sprite.Group()
        self.player = Player(self)
