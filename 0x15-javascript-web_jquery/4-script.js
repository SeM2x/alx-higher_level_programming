$(document).ready(function () {
    $('DIV#toggle_header').click(function (e) {
        e.preventDefault();
        if ($('header').hasClass('red')) {
            $('header').removeClass('red');
            $('header').addClass('green');
        } else {
            $('header').removeClass('green');
            $('header').addClass('red');
        }
    });
});
