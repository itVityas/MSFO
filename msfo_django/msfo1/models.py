from django.db import models
from django.utils import timezone
from django.utils.functional import empty


class Counterparty(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class AccountMapping(models.Model):
    account_1c = models.CharField(max_length=50)
    sorting_number = models.CharField(max_length=50)
    db_account_number = models.CharField(max_length=50)

    class Meta:
        unique_together = ('account_1c', 'sorting_number')

    def __str__(self):
        return f"{self.account_1c} (Type {self.sorting_number}) -> {self.db_account_number}"


class ReportFile(models.Model):
    file_path = models.CharField(max_length=500, unique=True, blank=True, null=True)
    year_report = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.file_path:
            return self.file_path
        else:
            return "No file path"


class Debt(models.Model):
    counterparty = models.ForeignKey(Counterparty, on_delete=models.CASCADE)
    account = models.ForeignKey(AccountMapping, on_delete=models.CASCADE)
    report_file = models.ForeignKey(ReportFile, on_delete=models.CASCADE)
    debt_byn = models.DecimalField(max_digits=15, decimal_places=2)
    debt_contract_currency = models.DecimalField(max_digits=15, decimal_places=2)
    contract_currency = models.CharField(max_length=10)
    date_of_debt = models.DateField(null=True, blank=True)
    payment_term_days = models.IntegerField()
