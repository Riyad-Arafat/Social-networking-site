
///////////////////////////////// create new post ///////////////////

$('#creat_post').submit(function (e) {
    e.preventDefault()
    post = $('#post').val()
    if (post !== ""){
        $.ajax({
            url : 'create/post',
            type : 'POST',
            cache: false,
            data:{
                content : $('#post').val(),
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
})


////////////////////////////// Get Comments of post ////////////////////////
$(document).bind('DOMSubtreeModified', function() {
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
                console.log($post.find('#comments').length)
                $data = $.parseHTML(data)
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

$(window).off('scroll').on('scroll',function() {
    if($(window).scrollTop() == $(document).height() - $(window).height()) {
        var $more = $('.page-more-link')
        /// Before loading items /////
        $('.get-more-posts').hide()

        //// Get new items //////
        $.get($($more).attr('href'), $.proxy(function(data) {
            var $data = $($.parseHTML(data))
            var $newMore = $data.find('.page-more-link')
            var $items = $data.find('.post-body')
            var $container = $('#time-line')

            if (!$items.length) {
                   $items = $data.filter('.post-body')
               }
            $container.append($items)

            if (!$newMore.length) {
                   $newMore = $data.filter('.page-more-link')
               }
            if ($newMore.length) {
                $more.replaceWith($newMore)
                $more = $newMore
            }
            else {
                   $more.remove()
            }
            ///// After loading new items ////
            autosize_textarea()
            $('.get-more-posts').show()
            /// count views of posts fun /////
            function countViews(){
                var i, x = $items
                for (i=0 ; i < x.length; i++){
                    $.ajax({
                        url: 'posts/count_views',
                        data: {
                            id: $(x[i]).attr("data-key"),
                        },
                    })
                }
            }
            countViews()

        }))
    }
});