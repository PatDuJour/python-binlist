from .abstract import AbstractNetwork


class MaestroUK(AbstractNetwork):
    @property
    def verbose_name(self):
        return "MaestroUK"

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
        return [
            "6759",
            "676770",
            "676774",
        ]

    @property
    def length(self):
        return list(range(12, 19 + 1))

    @property
    def validation(self):
        return True
