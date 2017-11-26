
$('.click').mouseenter(function () {
    $('#poppy').effect("bounce", {
        times: 1
    }, 200);
    $('.overlay').show();
});

$('.hover').mouseleave(function () {
    $('#poppy').hide();
    $('.overlay').hide();
});
