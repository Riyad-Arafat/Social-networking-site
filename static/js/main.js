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

function countViews(x){
    var i;
    for (i=0 ; i < x.length; i++){
        $.ajax({
            url: $count_views,
            data: {
                id: $(x[i]).attr("data-key"),
            },
        })
    }
}

function max_height(post) {
  for (var i=0; i < post.length; i++){
      if($(post[i]).height() > 260){
          $(post[i]).css('height', '130px')
          $(post[i]).offsetParent().find('.load-more').show()

      }

  }
}

function read_more() {
        var $loadMore = $('.load-more');
        $($loadMore).on('click',function (e) {
          e.preventDefault()
          var $x =e.target
          var $content = $($x).offsetParent().find('.post-content')
          $($content).css('height', 'unset')
          $($x).hide()
      })

}








/////////////////// CREAT POST MODEL///////////////

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
    if (event.target === ov) {
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
    var $post = $('.post-content');
    max_height($post);
    read_more()
    autosize_textarea();
    var x = document.querySelectorAll(".post-body")
    countViews(x);


})





//////////////////////////////// COMMUNITY TAGS PAGE

var swiper = new Swiper('.swiper-tags', {
    slidesPerView: 4,
    spaceBetween: 30,
    freemode: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
});