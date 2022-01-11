from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-add_date"]

    def __str__(self):
        return self.description


