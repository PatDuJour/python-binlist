from .abstract import AbstractNetwork


class RuPay(AbstractNetwork):
    @property
    def verbose_name(self):
        return "RuPay"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        return [
            "60",
            "6521",
            "6522",
        ]

    @property
    def length(self):
        return [16, ]

    @property
    def validation(self):
        return True
