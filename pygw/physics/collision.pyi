from ..graphic.cartesian import CartesianPlane
from .body import Body


class collision:
    def __init__(self, plane: CartesianPlane) -> None: ...
    def check(self, b1: Body, b2: Body) -> None: ...
