// Fetches from URL and displays hello value in DIV#hello
// HTML tag using jQuery API (imports from <head> tag

$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
