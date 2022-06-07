from django.contrib import admin
from Exhibition.models import *
# Register your models here.
admin.site.register(ExhibitionCategory),
admin.site.register(Exhibition)
admin.site.register(ExhibitionStall)
admin.site.register(StallPayments)
admin.site.register(StallModel)
admin.site.register(StallVideo)
admin.site.register(StallBanner)
admin.site.register(StallLeaflet)
admin.site.register(StallPdf)