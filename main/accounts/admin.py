from django.contrib import admin
from . models import Contributor,Address

# Register your models here.

admin.site.register([Contributor,Address])