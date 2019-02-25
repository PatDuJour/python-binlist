import abc


class AbstractNetwork(abc.ABC):

    def __repr__(self):
        resource_name = self.__class__.__name__
        return f'<{resource_name.title()} Network>'

    def __str__(self):
        return self.verbose_name

    @property
    @abc.abstractmethod
    def verbose_name(self):
        """
        Returns:
            str: verbose name for the Issuing Network, i.e American Express,
                Visa, Mastercard.
        """
        pass

    @property
    @abc.abstractmethod
    def active(self):
        """
        Returns:
            bool: True for Issuing Network is still active,
                False if is defunct.
        """
        pass

    @property
    @abc.abstractmethod
    def iin_ranges(self):
        """
        Returns:
            list of str: Issuer identification number (IIN) ranges
        """
        pass

    @property
    @abc.abstractmethod
    def length(self):
        """
        Returns:
            list of int: possible length of a card number from
                the Issuing Network.
        """
        pass

    @property
    @abc.abstractmethod
    def validation(self):
        """
        Returns:
            bool: whether the card number uses the last digit for
                the Luhn check, set by ISO/IEC 7812.
        """
        pass
