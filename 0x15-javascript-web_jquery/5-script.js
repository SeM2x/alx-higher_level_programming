$(document).ready(function () {
    $('DIV#add_item').click(function (e) {
        e.preventDefault();
        $('UL.my_list').html($('UL.my_list').html() + '<li>Item</li>');
    });
});
