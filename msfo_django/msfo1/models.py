from django.db import models


class Counterparty(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class AccountMapping(models.Model):
    account_1c = models.CharField(max_length=50)
    sorting_number = models.IntegerField()
    db_account_number = models.CharField(max_length=50)

    class Meta:
        unique_together = ('account_1c', 'sorting_number')

    def __str__(self):
        return f"{self.account_1c} (Type {self.sorting_number}) -> {self.db_account_number}"



class Debt(models.Model):
    counterparty = models.ForeignKey(Counterparty, on_delete=models.CASCADE)
    account_1c = models.CharField(max_length=10)
    sorting_number = models.CharField(max_length=10)
    report_account = models.CharField(max_length=50, blank=True)
    debt_byn = models.DecimalField(max_digits=15, decimal_places=2)
    debt_contract_currency = models.DecimalField(max_digits=15, decimal_places=2)
    contract_currency = models.CharField(max_length=10)
    date_of_debt = models.DateField()
    payment_term_days = models.IntegerField()

    def save(self, *args, **kwargs):
        try:
            mapping = AccountMapping.objects.get(
                account_1c=self.account_1c,
                sorting_number=self.sorting_number
            )
            self.db_account_number = mapping.db_account_number
        except AccountMapping.DoesNotExist:
            self.db_account_number = 'Unknown'

        super().save(*args, **kwargs)