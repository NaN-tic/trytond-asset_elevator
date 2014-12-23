# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .asset import *


def register():
    Pool.register(
        Building,
        ElevatorType,
        Finish,
        ManeveurType,
        HoseType,
        Situation,
        Suspension,
        DoorType,
        Guide,
        Asset,
        module='asset_elevator', type_='model')
