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

//alerts

setTimeout(function(){
    if ($('#msg').length>0){
        $('#msg').remove();
    }
},2000)


//cart functions


$("#postal-code, #domicilio, #sucursal").on("propertychange change keyup input paste", function(){
    let costo = 990;
    var code = $("#postal-code").val();
    var entrega = $('input[name="entrega"]:checked').val()
    let total = document.getElementById("products-cost")

    if (code < 1441)
        costo= 450
    else if (code > 1440 && code < 2943 || code > 6399 && code < 8181)
        entrega === "sucursal" ? costo = 750: costo = 950;
    else
        entrega === "sucursal" ? costo = 990: costo = 1499;

    document.getElementById("delivery-cost").innerHTML = costo;

    document.getElementById("total-cost").innerHTML = parseFloat(costo) + parseFloat(total.textContent)

    document.getElementById("payment").href = "http://127.0.0.1:8000/checkout/" + code + "/" + entrega
})

$("document").ready(function () {
    $.each($(".codigo-scanneado"), function (index, value) {
        let num = index + 1;
        $(value).attr("data-attrib", num);
    });

    $.each($(".codigo"), function (index, value) {
        let  num = index + 1;
        $(value).attr("data-attrib", "product" + num);
    });
    $.each($(".table-row"), function (index, value) {
        let  num = index + 1;
        $(value).attr("data-attrib", "row" + num);
    });   
});

$("document").ready(function(){
    "use strict"

    $('.codigo-scanneado').on('propertychange change keyup input paste', function () {
        let codigoScaneado = $(this).val();
        let codigo = document.querySelector('[data-attrib = product' + $(this).attr('data-attrib') + ']').textContent;
        codigo = codigo.replace(/\s/g, '');
        
        if(codigo === codigoScaneado){        
            $('[data-attrib = row1').addClass('green')
        }
    });
});
