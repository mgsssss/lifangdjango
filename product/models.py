from django.db import models


# Create your models here.


class Product(models.Model):
    
    
    client_company = models.CharField(max_length=256,
                               verbose_name='회사명', null=True,default='')    
        
    
    brand_company = models.CharField(max_length=256,
                                verbose_name='브랜드명', null=True,default='')



    name = models.CharField(max_length=256,
                                verbose_name='상품명', null=True,default='')
    

    
    
    price = models.IntegerField(verbose_name='상품가격')
    
    descrtiption = models.TextField(verbose_name='상품설명')

    stock = models.IntegerField(verbose_name='가품발견수')
    
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='등록날짜')
    
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'lifang_django_product'
        verbose_name = '기업목록'
        verbose_name_plural = '기업목록'
            