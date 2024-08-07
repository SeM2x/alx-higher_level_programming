$(document).ready(function () {
    $('DIV#add_item').click(function (e) { 
        e.preventDefault();
        $('UL.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').click(function (e) { 
        e.preventDefault();
        $('UL.my_list li:last-child').remove();
    });
    $('DIV#clear_list').click(function (e) { 
        e.preventDefault();
        $('UL.my_list').empty();
    });
});
