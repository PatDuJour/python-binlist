from .abstract import AbstractNetwork


class Maestro(AbstractNetwork):
    @property
    def verbose_name(self):
        return "Maestro"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        """
        Reference:
            https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
            https://www.barclaycard.co.uk/business/files/BIN-Rules-UK.pdf
        """
        return ['50', ] + list(map(str, range(56, 69 + 1)))

    @property
    def length(self):
        return list(range(12, 19 + 1))

    @property
    def validation(self):
        return True
