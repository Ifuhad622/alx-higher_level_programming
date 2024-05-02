// Add class red to <header> HTML tag to red after clicking
// <DIV#red_header> using JQuery API

$('DIV#red_header').click(function () {
  $('header').addClass('red');
});
