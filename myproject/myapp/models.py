from django.db import models

class Blog(models.Model):
    user_name = models.CharField(max_length=100)
    blog_text = models.TextField()

    def __str__(self):
        return self.user_name 