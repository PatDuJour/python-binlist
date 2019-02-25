from .AmEx import AmEx
from .ChinaTUnion import ChinaTUnion
from .ChinaUnionPay import ChinaUnionPay
from .DinersClub import DCI
from .Discover import Discover
from .JCB import JCB
from .Maestro import Maestro
from .MaestroUK import MaestroUK
from .Mastercard import Mastercard
from .RuPay import RuPay
from .Visa import Visa

__all__ = [
    'AmEx',
    'ChinaTUnion',
    'ChinaUnionPay',
    'DCI',
    'Discover',
    'JCB',
    'Maestro',
    'MaestroUK',
    'Mastercard',
    'RuPay',
    'Visa',
]


AmEx = AmEx()
ChinaTUnion = ChinaTUnion()
ChinaUnionPay = ChinaUnionPay()
DCI = DCI()
Discover = Discover()
JCB = JCB()
Maestro = Maestro()
MaestroUK = MaestroUK()
Mastercard = Mastercard()
RuPay = RuPay()
Visa = Visa()
