import pygame as pg

from game import Game


class App:
    """приложение"""

    def __init__(self) -> None:
        """"""
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.is_running = False

    def mainloop(self) -> None:
        """"""
        self.is_running = True
        self.game = Game()

        while self.is_running:
            events = pg.event.get()
            self.handle_events(events)
            self.update()
            self.render()

    def handle_events(self, events: list[pg.event.Event]):
        """"""
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.is_running = False
            if event.type == pg.QUIT:
                self.is_running = False

    def update(self):
        """обновление логики"""
        self.game.sprites.update()

    def render(self) -> None:
        """"""
        self.game.sprites.draw(self.screen)
        pg.display.flip()


if __name__ == "__main__":
    game = App()
    game.mainloop()
    pg.quit()
