from typing import Union, TypedDict
from models.vectors import Vector3, RGB
from math import sqrt
from utils.decorators import type_checker, number_greater_than_checker


class Sphere:
    @type_checker(
        checks={
            "center": Vector3,
            "radius": Union[int, float],
            "surfaceColor": RGB,
            "reflection": Union[int, float],
            "transparency": Union[int, float],
            "emissionColor": RGB,
        }
    )
    def __init__(
        self,
        center: Vector3,
        radius: Union[int, float],
        surfaceColor: RGB,
        reflection: Union[int, float] = 0,
        transparency: Union[int, float] = 0,
        emissionColor: RGB = RGB(),
    ) -> None:
        self.center = center
        self.radius = radius
        self.squareRadius = radius * radius
        self.surfaceColor = surfaceColor
        self.emissionColor = emissionColor
        self.transparency = transparency
        self.reflection = reflection

    @type_checker(checks=Vector3)
    def intersect(
        self, ray_origin: Vector3, ray_direction: Vector3
    ) -> tuple[bool, Union[int, float], Union[int, float]]:
        ray_to_sphere_center: Vector3 = self.center - ray_origin
        projection = ray_to_sphere_center.dot(ray_direction)

        if projection < 0:
            return (
                False,
                0,
                0,
            )

        distance_squared = (
            ray_to_sphere_center.dot(ray_to_sphere_center) - projection * projection
        )

        if distance_squared > self.squareRadius:
            return (
                False,
                0,
                0,
            )

        distance_to_surface = sqrt(self.squareRadius - distance_squared)
        first_intersection = projection - distance_to_surface
        second_intersection = projection + distance_to_surface

        return (
                True,
                first_intersection,
                second_intersection,
            )
