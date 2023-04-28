var old_event = 0;
var palabra = '';
var soloLetras = /^[a-zA-Z]{1}$/;
var ultimaLetra = '';

function redirigir(li){
  var variableID = li.id;
  var variableID = variableID.toLowerCase();
  window.location.href = "/games/"+variableID+"/";
}



$(document).ready(function() {

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
              //var img_src = "{% static 'app_index/assets/img/iconodelete.png'%}";
              var img_src = "/static/app_index/assets/img/iconodelete.png";

              filasResultados += '<tr><td><img src="' + img_src + '" id="botonBorrarTabla"></td><td>'+$contador+'</td><td>' + resultado.user_profile__user__username + '</td><td>' + resultado.score + '</td><td>' + resultado.date_played + '</td></tr>';
              $contador++;
            });
            $('#tablaGenerada').html(filasResultados);
            }
        });
      });
      $("#tablaGenerada").on("click", "#botonBorrarTabla", function() {
        var fila = $(this).parent().parent(); // Obtener la fila de la tabla
        var valores = {
          num: fila.find("td:nth-child(1)").text(),
          user: fila.find("td:nth-child(3)").text(),
          score: fila.find("td:nth-child(4)").text(),
          fecha: fila.find("td:nth-child(5)").text()
        }; // Obtener los valores de cada celda de la fila
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
                'valores': valores,
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
  
    
    
    
    

            
