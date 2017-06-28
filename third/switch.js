$(".line-all, .line-opt").click(function() {

    if ($(this).is(".line-all")){
        $(this).siblings(".line-opt").removeClass("und")
        if ($(this).not(".und")) $(this).addClass("und")
    }

else if($(this).siblings().is(".und")) {
    $(this).siblings(".line-all").removeClass("und")
    if ($(this).is(".und")) $(this).removeClass("und")
        else $(this).addClass("und")
    }
});

var min_p = 1400000
var max_p = 3500000

$("#price-slider").roundSlider({
    radius: 70,
    width: 1,
    sliderType: "range",
    min: min_p,
    max: 1.04 * max_p,
    value: min_p + ',' + max_p,
    handleSize: "12",
    tooltipFormat: "tooltipVal"
});


function tooltipVal(args) {
    var n = args.value;
    if (n >= 1000 && n < 1000000){
        var x = Math.round(n / 100)/10
        if(x >= 10) x = Math.round(x)
        return x + " тыс"
    }
    if (n >= 1000000){
        var x = Math.round(n / 100000)/10
        if(x >= 10) x = Math.round(x)
        return x + " млн"
    }
    return n  
}



$(".logo, .brand").hover(function(){
    $(".logo, .brand").css({ opacity: 1 });
})

$(".logo, .brand").mouseover(function(){
    $(".logo, .brand").css({ opacity: .7 });
})