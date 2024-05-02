// Toggles <header> HTML tag class when user clicks
// DIV#toggle_header using jQuery API

$('DIV#toggle_header').click(function () {
  $('header').toggleClass('green red');
});
