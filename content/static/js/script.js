$(".line-all, .line-opt").click(function() {

    if ($(this).siblings(".line-opt, .line-all").length <= 2) {
        $(this).addClass("und")
        $(this).siblings(".line-opt").removeClass("und")
        $(this).siblings(".line-all").removeClass("und")  
    } else if ($(this).is(".line-all")){
        $(this).siblings(".line-opt").removeClass("und")
        if ($(this).not(".und")) $(this).addClass("und")
    } else if($(this).siblings().is(".und")) {
        $(this).siblings(".line-all").removeClass("und")
        if ($(this).is(".und")) $(this).removeClass("und")
            else $(this).addClass("und")
        }
});


var min_p = 1400000
var max_p = 3500000

var d     = max_p - min_p

$("#price-slider").roundSlider({
    radius: 70,
    width: 1,
    sliderType: "range",
    min: min_p - .05 * d,
    max: max_p + .05 * d,
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

$(".thumb-item").brazzersCarousel();

$('.as-cards').click(function() {
    if ($('.cards').hasClass('lines')) {

        $('.cards').removeClass('lines');
        $('.card').removeClass('card-lin');

        $('.thumb-item').removeClass('thumb-item-lin');
        $('.lin-table').hide()
        $('.prd-props').show()

        $('.card').each(function(){
            $(this).append($(this).find('.prd-price'))
        })

    }
})

var wasAdded = false
$(".as-lines").click(function() {
    if (!$('.cards').hasClass('lines')) {

        $('.cards').addClass('lines');
        $('.card').addClass('card-lin');


        $('.prd-brand-model').each(function(){
            $(this).append($(this).siblings('.prd-price'))
        })

        $('.thumb-item').addClass('thumb-item-lin');

        $('.prd-props').hide()
        $('.lin-table').show()

        if(!wasAdded){
            $('.card').each(function(){
                for (var i = 1; i <= 4; i++) {
                // alert($(this).find('.tr:nth-child(3) .prd-prop-name').text())
                
                $(this).find('.lin-table').append('<tr></tr>');

                var fstPropName = $(this).find('.tr:nth-child(' + i + ') .prd-prop-name').text()
                $(this).find('tr:last-child').append('<td><b>' + fstPropName + '</b></td>');

                var fstProp = $(this).find('.tr:nth-child(' + i + ') .prd-prop').text()
                $(this).find('tr:last-child').append('<td class = "tbl-prop">' + fstProp + '</td>');

                var sndPropName = $(this).find('.tr:nth-child(' + (i + 4)  + ') .prd-prop-name').text()
                $(this).find('tr:last-child').append('<td class = "snd-col"><b>' + sndPropName + '</b></td>');

                var sndProp = $(this).find('.tr:nth-child(' + (i + 4) + ') .prd-prop').text()
                $(this).find('tr:last-child').append('<td class = "tbl-prop">' + sndProp + '</td>');
            }
            wasAdded = true
        })
        }
    }
})


$(".search-by-props").click(function() {
    $.ajax({
      type: "GET",
      dataType: "json"
    });
})