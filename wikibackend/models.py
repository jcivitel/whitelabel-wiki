import base64

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    logo = models.TextField(
        db_column='data',
        blank=True)

    def set_data(self, data):
        self.file = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self.file)

    data = property(get_data, set_data)

    def __str__(self):
        return self.name


class WikiPage(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=30, unique=True)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WikiPage2Customer(models.Model):
    WikiPage = models.ForeignKey(WikiPage, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} - {}".format(self.WikiPage.name, self.customer.name)
