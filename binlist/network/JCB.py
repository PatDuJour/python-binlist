from .abstract import AbstractNetwork


class JCB(AbstractNetwork):
    @property
    def verbose_name(self):
        return "Japan Credit Bureau"

    @property
    def active(self):
        return True

    @property
    def iin_ranges(self):
        """
        Reference:
            https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
            https://www.discoverglobalnetwork.com/downloads/IPP_VAR_Compliance.pdf
        """
        return list(map(str, range(3528, 3589 + 1)))

    @property
    def length(self):
        return list(range(16, 19 + 1))

    @property
    def validation(self):
        return True
