from django.db import models
import datetime


class EGIL(models.Model):
    data = models.DateField('Data')
    month_index = models.DecimalField('Month index', null=True, max_digits=15, decimal_places=4)
    year_index = models.DecimalField('Year index', null=True, max_digits=15, decimal_places=5)
    start_hyper_index = models.DecimalField('Start hyperinflation index', null=True, max_digits=15,
                                            decimal_places=3)
    hyper_index = models.DecimalField('Index for hyperinflation', max_digits=15, decimal_places=3)

    def __str__(self):
        return f"{self.data}"


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
    date_write_off = models.DateField('Date write off',
                                      default=datetime.date(2017, 1, 1))
    date_necessity = models.DateField('Date necessity')
    date_ig2014 = models.DateField('Date IG2014',
                                   default=datetime.date(2015, 1, 1))

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    name = models.CharField('Material name', max_length=255)
    code = models.DecimalField('Code material', max_digits=20, decimal_places=0)
    measuring = models.CharField('Measuring', max_length=20)

    def __str__(self):
        return f"{self.name}"


class Files(models.Model):
    year = models.IntegerField('Year report')
    result_file = models.FileField(upload_to=f'static/xlsx/%Y-%m-%d', blank=True, null=True)
    created_at = models.DateTimeField('Time creation', auto_now_add=True)

    def __str__(self):
        return f"{self.year}, {self.result_file}"


class Entrance(models.Model):
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    id_report = models.ForeignKey(Report, on_delete=models.CASCADE)
    id_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    id_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    id_file = models.ForeignKey(Files, on_delete=models.CASCADE)
    date = models.DateField('Receipt date')
    count = models.DecimalField('Count', max_digits=10, decimal_places=2)
    all_price = models.DecimalField('Cost', max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.id_material}, {self.date}"
