from django.db import models
from django.urls import reverse
from hateykhori.models import Category

# Create your models here.
class Product(models.Model):
    ###############################################################################################
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='product_images')
    ################################################################################################
    slug = models.SlugField(max_length=100)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    #################################################################################################
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    #################################################################################################
    def __str__(self):
        return self.product_name