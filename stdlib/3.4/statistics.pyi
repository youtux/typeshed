# Stubs for pathlib (Python 3.4)

import decimal
import fractions

from typing import Union, Iterable, Any

AnyNumber = Union[int, float, decimal.Decimal, fractions.Fraction]

class StatisticsError(ValueError): ...

def mean(data: Iterable[AnyNumber]) -> AnyNumber: ...

def median(data: Iterable[AnyNumber]) -> AnyNumber: ...

def median_grouped(data: Iterable[AnyNumber], interval: int = 1) -> AnyNumber: ...

def median_high(data: Iterable[AnyNumber]) -> AnyNumber: ...

def median_low(data: Iterable[AnyNumber]) -> AnyNumber: ...

def mode(data: Iterable[Any]) -> Any: ...

def pstdev(data: Iterable[AnyNumber]) -> AnyNumber: ...

def pvariance(data: Iterable[AnyNumber]) -> AnyNumber: ...

def stdev(data: Iterable[AnyNumber]) -> AnyNumber: ...

def variance(data: Iterable[AnyNumber]) -> AnyNumber: ...
