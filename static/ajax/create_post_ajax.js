$(document).ready(function () {
    $('textarea').autoResize();
    $('#creat_post').submit(function (e) {

        e.preventDefault()
        post = $('#post').val()
        if (post !== ""){

            $.ajax({
                url : 'create/post',
                type : 'POST',
                data:{
                    content : $('#post').val(),
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),

                },
                success: function (data,status,xhr) {
                    $("body").load(data);

                },
                error: function () {
                    alert("error")
                    $("body").load(data);
                }
            })




        }
        else{
            alert("Post must have content")
            $("body").load(data);
        }



    })
})


