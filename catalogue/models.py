from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalogue:pages_list_by_category", args=[self.slug])


class Page(models.Model):
    category = models.ForeignKey(
        Category, related_name="pages", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    image = models.CharField(max_length=200, db_index=True, blank=True)
    url = models.URLField(max_length=200, db_index=True, blank=True)
    description = models.TextField(blank=True)
    # email = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)
        index_together = (("id"),)

    def __str__(self):
        return self.name
