from .abstract import AbstractNetwork


class ChinaTUnion(AbstractNetwork):
    @property
    def verbose_name(self):
        return "China T-Union"

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
