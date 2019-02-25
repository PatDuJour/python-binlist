from .abstract import AbstractNetwork


class DCI(AbstractNetwork):
    @property
    def verbose_name(self):
        return "Diners Club International"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        return [
            "36",
            "38",
            "39",
            "300",
            "301",
            "302",
            "303",
            "304",
            "305",
            "3095",
        ]

    @property
    def length(self):
        return list(range(14, 19 + 1))

    @property
    def validation(self):
        return True
