$(document).ready(function () {
    $('#creat_post').submit(function (e) {
        e.preventDefault()
        content = $('#post').val()
        if (content !== ""){

            x = $.ajax({
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