function notify(type, msg) {
  noty({
    text: msg || 'Notificación',
    theme: 'relax',
    type: 'success',
    layout: 'bottomRight',
    timeout: 2000,
  });
}

function errorMsg(msg) {
  notify('error', msg || 'Ocurrió un error');
}
$(function() {

  $('#film-rating').on('rating.change', function(event, value, caption) {
    var idFilm = $('#film_id').val();
    console.log('CHANGED!');
    console.log(value);
    $.ajax({
      url: '/update_rating',
      type: 'POST',
      data: {
        rating: value,
        film: idFilm
      },
      error: function(error) {
        console.error('ERROR');
        console.error(error);
      },
      success: function(resultado) {
        console.log(resultado);
        if( resultado != "OK" ) errorMsg('Error guardando calificación');
        else {
          console.log('ACTUALIZADO CON EXITO');
          notify('success', 'Calificación guardada');
        }
      }
    });
  });
});