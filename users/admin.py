from django.contrib import admin
from .models import User

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    users_image = ('img_name', 'image')
    

