$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
  function sayHello (e) {
    e.preventDefault();
    $.ajax({
      url: url + $('INPUT#language_code').val(),
      method: 'GET',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }
  $('INPUT#btn_translate').click((e) => sayHello(e));
  $('INPUT#language_code').keypress(function (e) {
    if (e.keyCode === 13) {
      sayHello(e);
    }
  });
});
