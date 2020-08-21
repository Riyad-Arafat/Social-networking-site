function autosize_textarea() {
    $("textarea").on("input", function() {
        var e = this;
        setTimeout(function() {
            e.style.cssText += "height:auto;", e.style.cssText += "margin:0px;", e.style.cssText += "height:" + e.scrollHeight + "px"
        }, 0)
    })
}

function countViews(e) {
    var t;
    for (t = 0; t < e.length; t++) $.ajax({
        url: $count_views,
        data: {
            id: $(e[t]).attr("data-key")
        }
    })
}

function max_height(e) {
    for (var t = 0; t < e.length; t++) $(e[t]).height() > 260 && ($(e[t]).css("height", "130px"), $(e[t]).offsetParent().find(".load-more").show())
}

function read_more() {
    var e = $(".load-more");
    $(e).on("click", function(e) {
        e.preventDefault();
        var t = e.target,
            o = $(t).offsetParent().find(".post-content");
        $(o).css("height", "unset"), $(t).hide()
    })
}
var C_POST = document.getElementById("post"),
    Photo = $("#add-photo");
C_POST && Photo && (C_POST.onfocus = function() {
    var e = document.getElementById("ov"),
        t = t = document.getElementsByTagName("header")[0],
        o = document.getElementById("post-m");
    e.classList.add("op1"), t.style.zIndex = 30, o.classList.add("pm")
}, $("#add-photo").click(function() {
    var e = document.getElementById("ov"),
        t = t = document.getElementsByTagName("header")[0],
        o = document.getElementById("post-m");
    e.classList.add("op1"), t.style.zIndex = 30, o.classList.add("pm")
}), window.onclick = function(e) {
    var t = $(".btn-post");
    if (e.target === ov || e.target === t[0]) {
        var o = document.getElementById("ov"),
            n = n = document.getElementsByTagName("header")[0],
            s = document.getElementById("post-m");
        o.classList.remove("op1"), n.style.zIndex = 1030, s.classList.remove("pm")
    }
}), $(document).ready(function() {
    read_more(), autosize_textarea(), countViews($(".post-body")), $(window).width() < 992 && $(".navbar-collapse").show()
}), $(window).resize(function() {
    $(window).width() < 992 && $(".navbar-collapse").show()
}), $("#post").keyup(function() {
    $("#post-count").text($(this).val().length + "/500")
});
var swiper = new Swiper(".swiper-tags", {
    slidesPerView: 4,
    spaceBetween: 30,
    freemode: !0,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
    }
});