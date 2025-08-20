from django.db import models

# Create your models here.
class techProducts(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(default=100,null=True,decimal_places=2,max_digits=10)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    instock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f"{self.name}"
    


