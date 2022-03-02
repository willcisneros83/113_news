from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=256)
    body =models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])


# Mini challenge:
# 1. Create a new articles app (and install it).
# 2. Copy the model above to articles/models.py
# 3. Make migrations then migrate.

# 5. Create a fully functional CRUD + Scan.
# 6. Ensure that only registered users can create, update and delete articles.
# 7. Ensure that only article authors can update and delete their own articles.

# Bonus: Make it so that only staff users can create, update and delete articles.
