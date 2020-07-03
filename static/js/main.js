// CREAT POST MODEL

var C_POST = document.getElementById("post");

C_POST.onfocus =function(){
    var x = document.getElementById("ov"),
        nav = nav = document.getElementsByTagName("header")[0],
        y = document.getElementById('post-m');
    x.classList.add("op1");
    nav.style.zIndex = 30;
    y.classList.add('pm')


};

window.onclick = function(event) {
    if (event.target == ov) {
        var x = document.getElementById("ov"),
            nav = nav = document.getElementsByTagName("header")[0],
            y = document.getElementById('post-m');
        x.classList.remove("op1");
        nav.style.zIndex = 1030;
        y.classList.remove('pm');

    }
};



$(document).ready(function () {
    $('textarea').autoResize();
})






// COMMUNITY TAGS PAGE 



  var swiper = new Swiper('.swiper-tags', {
    slidesPerView: 5,
    freemode: true,
    centeredSlides: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
});