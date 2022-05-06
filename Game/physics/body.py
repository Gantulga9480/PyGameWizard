from Game.graphic.cartesian import CartesianPlane
from Game.graphic.shapes import polygon, shape, Vector2d
from Game.physics.core import vector2d
from math import pi

STATIC = 0
DYNAMIC = 1
FREE = 2


class body:

    def __init__(self, state, radius) -> None:
        super(body, self).__init__()
        self.state = state
        self.radius = radius

    def step(self):
        ...


class static_body(body):

    def __init__(self, radius) -> None:
        super(static_body, self).__init__(STATIC, radius)


class dynamic_body(body):

    def __init__(self, space, radius) -> None:
        super(dynamic_body, self).__init__(DYNAMIC, radius)
        self.acceleration = Vector2d(space, 0, 0)
        self.velocity = Vector2d(space, 0, 0)

    def step(self, pos: Vector2d, factor):
        if self.acceleration.length() > 1:
            self.velocity.x += self.acceleration._head.x.value
            self.velocity.y += self.acceleration._head.y.value
            self.acceleration.scale(1/1.1)
        if self.velocity.length() > 0:
            pos.x += self.velocity._head.x.value / factor
            pos.y += self.velocity._head.y.value / factor
            self.velocity.scale(1/1.1)


class base_body(polygon):

    def __init__(self,
                 body_type,
                 pos: Vector2d,
                 vertex_count: int = 2,
                 size: float = 1,
                 limit_vertex: bool = True) -> None:
        parent = CartesianPlane((size, size), 1, pos)
        super().__init__(parent_space=parent,
                         vertex_count=vertex_count,
                         size=size,
                         limit_vertex=limit_vertex)
        self.body_type = body_type
        if body_type == STATIC:
            self.body = static_body(size)
        elif body_type == DYNAMIC:
            self.body = dynamic_body(parent, size)
