from django.db import models

class Purchase(models.Model):
    item = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()

    def __str__(self):
        return self.item
