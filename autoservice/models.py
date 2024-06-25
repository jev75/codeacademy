from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Paslauga')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Kaina')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name_plural = 'Paslaugos'


class Order(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='Automobilis')
    date = models.DateField(verbose_name='Data')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Bendra suma')

    def __str__(self):
        return f'{self.car} {self.date}  {self.total_sum}'

    class Meta:
        verbose_name_plural = 'Užsakymai'


class OrderService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Užsakoma paslauga')
    quantity = models.IntegerField(verbose_name='Kiekis')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Užsakymas')

    STATUS_AUTO = (
        ('v', 'Vykdoma'),
        ('b', 'Baigta'),
        ('e', 'Eilėje'),
    )
    status = models.CharField(max_length=1, choices=STATUS_AUTO, default='e', verbose_name='Statusas', blank=True, null=True)

    def __str__(self):
        return f'{self.service}'

    class Meta:
        ordering = ['status']
        verbose_name_plural = 'Užsakytos paslaugos'


class Car(models.Model):
    client = models.CharField(max_length=200, verbose_name='Klientas')
    license_plate = models.CharField(max_length=20, verbose_name='Valstybinis numeris')
    VIN_code = models.CharField(max_length=20, verbose_name='VIN kodas')
    year = models.IntegerField(verbose_name='Metai')
    brand = models.CharField(max_length=200, verbose_name='Markė')
    model = models.CharField(max_length=200, verbose_name='Modelis')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Paveikslėlis')

    def __str__(self):
        return f'{self.client} {self.brand} {self.model} '

    class Meta:
        verbose_name_plural = 'Automobiliai'