/////////////// main functions //////////////////

function autosize_textarea() {
    $('textarea').on('input',function autosize() {
        var el = this;
        setTimeout(function(){
            el.style.cssText = 'height:auto;';
            el.style.cssText = 'margin:0px;';
            el.style.cssText = 'height:' + el.scrollHeight + 'px';

            },0
        );
    })

}

function countViews(){
    var i, x = document.querySelectorAll(".post-body");
    for (i=0 ; i < x.length; i++){
        $.ajax({
            url: 'posts/count_views',
            data: {
                id: $(x[i]).attr("data-key"),
            },
        })
    }
}








// CREAT POST MODEL

var C_POST = document.getElementById("post");
if  (C_POST){
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
}




/////////////////////////////////// count views of post ////////////////////////
$(document).ready(function () {
    autosize_textarea()
    countViews();

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