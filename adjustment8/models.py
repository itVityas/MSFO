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


class Report(models.Model):
    name = models.CharField('Report name')
    date_write_off = models.DateField('Date write off')
    date_necessity = models.DateField('Date necessity')
    date_ig2014 = models.DateField('Date IG2014')

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):

    name = models.CharField('Material name')
    code = models.IntegerField('Code material')
    measuring = models.CharField('Measuring')
    article = models.IntegerField('Article')

    def __str__(self):
        return f"{self.name}"


class Entrance(models.Model):
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    id_report = models.ForeignKey(Report, on_delete=models.CASCADE)
    id_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    id_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField('Receipt date')
    count = models.FloatField('Count')
    all_price = models.FloatField('Cost')
    price = models.FloatField('Price')
    reclass = models.FloatField('IFRS reclass account')
    write_off = models.CharField('Write-off of inventories')
    necessity_reserve = models.CharField('Necessity form reserve')
    ig2014 = models.FloatField('IG2014')
    cost_msfo = models.FloatField('IFRS cost')
    write_up = models.FloatField('Unrealized GI revaluation')
    cost_write_off = models.FloatField('Cost of materials written off')
    reserve = models.FloatField('IFRS reserve')
