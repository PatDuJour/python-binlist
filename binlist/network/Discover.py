from .abstract import AbstractNetwork


class Discover(AbstractNetwork):
    @property
    def verbose_name(self):
        return "Discover"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        return [
            "6011",
            "64",
            "65",
        ]

    @property
    def length(self):
        return [16, ]

    @property
    def validation(self):
        return True
