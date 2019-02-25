from .abstract import AbstractNetwork


class Visa(AbstractNetwork):
    @property
    def verbose_name(self):
        return "Visa"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        return ["4", ]

    @property
    def length(self):
        return [16, ]

    @property
    def validation(self):
        return True
