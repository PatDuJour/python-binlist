from .abstract import AbstractNetwork


class ChinaUnionPay(AbstractNetwork):
    @property
    def verbose_name(self):
        return "China UnionPay"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        return ["31", ]

    @property
    def length(self):
        return [19, ]

    @property
    def validation(self):
        return True
