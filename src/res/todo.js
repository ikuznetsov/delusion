$(document).ready(function() {
                 $('<div>', {'class': 'todo',
                   html: "<div id='watch'></div>"+
                         "<div class='tasks'></div>"
                  }).appendTo('body');
                  
                 $.getJSON('todo.json', function(json) {
                  var items = []
                  $.each(json, function(key, val) {
                   items.push('<input class="task" type="text" value="'+val[0]+'. '+val[1]+'"/><br/>');
                  });
                  $('<div>', {'class': 'tasks_list',
                   html: items.join('')
                  }).appendTo('.tasks');
                 });                                    
                }); 