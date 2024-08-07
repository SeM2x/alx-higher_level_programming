$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.ajax({
        url,
        method: 'GET',
        success: function(data) {
            data = data.results.map(movie => movie.title);
            data.forEach(title => {
                $('UL#list_movies').append(`<li>${title}</li>`);
            });
        },
    });
});
