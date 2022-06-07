$(document).ready(function() {

    $("#banner_error").hide()
    $("#video_error").hide()
    $("#generate_model").hide()
    $("#upload_model").hide()
    $("#leaflet_error").hide()
    $("#infoemation_sheet_av").hide()



    let image_limit,image_count, video_limit,video_count,modal_availability,leaflet_limit,leaflet_count,info_sheet;

    console.log('runnng payment validation')

    // banner error handling
    $('input').on('click', function (e) {
        image_limit = $("input[name='bannerOptions']:checked").val();
        console.log('Banner count', image_limit)

    });


    $('#stall_banner').change(function () {

        // $('#numberOfFiles').text(this.files.length + " file selected");
        image_count = this.files.length
        console.log("this is image count",image_count)


        if(image_limit < image_count){
            console.log('Image limit exceeded')
            $("#banner_error").show()

        }
        else {
            $("#banner_error").hide()
        }
    });

    // video error hanfling
    $('input').on('click', function (e) {
        video_limit = $("input[name='videoOptions']:checked").val();
        console.log('video count',typeof video_limit)

    });


    $('#stall_video').change(function () {

        $('#numberOfFiles').text(this.files.length + " file selected");
        video_count = this.files.length
        console.log("this is video count",video_count)


        if(video_limit < video_count){
            console.log('Image limit exceeded')
            $("#video_error").show()

        }
        else {
            $("#video_error").hide()

        }
    });

    // do you have a modal
    $('input').on('click', function (e) {
        modal_availability = $("input[name='modalAvailableOptions']:checked").val();
        console.log('modal availability', modal_availability)

        if(modal_availability === "True"){
            console.log("condition True")
            $("#generate_model").hide()
            $("#upload_model").show()

        }
        else if(modal_availability === "False"){
            console.log("condition false")
            $("#generate_model").show()
            $("#upload_model").hide()

        }

        else {
            console.log("not a single option matched")
        }

    });

    // leaflet count
    $('input').on('click', function (e) {
        leaflet_limit = $("input[name='leafletOptions']:checked").val();
        console.log('leaflet limit', leaflet_limit)

    });


    $('#stall_leaflet').change(function () {

        $('#numberOfFiles').text(this.files.length + " file selected");
        leaflet_count = this.files.length
        console.log("this is leaflet count",leaflet_count)

        if(leaflet_count > leaflet_limit){
            console.log('leaflet limit exceeded')
            $("#leaflet_error").show()
        }
        else {
            $("#leaflet_error").hide()

        }



    });

    // do you have a instruction sheet
    $('input').on('click', function (e) {
        info_sheet = $("input[name='informationSheetAvailableOptions']:checked").val();
        console.log('Info sheet availability', info_sheet)

        if(info_sheet === "1"){
            console.log("condition True")
            $("#infoemation_sheet_av").show()

        }
        if(info_sheet === "2"){
            console.log("condition True")
            $("#infoemation_sheet_av").hide()

        }


        else {
            console.log("not a single option matched")
        }

    });


    const purchasing_stall_id = document.getElementById("selected_stall").value
    test_url = '/exhibition/stall_payment/';
    console.log('pay url', test_url)
    console.log("stall_id", purchasing_stall_id)
    const image_tot = image_count
    console.log("total images",image_tot)

    $.ajax({
        url: test_url,
        data: {
            'stall_id': purchasing_stall_id,

        },
        dataType: 'json',
        success: function (data) {
            if (data.OLD_PWD_VALID) {
                // alert("Username already taken");
                $("#acc_pwd_change_old_pwd_alert").hide()
                document.getElementById("from_acc_reset_pwd_btn").disabled = false;




            }
            else {
                $("#acc_pwd_change_old_pwd_alert").show()
                document.getElementById("from_acc_reset_pwd_btn").disabled = true;





            }



        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("some error");
        }



    });













});

$(document).click(function() {
    test_url = '/exhibition/stall_payment/';
    const image_limit_be = $("input[name='bannerOptions']:checked").val();
    const video_limit_be = $("input[name='videoOptions']:checked").val();
    const modal_availability_be = $("input[name='modalAvailableOptions']:checked").val();
    const leaflet_limit_be = $("input[name='leafletOptions']:checked").val();
    const info_sheet_be = $("input[name='informationSheetAvailableOptions']:checked").val();
    const video_con_be = $("input[name='videoConferencingAvailableOptions']:checked").val();

    console.log("to backend image count", image_limit_be)
    $.ajax({
        url: test_url,
        data: {

            'no_of_banners': image_limit_be,
            'no_of_videos': video_limit_be,
            'models':modal_availability_be,
            'pdf':info_sheet_be,
            'no_of_leaflets':leaflet_limit_be,
            'video_con': video_con_be
        },
        dataType: 'json',
        success: function (data) {

            document.getElementById("exhibition_sum_pay").value = data.Total_Cost +".00";
            document.getElementById("banner_payment").value = data.Banner_Cost +".00";
            document.getElementById("video_payment").value = data.VideoCost +".00";
            document.getElementById("leaflet_payment").value = data.LeafletCost +".00";
            document.getElementById("model_payment").value = data.ModelCost +".00";
            document.getElementById("pdf_payment").value = data.PdfCost +".00";
            document.getElementById("vid_conf_payment").value = data.VconCost +".00";

            // // alert("Username already taken");
            // $("#acc_pwd_change_old_pwd_alert").hide()
            // document.getElementById("from_acc_reset_pwd_btn").disabled = false;








        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("some error");
        }



    });

});