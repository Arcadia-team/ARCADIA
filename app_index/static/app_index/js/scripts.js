var old_event = 0;
var palabra = '';
var soloLetras = /^[a-zA-Z]{1}$/;
var ultimaLetra = '';
var contenido = '';
var id = '';

function redirigir(li){
  var variableID = li.id;
  var variableID = variableID.toLowerCase();
  window.location.href = "/games/"+variableID+"/";
}



$(document).ready(function() {
    $(document).on('blur', '.clickedit input', function() {
      var clickedElement = $(this).closest('.clickedit');
      var newValue = $(this).val();
      clickedElement.text(newValue);
      clickedElement.removeClass('editing');
    });
    $(document).on('click', '.clickedit', function(){
      id = event.target.id;
			// Mostramos el ID en la consola del navegador
			console.log("El ID del elemento clickeado es: " + id);
      contenido = $(this).text();

      var input = $('<input>', {
        'type': 'text',
        'value': contenido
      });
      $(this).html(input);
      input.focus();
    });
    $(document).on('keydown', 'input[type="text"]', function(event) {
      console.log(event.which)
      var $campo = $(this).closest('td'); // Obtener la referencia al campo
      
      // Agregar el evento 'blur' al campo
      $campo.on('blur', function() {
        console.log('Se perdió el foco del campo');
      });
      if (event.which == 13) {  // Tecla Enter
        event.preventDefault();
        var nuevoContenido = $(this).val();
        $(this).parent().text(nuevoContenido);
        var fila = $(this).parent().parent(); // Obtener la fila de la tabla
        var valorSeleccionado = $("#selectjuegos").val();
        var csrftoken = Cookies.get('csrftoken');
        $.ajax({
            url: "/adminpanel3/",
            method: "POST",
            data: {
                'val1': nuevoContenido,
                'val2': contenido,
                'id':id,
                'juego':valorSeleccionado,
                'csrfmiddlewaretoken': csrftoken
            },
            dataType: 'json',
            success: function(response){
              $campo.text(response.val); // Cambiar contenido del campo con la respuesta de Django
            }
        });
      } else if (event.which == 27) {  // Tecla Esc

        event.preventDefault();
        $(this).parent().text(contenido);
        var fila = $(this).parent().parent(); // Obtener la fila de la tabla
      }
    });
    

    $('#letra').on('keyup', function(event){
        var contenido = $("#letra").val();
        if ((event.key !== ultimaLetra)  || (event.key == 'Backspace')) {
          if((soloLetras.test(event.key)) || (event.key == 'Backspace')){ //Compruebo si son letras
            if(event.key !== 'Backspace')
            {
              palabra = palabra + event.key;
            }else if(contenido.length == 0)
            {
              palabra = "";
            }else
            {
              palabra = palabra.slice(0, palabra.length - 1); //compruebo si lo que pone el usuario es diferente a la tecla de borrar 
            } 
            ultimaLetra = event.key;
            var csrftoken = Cookies.get('csrftoken');
            $.ajax({
                url: "/inicio2/",
                method: "POST",
                data: {
                    'letra': palabra,
                    'csrfmiddlewaretoken': csrftoken
                },
                dataType: 'json',
                success: function(response) {
                  if(response.length !== 0) {
                    if(palabra.length == 0){$("#mi-lista").hide();}else{$("#mi-lista").show()}
                    $("#mi-lista").addClass("list-group-item");
                    var ul = $('<ul>');
                    for (var i = 0; i < response.length; i++)
                    {
                      var li = $('<li id="'+ response[i][i] +'" '+ 'onclick="redirigir(this)" class="overBuscador"' + ' style="cursor:pointer;margin-top:1em;">').text(response[i][i]);
                      ul.append(li);
                    }
                    $('#mi-lista').empty().append(ul);
                  }
                }
            });
          }
        }  
      });

      // GENERAR TABLA DE RANKING EN EL PANEL DE ADMIN
      $('#selectjuegos').change(function(){
        var csrftoken = Cookies.get('csrftoken');
        var valorSeleccionado = $("#selectjuegos").val();
        $.ajax({
          url: "/adminpanel2/",
          method: "POST",
          data: {
              'selectjuegos': valorSeleccionado,
              'csrfmiddlewaretoken': csrftoken
          },
          dataType: 'json',
          success: function(data){
            $('.tablaInicial').remove();

            var filasResultados = '';
            $contador = 1;
            $.each(data, function(index, resultado) {
              var img_src = "/static/app_index/assets/img/iconodelete.png";
              const fechaOriginal = new Date(resultado.date_played);
              const opciones = { month: 'long', day: 'numeric', year: 'numeric', hour: 'numeric', minute: 'numeric', hour12: true };
              const fechaFormateada = fechaOriginal.toLocaleString('en-US', opciones);

              filasResultados += '<tr><td style="border:3px solid black; background-color:white;"><img src="' + img_src + '" id="botonBorrarTabla"></td><td style="border:3px solid black;  background-color:white;" >'+$contador+'</td><td id="user'+$contador+'" class="clickedit" style="border:3px solid black;  background-color:white;">' + resultado.user_profile__user__username + '</td><td id="score'+$contador+'" class="clickedit" style="border:3px solid black; background-color:white;">' + resultado.score + '</td><td id="dateplayed'+$contador+'" style="border:3px solid black; background-color:white;">' + fechaFormateada + '</td></tr>';
              $contador++;
            });
            $('#tablaGenerada').html(filasResultados);
            }
        });
      });


      $("#tablaGenerada").on("click", "#botonBorrarTabla", function() {
        var fila = $(this).parent().parent(); // Obtener la fila de la tabla

        var val1= fila.find("td:nth-child(1)").text();
        var val2 = fila.find("td:nth-child(3)").text();
        var val3 = fila.find("td:nth-child(4)").text();
        var val4 = fila.find("td:nth-child(5)").text();

        fila.remove(); // Eliminar la fila de la tabla
        var csrftoken = Cookies.get('csrftoken');
        $.ajax({
            url: "/adminpanel2/",
            method: "POST",
            data: {
                'val1': val1,
                'val2': val2,
                'val3': val3,
                'val4': val4,
                'csrfmiddlewaretoken': csrftoken
            },
            dataType: 'json',
            success: function(response) {
              
              
            }
        });
      });

      


  });
  
    
    
    
    

            
