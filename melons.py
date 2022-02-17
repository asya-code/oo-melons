"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    #order_type = None
    #tax = 0
    def __init__(self, species, qty, order_type, tax):
        """Initialize all orders to general attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True
    
    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == 'Christmas melon':
            base_price = base_price * 1.5
        total = float("{:.2f}".format((1 + self.tax) * self.qty * base_price)) #-->hey, how to get two digits?
        if self.qty < 10 and self.order_type == "international":
            total = total + 3
        return total

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    # tax = 0.17
    # order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code
        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovermentMelonOrder(AbstractMelonOrder):
    """An US Government melon order"""
    #order_type = "goverment"
    # tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "goverment", 0)
        self.passed_inspection = False


    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True

    

