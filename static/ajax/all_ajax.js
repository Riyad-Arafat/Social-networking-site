$("#creat_post").off("submit").on("submit", function(e) {
    e.preventDefault(), $("#post-submit").hide(), $(".progress-post").show();
    var t, n = $("#community");
    t = n.length > 0 ? $(n).attr("data-key") : "none";
    var o = $("#post").val(),
        a = $("#id_image")[0].files[0],
        i = '<p dir="auto">' + o.replace(/\n/g, "</p>\n<p dir='auto' >") + "</p>",
        c = new FormData;
    c.append("content", i), c.append("csrfmiddlewaretoken", $("input[name='csrfmiddlewaretoken']").val()), c.append("image", a), c.append("community", t), "" !== o && " " !== o || null != a ? $.ajax({
        url: $creat_post,
        type: "POST",
        cache: !1,
        contentType: !1,
        processData: !1,
        data: c,
        success: function(e, t, n) {
            $("#post").val(null), $("#ss").attr("src", ""), $("#ss").hide(), $("#post").css("height", "unset"), $("#id_image").val("");
            var o = $.parseHTML(e);
            $("#time-line").prepend(o), $audio.play()
        },
        error: function(e, t, n) {
            alert("sorry plz refresh the page and try again")
        },
        complete: function() {
            $("#post-submit").show(), $(".progress-post").hide()
        }
    }) : (alert("plz write a post"), $("#post-submit").show(), $(".progress-post").hide())
}), $(document).bind("DOMSubtreeModified", function() {
    $(".post-options").off("click").on("click", function(e) {
        e.preventDefault();
        var t = $(e.target)[0];
        $(t).is(".icofont-toggle-off") ? ($(t).removeClass("icofont-toggle-off"), $(t).addClass("icofont-toggle-on"), $(t).css("color", "#007bff")) : ($(t).removeClass("icofont-toggle-on"), $(t).addClass("icofont-toggle-off"), $(t).css("color", "unset"))
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".remove-post").off("click").on("click", function(e) {
        e.preventDefault();
        var t = $(e.target)[0];
        $.ajax({
            url: $remove_post,
            type: "Post",
            cache: !1,
            data: {
                post: $(t).attr("data-key"),
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(e, n, o) {
                var a = $(t).parents(".post");
                $(a).replaceWith('<div style="width: 500px" class="m-auto alert alert-success" ><p>The Post is Removed</p></div>')
            },
            error: function(e, t, n) {}
        })
    })
}), $(window).on("click", function() {
    var e = $(".post-options");
    $(e).is(".icofont-toggle-on") && ($(e).removeClass("icofont-toggle-on"), $(e).addClass("icofont-toggle-off"), $(e).css("color", "unset"))
}), $(document).bind("DOMSubtreeModified", function() {
    autosize_textarea(), $(".comment-btn").off("click").on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).parents(".post-body");
        $.ajax({
            url: $get_comments,
            type: "GET",
            cache: !1,
            data: {
                post: $(n).attr("data-key")
            },
            success: function(e, t, o) {
                $(n).find("#comments").length > 0 ? $(n).find("#comments").remove() : n.append(e)
            },
            error: function(e, t, n) {}
        })
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".remove-comment").off("click").on("click", function(e) {
        e.preventDefault();
        var t = $(e.target)[0];
        $.ajax({
            url: $remove_comment,
            type: "Post",
            cache: !1,
            data: {
                comment: $(t).attr("data-key"),
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(e, n, o) {
                $(t).parents(".comment").remove()
            },
            error: function(e, t, n) {
                alert("tray again")
            }
        })
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".like-btn").off("click").on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).parents(".post-body");
        $.ajax({
            url: $like_btn,
            type: "GET",
            cache: !1,
            data: {
                post: n.attr("data-key")
            },
            success: function(e, t, o) {
                $data = $.parseHTML(e), $s = $data[1], $(n).find(".stat").replaceWith($($data).find(".stat")), $audio.play()
            },
            error: function(e, t, n) {}
        }).done(function() {
            $(n).find(".like-btn").hasClass("active") ? $(n).find(".like-btn").removeClass("active") : $(n).find(".like-btn").addClass("active")
        })
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".comments-area").off("submit").on("submit", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).parents(".post-body").attr("data-key"),
            o = $(t).children("#content"),
            a = $(t).offsetParent().find(".comments");
        "" !== o.val() ? $.ajax({
            url: $creat_comment,
            type: "POST",
            cache: !1,
            data: {
                content: o.val(),
                post: n,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(e, t, n) {
                o.val(null), $(o).css("height", "unset"), $data = $.parseHTML(e), $($data).prependTo(a), $audio.play()
            },
            error: function(e, t, n) {
                alert("Sorry there is Error , Try again")
            }
        }) : alert("you must write a comment ")
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".like-comment").off("click").on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).parents(".comment");
        $.ajax({
            url: $like_comment,
            type: "GET",
            cache: !1,
            data: {
                comment: n.attr("data-key")
            },
            success: function(e, t, n) {
                $audio.play()
            },
            error: function(e, t, n) {}
        }).done(function() {
            "Like" === $(t).text() ? $(t).text("unLike") : $(t).text("Like")
        })
    })
}), $(document).bind("DOMSubtreeModified", function() {
    autosize_textarea(), $(".g_rp").off("click").on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).parents(".comment");
        $.ajax({
            url: $get_replies,
            type: "GET",
            cache: !1,
            data: {
                comment: $(n).attr("data-key")
            },
            success: function(e, t, o) {
                $(n).find("#replies").length > 0 ? $(n).find("#replies").remove() : $(n).append(e)
            },
            error: function(e, t, n) {}
        })
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".btn-reply").off("click").on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).parents("#reply_form"),
            o = $(n).children("#content"),
            a = $(t).parents("#replies");
        "" !== o.val() ? $.ajax({
            url: $create_reply,
            type: "POST",
            cache: !1,
            data: {
                content: o.val(),
                comment: n.attr("data-key"),
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(e, t, n) {
                o.val(null), $(o).css("height", "unset"), $(a).append(e), $audio.play()
            },
            error: function(e, t, n) {
                alert("Sorry there is Error , Try again")
            }
        }) : alert("you must write a comment ")
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".remove-reply").off("click").on("click", function(e) {
        e.preventDefault();
        var t = $(e.target)[0];
        $.ajax({
            url: $remove_reply,
            type: "Post",
            cache: !1,
            data: {
                reply: $(t).attr("data-key"),
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(e, n, o) {
                $(t).parents("#reply").remove()
            },
            error: function(e, t, n) {
                alert("tray again")
            }
        })
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".like-reply").off("click").on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).parents("#reply");
        $.ajax({
            url: $like_reply,
            type: "GET",
            cache: !1,
            data: {
                reply: n.attr("data-key")
            },
            success: function(e, t, n) {
                $audio.play()
            },
            error: function(e, t, n) {}
        }).done(function() {
            "Like" === $(t).text() ? $(t).text("unLike") : $(t).text("Like")
        })
    })
});
var infinite = new Waypoint.Infinite({
    element: $("#time-line")[0],
    items: ".post",
    more: ".page-more-link",
    onBeforePageLoad: function() {
        $(".loading").show()
    },
    onAfterPageLoad: function(e) {
        read_more(), autosize_textarea(), $(".loading").hide(), countViews($(e).find(".post-body"))
    }
});
$(document).ready(function() {
    $(".follow-btn").off("click").on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).attr("data-key");
        $.ajax({
            url: $follow,
            type: "Get",
            cache: !1,
            data: {
                id: n
            },
            success: function() {
                $audio.play(), "Follow" === $(t).val() ? ($(t).val("Unfollow"), $(t).removeClass("btn-primary").addClass("btn-outline-primary")) : ($(t).val("Follow"), $(t).removeClass("btn-outline-primary").addClass("btn-primary"))
            }
        })
    })
}), $(document).ready(function() {
    $.ajax({
        url: $get_notifications,
        type: "Get",
        cache: !1,
        success: function(e, t, n) {
            $("#notifications-area").append(e), $(".note").is(".false") && $("#notifications").css("color", "#ff0000")
        }
    }), setInterval(function() {
        $.ajax({
            url: $get_notifications,
            type: "Get",
            cache: !1,
            success: function(e, t, n) {
                var o = $("#notifications-area").children(".notes");
                $(o).replaceWith(e), $(".note").is(".false") && $("#notifications").css("color", "#ff0000")
            }
        })
    }, 15e3)
}), $(document).ready(function() {
    $("#notifications").off("click").on("click", function() {
        $.ajax({
            url: $get_notifications,
            type: "Get",
            cache: !1,
            success: function(e, t, n) {
                $("#notifications-area").children(".notes").replaceWith(e), $(".note").is(".false") ? $("#notifications").css("color", "#ff0000") : $("#notifications").css("color", "unset")
            }
        })
    })
}), $(document).ready(function() {
    $("#r-note").off("click").on("click", function() {
        $.ajax({
            url: $read_notifications,
            type: "Get",
            cache: !1,
            success: function(e, t, n) {
                $(".note").removeClass("false"), $("#notifications").css("color", "unset")
            }
        })
    })
}), $(document).bind("DOMSubtreeModified", function() {
    $(".hash-tag").off("click").on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            n = $(t).text();
        n = n.replace("#", ""), window.location.href = $hash.replace(0, n)
    })
});