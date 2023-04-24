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
      






  });
  
    
    
    
    

            
