from django.db import models


# Create your models here.
class Order(models.Model):
    number = models.CharField(max_length=100, verbose_name='单号')
    created_at = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "维修单"
        verbose_name_plural = "维修单"


class OrderStatus(models.Model):
    text = models.TextField(verbose_name='状态')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "状态：%s, 时间：%s" % (self.text, self.created_at.replace(microsecond=0))

    class Meta:
        verbose_name = "状态"
        verbose_name_plural = "状态"
