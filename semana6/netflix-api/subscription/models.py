from django.db import models

# Create your models here.


class Subscription(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.IntegerField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # solo modificado una vez
    updated_at = models.DateTimeField(auto_now=True)

    # Para que en el admin muestre el titulo en vez de el objeto
    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        db_table = "subscription"


"""
Pasos para crear una tabla
1: Crear la migracion: Crea un archivo con el codigo necesario para poder crear la tabla

    python manage.py makemigrations subscription

2: Ejecutar la migracion

    python manage.py migrate subscription
"""

"""
CharField: Para textos cortos/medianos
FloatField: Para decimales
TextField: Para textos largos
DateTimeField: Para la fecha y hora
"""

"""
subscription_subscription --> <modulo>_<tabla>
"""
