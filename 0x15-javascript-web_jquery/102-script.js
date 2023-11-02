document.addEventListener('DOMContentLoaded', function() {
  $('INPUT#btn_translate').click(function() {
    const languageCode = $('INPUT#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
    
    $.get(apiUrl, { lang: languageCode }, function(data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
