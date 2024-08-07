$(document).ready(function () {
  $('DIV#toggle_header').click(function (e) {
    e.preventDefault();
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});
