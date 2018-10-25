from django.contrib import admin
from .models import author,category,article ,comment ,message

# Register your models here.


class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]

    class Meta:
        Model = author


admin.site.register(author, authorModel)


class articleModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__", "body"]
    list_filter = ["posted_on", "category"]
    list_per_page = 10

    class Meta:
        Model = article


admin.site.register(article, articleModel)


class categoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "__str__"]

    class Meta:
        Model = category


admin.site.register(category, categoryModel)

class commentModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "__str__"]

    class Meta:
        Model = comment


admin.site.register(comment, commentModel)


class messageModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "__str__"]

    class Meta:
        Model = message


admin.site.register(message, messageModel)