from Game import Game
from Game import core
from Game.graphic import CartesianPlane
from Game.physics import (DynamicTriangleBody,
                          StaticTriangleBody,
                          EnginePolygon,
                          FreePolygonBody,
                          object_body)
import numpy as np


class Test(Game):

    def __init__(self) -> None:
        super().__init__()
        self.size = (1920, 1080)
        self.window_flags = core.FULLSCREEN | core.HWSURFACE

    def setup(self):
        self.plane = CartesianPlane(self.window, self.size)
        self.b1_plane = self.plane.createPlane()
        self.b2_plane = self.plane.createPlane(300, 300)
        self.b1 = DynamicTriangleBody(0, self.b1_plane, (30, 30, 30), 10)
        self.b2 = FreePolygonBody(1, self.b2_plane, (30, 30, 30))

        # self.b1.attach(self.b2, False)
        self.engine = EnginePolygon(self.plane, np.array([self.b1, self.b2], dtype=object_body))

    def onEvent(self, event):
        if event.type == core.KEYUP:
            if event.key == core.K_q:
                self.running = False

    def loop(self):
        if self.keys[core.K_f]:
            self.b1.detach(self.b2)
        if self.keys[core.K_g]:
            self.b1.attach(self.b2, False)

        if self.keys[core.K_LEFT]:
            self.b1.rotate(0.1)
        if self.keys[core.K_RIGHT]:
            self.b1.rotate(-0.1)
        if self.keys[core.K_UP]:
            self.b1.accelerate(0.3)
        if self.keys[core.K_DOWN]:
            self.b1.accelerate(-0.3)

        if self.keys[core.K_a]:
            self.b2.rotate(0.1)
        if self.keys[core.K_d]:
            self.b2.rotate(-0.1)
        if self.keys[core.K_w]:
            self.b2.accelerate(0.3)
        if self.keys[core.K_s]:
            self.b2.accelerate(-0.3)

        self.engine.step()

    def onRender(self):
        self.window.fill((255, 255, 255))
        self.b1.show(True)
        self.b2.show(True)


Test().loop_forever()
