$(document).ready(function() {
    $("#exhibitor_signup_form").validate(
        {
            errorClass: 'errors',
            rules: {
                exhibitor_company : {
                    required: true,
                },
                exhibitor_address: {
                    required: true,
                },
                exhibitor_contact_number: {
                    required: true,
                    minlength:10,
                    maxlength:10
                },
            },
            messages : {
                exhibitor_company: {
                    required: "*Please provide company name",
                },
                exhibitor_address: {
                    required: "*Please provide company address ",
                },
                exhibitor_contact_number: {
                    required: "*Please provide a contact number ",
                    minlength:"*Please enter a valid phone number",
                    maxlength: "*Mobile number cannot exceed more than 10 characters"
                },

            }
        }
    );
});