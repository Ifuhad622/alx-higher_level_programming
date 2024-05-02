// Fetches and replaces character name of URL
// of the character in the DIV#character tag text

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
