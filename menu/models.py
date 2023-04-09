from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "%s" % self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    path = models.CharField(max_length=128, blank=False, null=False)
    tree_level = models.CharField(max_length=256, blank=False, null=False, default='0')

    def __str__(self):
        return "%s" % self.name
