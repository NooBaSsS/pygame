import pygame as pg

import config
from game import Game


class App:
    """приложение."""

    def __init__(self) -> None:
        """"""
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.is_running = False

    def mainloop(self) -> None:
        """главный цикл."""
        self.is_running = True
        self.game = Game(self)

        while self.is_running:
            events = pg.event.get()
            self.handle_events(events)
            self.update()
            self.render()
        pg.quit()

    def handle_events(self, events: list[pg.event.Event]) -> None:
        """реакция на события."""
        for event in events:
            if event.type == pg.KEYDOWN and event.key == config.K_QUIT:
                self.is_running = False
            if event.type == pg.QUIT:
                self.is_running = False
        self.game.handle_events(events)

    def update(self) -> None:
        """обновление логики."""
        self.game.update()

    def render(self) -> None:
        """обновление экрана."""
        self.screen.fill(config.GAME_BG_COLOR)
        self.game.sprites.draw(self.screen)
        pg.display.flip()


if __name__ == "__main__":
    game = App()
    game.mainloop()
    pg.quit()
