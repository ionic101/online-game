from game_engine.scene import Scene
from typing import List
import pygame
import game_settings as settings
from classes.button_actor import ButtonActor
from game_engine.game_engine import GameEngine
from scenes.singleplayer_scene import SingleplayerScene
from viewers.singleplayer_viewer import SingleplayerViewer
from controllers.singleplayer_controller import SingleplayerController


class MenuScene(Scene):
    def __init__(self) -> None:
        self._BUTTON_WIDTH: int = 300
        self._BUTTON_HEIGHT: int = 70
        self._BUTTOM_INTERVAL: int = 100

        self.buttons: List[ButtonActor] = [
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='singleplayer',
                callback=self.switch_on_level
            ),
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2 + self._BUTTOM_INTERVAL,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='multiplayer',
                callback=lambda: print('multiplayer')
            ),
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2 + self._BUTTOM_INTERVAL * 2,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='quit',
                callback=GameEngine.stop_forced
            ),
        ]

    def switch_on_level(self) -> None:
        GameEngine.set_session_forced(SingleplayerScene, SingleplayerViewer, SingleplayerController)
    
    def update(self, dt: float) -> None:
        pass
