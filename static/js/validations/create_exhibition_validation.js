$(document).ready(function() {
    $("#create_exhibition_form").validate(
        {
            errorClass: 'errors',
            rules: {
                exhibition_name_create : {
                    required: true,
                },
                exhibition_type : {
                    required: true,
                },
                exhibition_start_date: {
                    required: true,
                },
                exhibition_end_date: {
                    required: true,
                },
                exhibition_amount: {
                    required: true,

                },
            },
            messages : {
                exhibition_name_create: {
                    required: "*Please provide a name for a exhibition",
                },
                exhibition_type: {
                    required: "*Please provide a exhibition category",
                },
                exhibition_start_date: {
                    required: "*Please provide exhibition start date ",
                },
                exhibition_end_date: {
                    required: "*Please provide exhibition end date ",
                },
                exhibition_amount: {
                    required: "*Please provide ticket amount ",

                },

            }
        }
    );
});