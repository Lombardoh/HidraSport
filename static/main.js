const domContainer = document.querySelector('#like_button_container');
ReactDOM.render("test", domContainer);

//navbar JS

$("document").ready(function () {
    $(".menu-icon-toggle").on('click', function () {
        var x = document.getElementById("menu");
        if (x.className === "menu") {
            x.className += " visible";
        } else {
            x.className = "menu";
        }
    })
});

$("document").ready(function () {
    $(".menu-icon-toggle-x").on('click', function () {
        var x = document.getElementById("menu");
        var y = document.getElementsByClassName("submenu-cols");
        
        x.className = "menu";
        
        for(var i=0; y.length; i++)
            y[i].className = "submenu-cols";
        
    })
});

$("document").ready(function () {
    $(".arrow").on('click', function () {
        var y = this.id.split(" ");
        y = y[0] + "-submenu-cols";
        
        var x = document.getElementById(y);
        console.log(x);
        if (x.className === "submenu-cols") {
            x.className += " visible";
        } else {
            x.className = "submenu-cols";
        }
    })
});


//article detail talles and button

$("document").ready(function () {

    $('.talle-button').on('click', function () {
        const x = document.getElementsByClassName('talle-button');
        for(var i=0; i<x.length; i++){
            x[i].className="talle-button";
        }
        
        this.className+=" selected";

        
    })
});

$("document").ready(function(){
    $('#buy-link').on('click', function(){
        const talle = document.getElementsByClassName('selected');
        document.getElementById('buy-link').href += $(talle[0]).text();
    })
});

//article detail talles and button imgs 

$("document").ready(function () {
    $.each($(".big-imgs img"), function (index, value) {
        var num = index + 1;
        $(value).attr("data-attrib", "productImg" + num);
    });
    const x = document.getElementsByClassName('talle-button');
    x[0].className+= " selected";
    $('[data-attrib = productImg1]').addClass('active');
});

$("document").ready(function () {
    $.each($(".small-imgs img"), function (index, value) {
        var num = index + 1;
        $(value).attr("data-attrib", "productImg" + num);
    });
});

$(document).ready(function () {
    $('.small-imgs img').on('click', function () {
        var imgNumber = $(this).attr('data-attrib');

        $('.active').removeClass('active');
        $('[data-attrib = ' + imgNumber + ']').addClass('active');
        //      $(this).addClass('active');
    });
});

// Fancier version https://gist.github.com/985283 admin filter collapse

$(document).ready(function ($) {
    ListFilterCollapsePrototype = {
        bindToggle: function () {
            var that = this;
            this.$filterEl.click(function () {
                that.$filterList.slideToggle();
            });
        },
        init: function (filterEl) {
            this.$filterEl = $(filterEl).css('cursor', 'pointer');
            this.$filterList = this.$filterEl.next('ul').hide();
            this.bindToggle();
        }
    }

    function ListFilterCollapse(filterEl) {
        this.init(filterEl);
    }
    ListFilterCollapse.prototype = ListFilterCollapsePrototype;

    $(document).ready(function () {
        $('#changelist-filter').children('h3').each(function () {
            var collapser = new ListFilterCollapse(this);
        });
    });
})
