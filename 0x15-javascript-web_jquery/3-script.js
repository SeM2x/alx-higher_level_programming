$(document).ready(function () {
    $('#red_header').click(function (e) {
        e.preventDefault();
        $('header').addClass('red');
    });
});
