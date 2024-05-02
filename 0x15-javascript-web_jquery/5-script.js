// Adds <li> element to list when DIV#add_item tag is clicked,
// added to UL.my_list using jQuery API

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
