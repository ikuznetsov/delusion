$(document).ready(function() {
                 $.getJSON('filemanager.json', function(json) {
                  var items = []
                  $.each(json, function(key, val) {
                   items.push('<a href="xdg:' + val[1] + '"><img src="images/folder.png">&nbsp;'+ val[0]+'</a>');
                  });
                  $('<div>', {'class': 'filemanager',
                   html: items.join('')
                  }).appendTo('body');
                 });
                $(".filemanger").prepend("<h1>My home</h1>");
                }); 