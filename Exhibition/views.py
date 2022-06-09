from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from Exhibition.models import *


# Create your views here.

# exhibition creation details
def create_new_exhibition(request):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"
    exhibition_types = ExhibitionCategory.objects.all()
    if request.method == "POST":
        exhibition_name = request.POST.get('exhibition_name_create')
        exhibition_type = request.POST.get('exhibition_type')
        start_date = request.POST.get('exhibition_start_date')
        end_date = request.POST.get('exhibition_end_date')
        ticket_amount = request.POST.get('exhibition_amount')

        try:
            exhibition_type_obj = ExhibitionCategory.objects.get(id=exhibition_type)
        except:
            print("exhibition type not found")

        new_exhibition = Exhibition(
            exhibition_name=exhibition_name,
            exhibition_category=exhibition_type_obj,
            exhibition_start_date=start_date,
            exhibition_end_date=end_date,
            exhibition_ticket_price=ticket_amount
        )

        new_exhibition.save()

    context = {
        "EXHIBITION_TYPE": exhibition_types,
        'LOGGED_GROUP': logged_group,

    }
    return render(request, 'exhibition/create_exhibition.html', context)


# created exhibition list
def exhibition_list(request):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"
    try:
        all_exhibitions = Exhibition.objects.all()
    except:
        print("exhibition matching query didn't found")

    context = {
        "ALL_EXHIBITIONS": all_exhibitions,
        'LOGGED_GROUP': logged_group,

    }

    return render(request, 'exhibition/all_exhibitions.html', context)


def create_stall(request):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"
    if not ExhibitionStall.objects.exists():
        stall_id = 'S' + str(1).zfill(3)
    else:
        current_stall_id = ExhibitionStall.objects.all().last().id
        stall_id = 'S' + str(current_stall_id + 1).zfill(3)

    print('this is stall id', stall_id)

    # exhibition query
    try:
        all_exhibitions = Exhibition.objects.all()
    except:
        print("exhibition matching query didn't found")

    if request.method == 'POST':
        related_exhibition_id = request.POST.get('stall_exhibition')
        stall_no = request.POST.get('stall_num')
        stall_amount = request.POST.get('stall_price')

        # stall exhibition object
        try:
            related_exhibition_object = Exhibition.objects.get(id=related_exhibition_id)
        except:
            print("Exhibition not found")

        # print(related_exhibition_id,related_exhibition_object.exhibition_name,stall_no,stall_amount)
        new_exhibition_stall = ExhibitionStall(
            stall_exhibition=related_exhibition_object,
            stall_number=stall_no,
            stall_price=stall_amount,
            stall_reserved_by=request.user
        )

        new_exhibition_stall.save()

    context = {
        "STALL_ID": stall_id,
        "ALL_EXHIBITIONS": all_exhibitions,
        'LOGGED_GROUP': logged_group,
    }
    return render(request, 'exhibition/create_stall.html', context)


def all_stalls(request, pk):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"
    # all stalls for given exhibition
    try:
        stall_list = ExhibitionStall.objects.filter(stall_exhibition__id=pk)
    except:
        print("stalls are not found")

    context = {
        "STALL_LIST": stall_list,
        'LOGGED_GROUP': logged_group,
    }
    return render(request, 'exhibition/all_stalls.html', context)

def my_stalls(request):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"
    # all stalls for given exhibition
    print(request.user)
    try:
        my_stall_list = ExhibitionStall.objects.filter(stall_reserved_by=request.user)
        print(my_stall_list)
        # my_stall_list = my_payments
        # print(my_stall_list.)

    except:
        print("stalls are not found")

    context = {
        "MY_STALL_LIST": my_stall_list,
        'LOGGED_GROUP': logged_group,
    }
    return render(request, 'exhibition/my_stalls.html', context)


# image upload for stalls
def stall_image_uploading(request, pk):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"

    if request.method == "POST":
        uploaded_list = []
        fss = FileSystemStorage()
        image_list = request.FILES.getlist('stall_modal_image')
        for img in image_list:
            file = fss.save(img.name, img)
            file_url = fss.url(file)
            uploaded_list.append(file_url)

            print(file_url)
        print("This is list list ", uploaded_list)

    context = {
        'LOGGED_GROUP': logged_group,
    }

    return render(request, 'exhibition/create_stall_modal.html', context)


