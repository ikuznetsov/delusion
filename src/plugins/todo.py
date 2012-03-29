# -*- coding: utf-8 -*-
response = """
[["1", "Купить всех"], 
["2", "Купить все"],
["3", "Завоевать мир"]] 
"""

resources = open("res/todo.json","w")
resources.write(response)
resources.close()

js_plugin = """$(document).ready(function() {
                 $('<div>', {'class': 'todo',
                   html: "<div class='watch'>16:28</div>"+
                         "<div class='tasks'></div>"
                  }).appendTo('body');
                  
                 $.getJSON('todo.json', function(json) {
                  var items = []
                  $.each(json, function(key, val) {
                   items.push('<div>'+val[0]+'. '+val[1]+'</div>');
                  });
                  $('<div>', {'class': 'tasks_list',
                   html: items.join('')
                  }).appendTo('.tasks');
                 });                                    
                }); """

resources = open("res/todo.js","w")
resources.write(js_plugin)
resources.close()

plugin_style = """.todo {background: rgba(0,0,0,0.7); margin-top: 500px; padding: 10px 100px;}
                  .todo .watch{font-size: 3em; color: white; border-bottom: 1px solid rgba(255,255,255,0.2); width: 30%; padding: 10px}
                  .todo .tasks {padding: 20px} 
               """

resources = open("res/todo.css","w")
resources.write(plugin_style)
resources.close()
