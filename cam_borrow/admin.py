from django.contrib import admin

from cam_borrow import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Seller)
admin.site.register(models.Customer)
admin.site.register(models.Camera)
admin.site.register(models.Lens)
admin.site.register(models.Accessory)