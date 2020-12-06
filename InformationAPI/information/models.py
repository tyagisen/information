from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat_name = models.CharField(max_length=250)


    def __str__(self):
        return self.subcat_name


class Information(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    info_title = models.CharField(max_length=100)
    info_list = models.CharField(max_length=500)

    def __str__(self):
        return self.info_title
