from __future__ import annotations
from functools import reduce
from typing import List


class Bill:

    def __init__(self, amount: float, period: str):
        self._amount = amount
        self._period = period

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def period(self) -> str:
        return self._period


class Flatmate:

    _flatmates: List[Flatmate] = []

    def __init__(self, name: str, days_lived: int = 0):
        self._name = name
        self._days_lived = days_lived
        self._flatmates.append(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def days_lived(self) -> int:
        return self._days_lived

    @classmethod
    def flatmates(cls) -> List[Flatmate]:
        return cls._flatmates

    # noinspection PyTypeChecker
    def calc_share(self, bill: Bill) -> float:
        weight = self._days_lived / reduce(lambda a, b:
                                           a.days_lived + b.days_lived,
                                           self._flatmates)
        return bill.amount * weight

    @classmethod
    def calc_shares(cls, bill: Bill) -> dict:
        shares = []
        for flatmate in cls._flatmates:
            shares.append({'name': flatmate.name,
                           'share': flatmate.calc_share(bill)})
        return {'period': bill.period, 'shares': shares}
