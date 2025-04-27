from django.db import models

class GeneratedName(models.Model):
    keyword = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.keyword})"
