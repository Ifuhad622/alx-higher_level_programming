// Queries an API and fetches all movie titles then inserts them
// into the UL#list_movies tag

let url = 'https://swapi.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  let films = data.results;
  for (let film of films) {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  }
});
