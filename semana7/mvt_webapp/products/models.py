from django.db import models


# Model: Represents the data structure and business logic
class Product(models.Model):
    price = models.CharField(max_length=100, blank=True)

    def update_price(self, new_price):
        self.price = new_price
        self.save()

    def get_price(self):
        return self.price
