var old_event = 0;
var palabra = '';
var soloLetras = /^[a-zA-Z]{1}$/;
$(document).ready(function() {
    var ultimaLetra = '';
    $('#letra').on('keyup', function(event) {
        
        if ((event.key !== ultimaLetra)  || (event.key == 'Backspace')) {
          if((soloLetras.test(event.key)) || (event.key == 'Backspace')){ //Compruebo si son letras
            if(event.key !== 'Backspace')
            {
              palabra = palabra + event.key;
            }else if(palabra.length == 0)
            {
              console.log('asd')
              palabra = "";
            }else
            {
              palabra = palabra.slice(0, palabra.length - 1); //compruebo si lo que pone el usuario es diferente a la tecla de borrar 
            } 
            
            console.log('OLDEVENT: '+old_event+' el evento: '+event.key.length+' '+ ' Palabra: '+palabra.length);
            
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
                      var li = $('<li>').text(response[i][i]);
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
  
    
    
    
    

            
