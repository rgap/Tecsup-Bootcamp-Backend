from client.models import Client
from django.db import models


class Payment(models.Model):
    PAYMENT_STATUS = [(1, "CREADO)"), (2, "PENDIENTE"), (3, "PAGADO"), (4, "RECHAZADO")]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_date = models.DateField()
    status = models.PositiveIntegerField(choices=PAYMENT_STATUS, default=1)
    amount = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.user.first_name} - {self.payment_date} - {self.status}"

    class Meta:
        db_table = "payments"