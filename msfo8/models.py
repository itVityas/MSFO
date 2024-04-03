from django.db import models


class EGIL(models.Model):
    data = models.DateField('Data')
    month_index = models.DecimalField('Month index', null=True, max_digits=15, decimal_places=4)
    year_index = models.DecimalField('Year index', null=True, max_digits=15, decimal_places=5)
    start_hyper_index = models.DecimalField('Start hyperinflation index', null=True, max_digits=15,
                                            decimal_places=3)
    hyper_index = models.DecimalField('Index for hyperinflation', max_digits=15, decimal_places=3)


class Bill(models.Model):
    name = models.CharField('Bill name', max_length=10)
    number = models.CharField('Bill name', max_length=10)

    def __str__(self):
        return f"{self.name}"


class Store(models.Model):
    name = models.CharField('Store name', max_length=50)
    numbers = models.CharField('Store number', max_length=20)

    def __str__(self):
        return f"{self.name}"


class Report(models.Model):
    name = models.CharField('Report name', max_length=20)
    date_write_off = models.DateField('Date write off')
    date_necessity = models.DateField('Date necessity')
    date_ig2014 = models.DateField('Date IG2014')

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    name = models.CharField('Material name', max_length=255)
    code = models.IntegerField('Code material')
    measuring = models.CharField('Measuring', max_length=20)

    def __str__(self):
        return f"{self.name}"


class Entrance(models.Model):
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    id_report = models.ForeignKey(Report, on_delete=models.CASCADE)
    id_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    id_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField('Receipt date')
    count = models.DecimalField('Count', max_digits=10, decimal_places=2)
    all_price = models.DecimalField('Cost', max_digits=15, decimal_places=2)
    price = models.CharField('Price', max_length=100)
    reclass = models.CharField('IFRS reclass account', max_length=100)
    write_off = models.CharField('Write-off of inventories', max_length=100)
    necessity_reserve = models.CharField('Necessity form reserve', max_length=100)
    ig2014 = models.CharField('IG2014', max_length=100)
    cost_msfo = models.CharField('IFRS cost', max_length=100)
    write_up = models.CharField('Unrealized GI revaluation', max_length=100)
    cost_write_off = models.CharField('Cost of materials written off', max_length=100)
    reserve = models.CharField('IFRS reserve', max_length=100)
