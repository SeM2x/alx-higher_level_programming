$(document).ready(function () {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            $('DIV#character').html(data.name);
        },
        error: function (xhr, status, error) {
            console.error('There was a problem with the ajax request:', error);
        }
    });
});
