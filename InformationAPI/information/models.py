from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    user_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat_name = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.user_category.id})

    def __str__(self):
        return self.subcat_name


class Information(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    info_title = models.CharField(max_length=100)
    info_list = RichTextField()

    def get_absolute_url(self):
        return reverse('info-detail', kwargs={'pk': self.sub_category.id})

    def __str__(self):
        return self.info_title
