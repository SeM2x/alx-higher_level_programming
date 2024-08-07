$(document).ready(function () {
    $('DIV#red_header').click(function (e) {
        e.preventDefault();
        $('header').addClass('red');
    });
});
