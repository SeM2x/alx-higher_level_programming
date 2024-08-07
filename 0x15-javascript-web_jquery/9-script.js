$(document).ready(function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.ajax({
        url,
        method: 'GET',
        success: function(data) {
            $('DIV#hello').text(data.hello);
        },
    });
});
