
$(document).ready(function(){
    $('.left-column img:first').addClass('active');
});


//$(document).ready(function() {
//
//  $('.color-choose input').on('click', function() {
//      var headphonesColor = $(this).attr('data-image');
//
//      $('.active').removeClass('active');
//      $('.left-column img[data-image = ' + headphonesColor + ']').addClass('active');
//      $(this).addClass('active');
//  });
//
//});


// Fancier version https://gist.github.com/985283 

console.log("test");

;(function($){ $(document).ready(function(){
    $('#changelist-filter').children('h3').each(function(){
        var $title = $(this);
        $title.click(function(){
            $title.next().slideToggle();
        });
    });   
  });
})(django.jQuery);