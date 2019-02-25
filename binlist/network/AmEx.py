from .abstract import AbstractNetwork


class AmEx(AbstractNetwork):
    @property
    def verbose_name(self):
        return "American Express"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        return ["34", "37"]

    @property
    def length(self):
        return [15, ]

    @property
    def validation(self):
        return True
