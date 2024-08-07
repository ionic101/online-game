from abc import ABC
from game_engine.scene import Scene
import pygame
import game_engine.game_engine as game_engine
from typing import List
from enum import IntEnum


class MouseButton(IntEnum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3


class Controller(ABC):
    def __init__(self, scene: Scene) -> None:
        self._scene = scene

    def set_scene(self, new_scene: Scene) -> None:
        assert isinstance(new_scene, Scene), Exception('In argument must be scene')
        self._scene = new_scene
        
    def control(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                game_engine.GameEngine.stop_forced()
