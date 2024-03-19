from django.db import models


class EGIL(models.Model):
    data = models.DateField('Data')
    month_index = models.FloatField('Month index')
    year_index = models.FloatField('Year index')
    start_hyper_index = models.FloatField('Start hyperinflation index')
    hyper_index = models.FloatField('Index for hyperinflation')


class Bill(models.Model):
    name = models.CharField('Bill name')
    numbers = models.IntegerField('Bill number')

    def __str__(self):
        return f"{self.name}"


class Store(models.Model):
    name = models.CharField('Store name')
    numbers = models.IntegerField('Store number')

    def __str__(self):
        return f"{self.name}"


class Report(models.Model):                         # ДОПИСАТЬ ЗАВТРА, Я ЗАПУТАЛСЯ
    name = models.CharField('Report name')

    def __str__(self):
        return f"{self.name}"


MEASURE_CHOICES = (
    ("шт", "шт"),
    ("кг", "кг"),
)


class Material(models.Model):
    id_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    id_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    id_report = models.ForeignKey(Report, on_delete=models.CASCADE)
    name = models.CharField('Material name')
    code = models.IntegerField('Code material')
    measuring = models.CharField('Measuring')

    def __str__(self):
        return f"{self.name}"
