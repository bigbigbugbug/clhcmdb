from django.db import models


# Create your models here.
class Switch(models.Model):
    name = models.CharField(max_length=100, verbose_name='交换机名称')
    ip = models.CharField(verbose_name='IP地址', max_length=32)
    position = models.CharField(max_length=256, verbose_name='交换机位置')
    description = models.CharField(max_length=1024, verbose_name='描述')
    image = models.ImageField(upload_to='image/')

    class Meta:
        verbose_name = "交换机"
        verbose_name_plural = "交换机信息"

    def __unicode__(self):
        return self.name


