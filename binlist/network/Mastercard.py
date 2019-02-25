from .abstract import AbstractNetwork


class Mastercard(AbstractNetwork):
    @property
    def verbose_name(self):
        return "Mastercard"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        """
        Reference:
            https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
            https://www.mastercard.us/content/dam/mccom/global/documents/mastercard-rules.pdf
        """
        return list(
            map(str, range(2221, 2720 + 1))
        ) + list(
            map(str, range(51, 55 + 1))
        )

    @property
    def length(self):
        return [16, ]

    @property
    def validation(self):
        return True
