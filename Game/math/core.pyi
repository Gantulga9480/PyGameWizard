from typing import Union

_vector2d_or_tuple = Union[vector2d, tuple]


class scalar:
    is_limit: bool
    def __init__(self, value: float, limits: tuple) -> None: ...
    @property
    def value(self) -> float: ...
    @value.setter
    def value(self, o: float) -> None: ...


class point2d:
    def __init__(self,
                 x: float,
                 y: float,
                 x_lim: tuple = None,
                 y_lim: tuple = None) -> None: ...

    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, o: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, o: float) -> None: ...
    @property
    def xy(self) -> tuple: ...
    @xy.setter
    def xy(self, o: object) -> None: ...


class vector2d:
    def __init__(self,
                 x: float,
                 y: float,
                 max_length: float = 0,
                 min_length: float = 0) -> None: ...

    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, o: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, o: float) -> None: ...
    @property
    def head(self) -> tuple: ...
    @head.setter
    def head(self, o: tuple) -> None: ...
    @property
    def tail_x(self) -> float: ...
    @tail_x.setter
    def tail_x(self, o: float): ...
    @property
    def tail_y(self) -> float: ...
    @tail_y.setter
    def tail_y(self, o: float): ...
    @property
    def tail(self) -> tuple: ...
    @tail.setter
    def tail(self, o: tuple) -> None: ...
    def add(self, o: float) -> None: ...
    def scale(self, o: float) -> None: ...
    def set_x_ref(self, o: scalar) -> None: ...
    def set_y_ref(self, o: scalar) -> None: ...
    def set_head_ref(self, o: point2d) -> None: ...
    def set_tail_x_ref(self, o: scalar) -> None: ...
    def set_tail_y_ref(self, o: scalar) -> None: ...
    def set_tail_ref(self, o: point2d) -> None: ...
    def rotate(self, radians: float) -> None: ...
    def length(self) -> float: ...
    def direction(self) -> float: ...
    def distance_to(self, vector: vector2d) -> float: ...
    def angle_between(self, vector: vector2d) -> float: ...
    def dot(self, vector: vector2d) -> float: ...
    def unit(self, scale: float = 1, vector: bool = True) -> _vector2d_or_tuple: ...
    def update(self) -> None: ...
