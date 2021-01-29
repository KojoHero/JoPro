from django.contrib import admin
from .models import BlogModel, DocxModel, CatModel, FAQModel, ListModel

# Register your models here.
admin.site.register(BlogModel)
admin.site.register(DocxModel)
admin.site.register(CatModel)
admin.site.register(FAQModel)
admin.site.register(ListModel)