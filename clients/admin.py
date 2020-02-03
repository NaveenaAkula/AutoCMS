from django.contrib import admin

from .models import Client, Comment, VechicleByCustomer


class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


class VechicleAdmin(admin.ModelAdmin):
    model = VechicleByCustomer


admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(VechicleByCustomer)
