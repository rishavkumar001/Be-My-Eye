from django.contrib import admin
from information.models import Information

class InformationAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'company_name', 'product_description', 'product_cost', 'manu_date', 'exp_date', 'product_image', 'qr_code')

admin.site.register(Information, InformationAdmin)

# Register your models here.
