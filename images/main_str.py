from dataclasses import dataclass
from typing import NamedTuple

from pympler import asizeof


@dataclass
class CoordinatesDT:
    longitude: float
    latitude: float


class CoordinatesNT(NamedTuple):
    longitude: float
    latitude: float


coordinates_dt = CoordinatesDT(longitude=10.0, latitude=20.0)
coordinates_nt = CoordinatesNT(longitude=10.0, latitude=20.0)

print('dataclass:', asizeof.asized(coordinates_dt).size)
print('nametuple:', asizeof.asized(coordinates_nt).size)


@dataclass(slots=True, frozen=True)
class CoordinatesDT2:
    longitude: float
    latitude: float


coordinates_dt2 = CoordinatesDT2(longitude=10.0, latitude=20.0)

print("dataclass with frozen and slots:",
      asizeof.asized(coordinates_dt2).size)
# dataclass with frozen and slots: 96 bytes
