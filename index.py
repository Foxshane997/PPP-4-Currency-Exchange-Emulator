class Currency:

    currencies = {'CHF': 0.930023,  # Swiss franc
                   'CAD': 1.264553,  # Canadian dollar
                   'GBP': 0.737414,  # British pound
                   'JPY': 111.019919,  # Japanese yen
                   'EUR': 0.862361,  # Euro
                   'USD': 1.0}  # US dollar

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        A Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __repr__(self):
        return f"{self.value:.2f} {self.unit}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, Currency):
            # Convert other to the same unit as self
            other_value_in_self_unit = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
            return Currency(self.value + other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            # Treat other as USD value
            return Currency(self.value + other, self.unit)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Currency):
            other_value_in_self_unit = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
            self.value += other_value_in_self_unit
        elif isinstance(other, (int, float)):
            self.value += other
        else:
            return NotImplemented
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Currency):
            # Convert other to the same unit as self
            other_value_in_self_unit = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
            return Currency(self.value - other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            # Treat other as USD value
            return Currency(self.value - other, self.unit)
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Currency):
            other_value_in_self_unit = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
            self.value -= other_value_in_self_unit
        elif isinstance(other, (int, float)):
            self.value -= other
        else:
            return NotImplemented
        return self

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            # Treat other as USD value and subtract from self
            return Currency(other - self.value, self.unit)
        else:
            return NotImplemented


def simple_test():
    # Create Currency objects
    eur = Currency(23.43, "EUR")
    usd = Currency(19.97, "USD")

    # Test addition of two Currency objects
    result_add = eur + usd
    print(f"eur + usd: {result_add}")  # Should convert USD to EUR and add

    # Test addition with a numerical value (USD)
    result_add_num = eur + 5
    print(f"eur + 5 USD: {result_add_num}")  # Should add 5 USD to EUR value

    # Test subtraction of two Currency objects
    result_sub = eur - usd
    print(f"eur - usd: {result_sub}")  # Should convert USD to EUR and subtract

    # Test subtraction with a numerical value (USD)
    result_sub_num = eur - 3
    print(f"eur - 3 USD: {result_sub_num}")  # Should subtract 3 USD from EUR value

if __name__ == "__main__":
    simple_test()
