$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.ajax({
        url,
        method: 'GET',
        success: function(data) {
            $('DIV#character').text(data.name);
        },
    });
});
