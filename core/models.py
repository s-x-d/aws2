from django.db import models

class RainbowColor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hex_code = models.CharField(max_length=7)
    order = models.IntegerField(unique=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    @classmethod
    def get_all_colors(cls):
        return cls.objects.all()

    @classmethod
    def get_color_by_name(cls, name):
        try:
            return cls.objects.get(name__iexact=name)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_color_by_order(cls, order):
        try:
            return cls.objects.get(order=order)
        except cls.DoesNotExist:
            return None
