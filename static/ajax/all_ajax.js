///////////////////////////////// create new post ///////////////////

$('#creat_post').off('submit').on('submit',function (e) {
    e.preventDefault()
    var $community = $('#community');
    var $cid;
    if ($community.length > 0 ){
        $cid = $($community).attr('data-key')
    }else {
        $cid = 'none';
    }
    var $content = $('#post').val();
    var $file =  $('#id_image')[0].files[0];
    var $postContent = '<p dir="auto">' + $content.replace(/\n/g, "</p>\n<p dir='auto' >") + '</p>';
    var $data = new FormData();
    $data.append("content", $postContent);
    $data.append("csrfmiddlewaretoken", $("input[name='csrfmiddlewaretoken']").val());
    $data.append("image", $file);
    $data.append('community', $cid)



    if ($content !== "" && $content !== ' '){
        $.ajax({
            url : $creat_post,
            type : 'POST',
            cache: false,
            contentType: false,
            processData: false,
            data: $data,

            success: function (data,status,xhr) {
                $('#post').val(null)
                $("#ss").attr('src', '')
                $("#ss").hide()
                $('#post').css('height' , 'unset')
                var $new_post = $.parseHTML(data)
                $('#time-line').prepend($new_post)
                $audio.play();
            },
            error: function (data,status,xhr) {
            }
        })
    }
    else{
        alert('Plz write post')
    }
})



////////////////// Remove post ////////////////////

$(document).bind('DOMSubtreeModified', function () {
    $('.post-options').off('click').on('click', function (e) {
        e.preventDefault();
        var  $i = $(e.target)[0];
        if ($($i).is('.icofont-toggle-off')){

            $($i).removeClass('icofont-toggle-off')
            $($i).addClass('icofont-toggle-on')
            $($i).css('color','#007bff')

        }else {
            $($i).removeClass('icofont-toggle-on')
            $($i).addClass('icofont-toggle-off')
            $($i).css('color','unset')
        }


    })

})


$(document).bind('DOMSubtreeModified', function () {
    $('.remove-post').off('click').on('click', function (e) {
        e.preventDefault();
        var  $i = $(e.target)[0];

        $.ajax({
            url: $remove_post,
            type: 'Post',
            cache: false,
            data: {
                post: $($i).attr("data-key"),
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),

            },
            success: function (data, status, xhr) {
                var $post = $($i).parents('.post')
                $($post).replaceWith('<div style="width: 500px" class="m-auto alert alert-success" ><p>The Post is Removed</p></div>')
            },
            error: function (data, status, xhr) {
                console.log(status)


            },
        })




    })

})



$(window).on('click', function () {

    var  $i = $('.post-options');
    if ($($i).is('.icofont-toggle-on')){

        $($i).removeClass('icofont-toggle-on');
        $($i).addClass('icofont-toggle-off');
        $($i).css('color','unset')
    }


})







////////////////////////////// Get Comments of post ////////////////////////
$(document).bind('DOMSubtreeModified', function() {
    autosize_textarea()
    $('.comment-btn').off('click').on('click',function (e) {
        e.preventDefault()
        var $x = e.target;
        var $post = $($x).parents('.post-body')

        $.ajax({
            url: $get_comments,
            type: 'GET',
            cache: false,
            data: {
                post: $($post).attr("data-key"),
            },
            success: function (data, status, xhr) {
                if ($($post).find('#comments').length > 0){
                    $($post).find('#comments').remove()
                }else {
                    $post.append(data)
                }
            },
            error: function (data, status, xhr) {

            },
        })


    })
})


/////////////////// like button ////////////////////////
$(document).bind('DOMSubtreeModified', function() {
    $('.like-btn').off('click').on('click',function (e) {
        e.preventDefault()
        var $x = e.target;
        var $post = $($x).parents(".post-body")

        $.ajax({
            url: $like_btn,
            type: 'GET',
            cache: false,
            data: {
                post: $post.attr("data-key"),
            },
            success: function (data, status, xhr) {
                $data = $.parseHTML(data)
                $s = $data[1]
                $($post).find('.stat').replaceWith($($data).find('.stat'))
                $audio.play()

            },
            error: function (data, status, xhr) {

            },
        }).done(function () {
            if( $($post).find(".like-btn").hasClass('active')){
                $($post).find(".like-btn").removeClass('active');

            }else {

                $($post).find(".like-btn").addClass('active');
            }
        })

    })
})



