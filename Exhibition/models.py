from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Exhibition category
class ExhibitionCategory(models.Model):
    exhibition_category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.exhibition_category_name


# exhibition data modal
class Exhibition(models.Model):
    exhibition_name = models.CharField(max_length=100)
    exhibition_start_date = models.DateField()
    exhibition_end_date = models.DateField()
    exhibition_category = models.ForeignKey(ExhibitionCategory, on_delete=models.DO_NOTHING)
    exhibition_ticket_price = models.FloatField()

    def __str__(self):
        return self.exhibition_name


# stall in one exhibition
class ExhibitionStall(models.Model):
    stall_exhibition = models.ForeignKey(Exhibition, on_delete=models.DO_NOTHING)
    stall_number = models.CharField(max_length=20)
    stall_price = models.FloatField()
    stall_status = models.IntegerField(default=0)
    stall_reserved_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.stall_number


# custom stall
class CustomStall(models.Model):
    customized_stall = models.ForeignKey(ExhibitionStall, on_delete=models.DO_NOTHING)
    customized_name = models.CharField(max_length=100)
    stall_customized_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)



    def __str__(self):
        return self.customized_name


# banners in stall
class StallBanner(models.Model):
    stall_banner_stall = models.ForeignKey(ExhibitionStall, on_delete=models.DO_NOTHING)
    stall_banner_img = models.FileField(null=True)
    banner_status = models.IntegerField(default=0)


# pdf in stall
class StallPdf(models.Model):
    stall_pdf_stall = models.ForeignKey(ExhibitionStall, on_delete=models.DO_NOTHING)
    stall_pdf = models.FileField(null=True)
    pdf_status = models.IntegerField(default=0)


# videos in stall
class StallVideo(models.Model):
    stall_video_stall = models.ForeignKey(ExhibitionStall, on_delete=models.DO_NOTHING)
    stall_video = models.FileField(null=True)
    video_status = models.IntegerField(default=0)


# leaflets in stall
class StallLeaflet(models.Model):
    stall_leaflet_stall = models.ForeignKey(ExhibitionStall, on_delete=models.DO_NOTHING)
    stall_leaflet_img = models.FileField(null=True)
    leaflet_status = models.IntegerField(default=0)


# modals for stall
class StallModel(models.Model):
    stall_lmodel_stall = models.ForeignKey(ExhibitionStall, on_delete=models.DO_NOTHING)
    stall_model = models.FileField(null=True)
    model_status = models.IntegerField(default=0)

# payments for individual stall
class StallPayments(models.Model):
    stall_payment_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    stall_payment_exhibition = models.ForeignKey(Exhibition, on_delete=models.DO_NOTHING)
    stall_payment_exhibition_stall = models.ForeignKey(ExhibitionStall, on_delete=models.DO_NOTHING)
    stall_payment_date = models.DateTimeField(auto_now_add=True)
    stall_payment_banner = models.FloatField(null=True)
    stall_payment_video = models.FloatField(null=True)
    stall_payment_model = models.FloatField(null=True)
    stall_payment_leaflet = models.FloatField(null=True)
    stall_payment_pdf = models.FloatField(null=True)
    stall_payment_video_conf = models.FloatField(null=True)
    stall_payment_total_amount = models.FloatField()

    def __str__(self):
        return self.stall_payment_user.username 
