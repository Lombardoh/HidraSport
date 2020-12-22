
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

$(document).ready(function($){
ListFilterCollapsePrototype = {
    bindToggle: function(){
        var that = this;
        this.$filterEl.click(function(){
            that.$filterList.slideToggle();
        });
    },
    init: function(filterEl) {
        this.$filterEl = $(filterEl).css('cursor', 'pointer');
        this.$filterList = this.$filterEl.next('ul').hide();
        this.bindToggle();
    }
}
function ListFilterCollapse(filterEl) {
    this.init(filterEl);
}
ListFilterCollapse.prototype = ListFilterCollapsePrototype;

$(document).ready(function(){
    $('#changelist-filter').children('h3').each(function(){
        var collapser = new ListFilterCollapse(this);
    });
});
})