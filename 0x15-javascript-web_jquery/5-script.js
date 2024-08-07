$(document).ready(function () {
    $('DIV#add_item').click(function (e) { 
        e.preventDefault();
        $('UL.my_list').append('<li>Item</li>');
    });
});
