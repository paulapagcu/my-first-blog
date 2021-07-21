from django.contrib import admin
from .models import Post
# importe Post model define in blog/models.py

# the code below makes the Post model visible on the admin page
admin.site.register(Post)