/////////////////////////////////// create new comment ///////////////////////////////////
$(document).bind('DOMSubtreeModified', function(){
    $('.comments-area' ).off('submit').on("submit",function (e) {
        e.preventDefault()
        var $x = e.target;
        var $post = $($x).parents('.post-body').attr('data-key');
        var $comment = $($x).children('#content');

        var $new_comment = $($x).offsetParent().find(".comments")

        if ($comment.val() !== "" ){
            $.ajax({
                url : $creat_comment,
                type : 'POST',
                cache: false,
                data :{
                    content : $comment.val(),
                    post : $post,
                    csrfmiddlewaretoken : $("input[name='csrfmiddlewaretoken']").val(),
                },
                success: function (data,status,xhr){

                    $comment.val(null)
                    $($comment).css('height' , 'unset')
                    $data= $.parseHTML(data);
                    $($data).prependTo($new_comment)
                    $audio.play();
                },
                error: function (data,status,xhr) {
                    alert("Sorry there is Error , Try again")
                },
            })
        }else {
            alert("you must write a comment ")
        }
    })
})







////////////////////////////////// Loading posts in time line when scroll down ///////////////////////////////

var infinite = new Waypoint.Infinite({
    element: $('#time-line')[0],
    items: '.post',
    more: '.page-more-link',
    onBeforePageLoad: function () {
        $('.loading').show();
    },
    onAfterPageLoad: function ($items) {
        read_more();
        autosize_textarea();
        $('.loading').hide();
        /// count views of posts fun /////
        countViews($($items).find('.post-body'));


    }
});


///////////////////// follow profile ////////////////

$(document).ready(function () {
    $('.follow-btn').off('click').on('click', function (e) {
        e.preventDefault()
        var $x = e.target;
        var $id = $($x).attr('data-key')

        $.ajax({
            url: $follow,
            type: 'Get',
            cache: false,
            data: {
                id: $id

            },
            success: function () {
                $audio.play();
                if ($($x).val() === 'Follow') {
                    $($x).val('Unfollow');
                    $($x).removeClass('btn-primary').addClass('btn-outline-primary')

                } else {
                    $($x).val('Follow');
                    $($x).removeClass('btn-outline-primary').addClass('btn-primary')

                }


            }
        })
    })
})


////// Get Notifications //////////////////

$(document).ready(function () {
    $.ajax({
        url: $get_notifications,
        type: 'Get',
        cache: false,
        success: function (data, status, xhr) {
            $('#notifications-area').append(data);
            var $n = $('.note');

            if( $n.is('.false')){
                $('#notifications').css('color', '#ff0000')
            }
        }
    })
    function note() {
        $.ajax({
            url: $get_notifications,
            type: 'Get',
            cache: false,
            success: function (data, status, xhr) {
                $('#notifications-area').append(data);
                var $n = $('.note');

                if ($n.is('.false')) {
                    $('#notifications').css('color', '#ff0000')
                }


            }
        })
    }
    setInterval(function(){
      note();
    }, 15000)
})




$(document).ready(function () {
    $('#notifications').off('click').on('click', function () {
        $.ajax({
            url: $get_notifications,
            type: 'Get',
            cache: false,
            success: function (data, status, xhr) {
              var $x =   $('#notifications-area').children('.notes')
                $x.replaceWith(data)
                var $n = $('.note');
                if( $n.is('.false')){
                    $('#notifications').css('color', '#ff0000')
                }else{
                    $('#notifications').css('color', 'unset')
                }
            }

        })
    })
})


////// Read Notifications //////////////////

$(document).ready(function () {
    $('#r-note').off('click').on('click', function () {
        $.ajax({
            url: $read_notifications,
            type: 'Get',
            cache: false,
            success: function (data, status, xhr) {
                $('.note').removeClass('false');
                $('#notifications').css('color', 'unset');
            }


        })
    })

})