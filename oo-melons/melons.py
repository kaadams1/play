"""Classes for melon orders."""
import random

class AbstractMelonOrder:

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_base_price(self):
        return random.choice([5,6,7,8,9])

    def get_total(self, modifier=1.5):
        """Calculate price, including tax."""

        if species == "Christmas":
            base_price = self.get_base_price() * modifier

        else:
            base_price = self.get_base_price()
        
        total = (1 + self.tax) * self.qty * base_price


        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):   
        super().__init__(species, qty)
        self.order_type = "international"
        self.tax = 0.17
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self, flat=3):
        """Return total by adding flat fee of $3"""
        if self.qty < 10:
            return super().get_total() + flat
        else: 
            return super().get_total()


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):   
        super().__init__(species, qty)
        self.order_type = "Government"
        self.tax = 0
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True
        