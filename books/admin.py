from django.contrib import admin
from .models import Book, Review, Source, Translation

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Source)
admin.site.register(Translation)
