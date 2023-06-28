from django.contrib import admin

# Register your models here.

from .models import BibTag, BibEntry, Author

admin.site.register(BibEntry)
admin.site.register(BibTag)
admin.site.register(Author)
