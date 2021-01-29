//https://www.youtube.com/watch?v=mISFEwojJmE - adding functionality to a form using AJAX

$("form[name=signup_form").submit(function(event){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({

        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
        },
        error: function (resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    event.preventDefault();
});