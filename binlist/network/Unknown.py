from .abstract import AbstractNetwork


class Unknown(AbstractNetwork):
    @property
    def verbose_name(self):
        return "Unknown"

    @property
    def active(self):
        return False

    @property
    def iin_ranges(self):
        return []

    @property
    def length(self):
        return []

    @property
    def validation(self):
        return False
