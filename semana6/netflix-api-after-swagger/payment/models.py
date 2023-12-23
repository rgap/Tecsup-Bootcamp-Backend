from client.models import Client
from django.core.validators import MaxValueValidator
from django.db import models


class Payment(models.Model):
    PAYMENT_STATUS = [(1, "CREADO)"), (2, "PENDIENTE"), (3, "PAGADO"), (4, "RECHAZADO")]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_date = models.DateField()

    ## campos recibidos de pagar con mercadopago
    payer_email = models.EmailField(max_length=250, null=True)
    payer_document_type = models.CharField(max_length=10, blank=True)
    payer_document_number = models.CharField(max_length=50, blank=True)
    installments = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(36)], null=True
    )
    issuer_id = models.CharField(max_length=100, null=True, blank=True)
    payment_method_id = models.CharField(max_length=20, blank=True)
    token = models.CharField(max_length=250, blank=True)
    ################################################################

    status = models.PositiveIntegerField(choices=PAYMENT_STATUS, default=1)
    amount = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.user.first_name} - {self.payment_date} - {self.status}"

    class Meta:
        db_table = "payments"
