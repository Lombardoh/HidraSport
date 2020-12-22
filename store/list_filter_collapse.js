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