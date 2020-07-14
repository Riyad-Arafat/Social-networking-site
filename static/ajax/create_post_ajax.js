
///////////////////////////////// create new post ///////////////////

$('#creat_post').submit(function (e) {
    e.preventDefault()

    var $content = $('#post').val()
    var $post = '<p dir="auto">' + $content.replace(/\n/g, "</p>\n<p dir='auto' >") + '</p>';

    if ($content !== "" && $content !== ' '){
        $.ajax({
            url : 'create/post',
            type : 'POST',
            cache: false,
            data:{
                content : $post,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),

            },
            success: function (data,status,xhr) {
                x = $('body').load('')
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


////////////////////////////// Get Comments of post ////////////////////////
$(document).bind('DOMSubtreeModified', function() {
    autosize_textarea()
    $('.comment-btn').off('click').on('click',function (e) {
        e.preventDefault()
        var $x = e.target;
        var $post = $($x).offsetParent().offsetParent()
        $.ajax({
            url: 'get/comments',
            type: 'GET',
            cache: false,
            data: {
                post: $post.attr("data-key"),
            },
            success: function (data, status, xhr) {
                if ($post.find('#comments').length > 0){
                    $post.find('#comments').remove()
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
        var $post = $($x).offsetParent().offsetParent()

        $.ajax({
            url: 'post/like',
            type: 'GET',
            cache: false,
            data: {
                post: $post.attr("data-key"),
            },
            success: function (data, status, xhr) {
                $data = $.parseHTML(data)
                $s = $data[1]
                $post.find('.stat').replaceWith($($data).find('.stat'))

                $audio.play()

            },
            error: function (data, status, xhr) {

            },
        }).done(function () {
            if( $post.find(".like-btn").hasClass('active')){
                $post.find(".like-btn").removeClass('active');

            }else {

                $post.find(".like-btn").addClass('active');
            }
        })

    })
})



/////////////////////////////////// create new comment ///////////////////////////////////
$(document).bind('DOMSubtreeModified', function(){
    $('.comments-area' ).off('submit').on("submit",function (e) {
        e.preventDefault()
        var $x = e.target;
        var $post = $($x).offsetParent().attr('data-key');
        var $comment = $($x).children('#content');

        var $new_comment = $($x).offsetParent().find(".comments")

        if ($comment.val() !== "" ){
            $.ajax({
                url : 'create/comment',
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

var infinite = new Waypoint.Infinite({
    element: $('#time-line'),
    items: '.post',
    more: '.page-more-link',
    onBeforePageLoad: function () {
        $('.get-more-posts').hide();
        $('.loading').show();
    },
    onAfterPageLoad: function ($items) {
         max_height($items.find('.post-content'));
         read_more();
         autosize_textarea();
         $('.get-more-posts').show();
         $('.loading').hide();
         /// count views of posts fun /////
        countViews($($items).find('.post-body'));
    }
});





////////////////////////////////// Loading posts in time line when scroll down ///////////////////////////////




///////////////////// follow profile ////////////////

$(document).ready(function () {
    $('.follow-btn').off('click').on('click',function (e) {
        e.preventDefault()
        var $x = e.target;

        var $id = $($x).attr('data-key')

        $.ajax({
            url : 'follow/profile',
            type: 'Get',
            cache: false,
            data : {
                id : $id

            },
            success: function () {

                if ( $($x).val() ==='Follow'){
                    $($x).val('Unfollow');
                }
                else {
                    $($x).val('Follow');
                }


            }
        })
    })

})

