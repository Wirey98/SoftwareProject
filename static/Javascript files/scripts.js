//https://www.youtube.com/watch?v=mISFEwojJmE - adding functionality to a form using AJAX

// signup functionality
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
        window.location.href = "/homepage";
        },
        error: function (resp){
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    event.preventDefault();
});


// login functionality
$("form[name=login_form").submit(function(event){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
        window.location.href = "/homepage";
        },
        error: function (resp){
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    event.preventDefault();
});


// forum functionality
$("form[name=forum_form").submit(function(event){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/forum/post",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
        window.location.href = "/forumResult";
            
        },
        error: function (resp){
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    event.preventDefault();
});