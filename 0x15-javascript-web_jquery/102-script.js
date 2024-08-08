$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
  $('INPUT#btn_translate').click(function (e) {
    e.preventDefault();
    $.ajax({
      url: url + $('INPUT#language_code').val(),
      method: 'GET',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