def purchase_stall(request, pk):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"

    try:
        purchasing_stall = ExhibitionStall.objects.get(id=pk)
    except:
        print("searched_stall_not_found")

    reserved_user = request.user

    if request.method == 'POST':
        tot_banner = request.POST.get('banner_total')
        tot_video = request.POST.get('video_total')
        tot_model = request.POST.get('leaflet_total')
        tot_leaflet = request.POST.get('model_total')
        tot_pdf = request.POST.get('pdf_total')
        tot_video_con = request.POST.get('conf_total')
        tot_sum = request.POST.get('stall_custom_price')

        new_stall_payment = StallPayments(
            stall_payment_user=reserved_user,
            stall_payment_exhibition=purchasing_stall.stall_exhibition,
            stall_payment_exhibition_stall=purchasing_stall,
            stall_payment_banner=tot_banner,
            stall_payment_video=tot_video,
            stall_payment_model=tot_model,
            stall_payment_leaflet=tot_leaflet,
            stall_payment_pdf=tot_pdf,
            stall_payment_video_conf=tot_video_con,
            stall_payment_total_amount=tot_sum

        )

        new_stall_payment.save()
        new_stall_payment.stall_payment_exhibition_stall.stall_status = 1
        new_stall_payment.stall_payment_exhibition_stall.save()

        purchasing_stall.stall_reserved_by = request.user
        purchasing_stall.save()

        fss = FileSystemStorage()
        banner_list = request.FILES.getlist('stall_banner')
        print("this is banner list", banner_list)
        if banner_list:
            for banner in banner_list:
                file = fss.save(banner.name, banner)
                file_url = fss.url(file)
                file_url = file_url.split('/')[-1]
                print("This is file url", file_url)
                new_stall_banner = StallBanner(
                    stall_banner_stall=purchasing_stall,
                    stall_banner_img=file_url
                )
                new_stall_banner.save()

        video_list = request.FILES.getlist('stall_video')
        if video_list:
            for video in video_list:
                file = fss.save(video.name, video)
                file_url = fss.url(file)
                file_url = file_url.split('/')[-1]
                new_stall_video = StallVideo(
                    stall_video_stall=purchasing_stall,
                    stall_video=file_url
                )
                new_stall_video.save()

        leaflet_list = request.FILES.getlist('stall_leaflet')
        if leaflet_list:
            for leaflet in leaflet_list:
                file = fss.save(leaflet.name, leaflet)
                file_url = fss.url(file)
                file_url = file_url.split('/')[-1]
                new_stall_leaflet = StallLeaflet(
                    stall_leaflet_stall=purchasing_stall,
                    stall_leaflet_img=file_url
                )
                new_stall_leaflet.save()

        if request.method == 'POST' and request.FILES.get('stall_information_sheet'):
            stall_pdf = request.FILES.get('stall_information_sheet')
            file = fss.save(stall_pdf.name, stall_pdf)
            file_url = fss.url(file)
            file_url = file_url.split('/')[-1]

            new_stall_pdf = StallPdf(
                stall_pdf_stall=purchasing_stall,
                stall_pdf=file_url
            )

            new_stall_pdf.save()

        if request.method == 'POST' and request.FILES.get('stall_model'):
            stall_3d_model = request.FILES.get('stall_model')
            file = fss.save(stall_3d_model.name, stall_3d_model)
            file_url = fss.url(file)
            file_url = file_url.split('/')[-1]
            new_stall_model = StallModel(
                stall_lmodel_stall=purchasing_stall,
                stall_model=file_url
            )

            new_stall_model.save()



    context = {
        "STALL_ID": purchasing_stall.id,
        'LOGGED_GROUP': logged_group,

    }
    return render(request, 'exhibition/create_stall_purchase.html', context)


def calculate_stall_payment(request):
    banner_cost = None
    video_cost = None
    model_cost = None
    pdf_cost = None
    leaflet_cost = None
    vcon_cost = None
    stall_id_ajax = request.GET.get('stall_id')
    print("Stall id from ajax", stall_id_ajax)

    banner_count = request.GET.get('no_of_banners')
    video_count = request.GET.get('no_of_videos')
    model_count = request.GET.get('models')
    pdf_count = request.GET.get('pdf')
    leaflet_count = request.GET.get('no_of_leaflets')
    video_conf_count = request.GET.get('video_con')
    tot = 0

    if banner_count:
        banner_cost = 10 * int(banner_count)
        print("Banner Cost:", banner_cost)
        tot += banner_cost

    if video_count:
        video_cost = 20 * int(video_count)
        print("video Cost:", video_cost)
        tot += video_cost

    if model_count == "True":
        model_cost = 30
        tot += model_cost
        print("model Cost:", model_count)

    if pdf_count == "1":
        pdf_cost = 10
        tot += pdf_cost
        print("pdf Cost:", pdf_cost)

    if leaflet_count:
        print("lc", leaflet_count)
        leaflet_cost = 5 * int(leaflet_count)
        tot += leaflet_cost
        print("leaflet Cost:", leaflet_cost)

    if video_conf_count == "1":
        vcon_cost = 30
        tot += vcon_cost
        print("vcon Cost:", vcon_cost)

    if  video_conf_count == "2":
        vcon_cost = 0
        tot += vcon_cost


    print("total Cost:", tot)

    print(banner_count, video_count, model_count, pdf_count, leaflet_count)

    return JsonResponse(
        {'Total_Cost': tot,
         'Banner_Cost': banner_cost,
         'VideoCost': video_cost,
         'ModelCost': model_cost,
         'PdfCost': pdf_cost,
         'LeafletCost': leaflet_cost,
         'VconCost': vcon_cost

         })


# all payments
def all_payments(request):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"
    all_received_payments = StallPayments.objects.all()
    context = {
        "ALL_PAY": all_received_payments,
        'LOGGED_GROUP': logged_group,

    }
    return render(request, 'exhibition/all_payments.html', context)


def user_defined_payments(request):
    if not request.user.is_staff:
        logged_group = request.user.groups.all()[0].name
    else:
        logged_group = "ADMIN"
    logged_user_payments = StallPayments.objects.filter(stall_payment_user=request.user)

    context = {

        'MY_PAYMENTS': logged_user_payments,
        'LOGGED_GROUP': logged_group,

    }

    return render(request, 'exhibition/my_payments.html', context)
