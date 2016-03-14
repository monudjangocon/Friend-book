{"changed":true,"filter":false,"title":"urls.py","tooltip":"/friend/urls.py","value":"\nfrom django.conf.urls import url\nfrom django.contrib import admin\n\nurlpatterns = [\n    url(r'^admin/', admin.site.urls),\n    url(r'^signup/', 'prof.views.signup'),\n    url(r'^$', 'prof.views.Cover'),\n    url(r'^log_out/$','prof.views.log_out',name=\"log_out\"),\n    url(r'^notifications/$', 'notify.views.notifications', name='notifications'),\n    url(r'^notifications/last/$', 'notify.views.last_notifications', name='last_notifications'),\n      \n    url(r'^notifications/check/$', 'notify.views.check_notifications', name='check_notifications'),\n    url(r'^feeds/', include('feeds.urls')),\n]\n","undoManager":{"mark":95,"position":100,"stack":[[{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"remove","lines":["U"],"id":47}],[{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":["u"],"id":48}],[{"start":{"row":21,"column":42},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":42},"action":"insert","lines":["url(r'^signup/', 'prof.views.signup'),"],"id":50}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["p"],"id":51}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"remove","lines":["u"],"id":52}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"remove","lines":["n"],"id":53}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"remove","lines":["g"],"id":54}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"remove","lines":["i"],"id":55}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"remove","lines":["s"],"id":56}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["$"],"id":57}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"remove","lines":["/"],"id":58}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"remove","lines":["p"],"id":59}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["u"],"id":60}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":["n"],"id":61}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["g"],"id":62}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["i"],"id":63}],[{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"remove","lines":["s"],"id":64}],[{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"insert","lines":["c"],"id":65}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["o"],"id":66}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["v"],"id":67}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["e"],"id":68}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["r"],"id":69}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["r"],"id":70}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":["e"],"id":71}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["v"],"id":72}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["o"],"id":73}],[{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"remove","lines":["c"],"id":74}],[{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"insert","lines":["C"],"id":75}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["O"],"id":76}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["v"],"id":77}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["e"],"id":78}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["r"],"id":79}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["r"],"id":80}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":["e"],"id":81}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["v"],"id":82}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["O"],"id":83}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["o"],"id":84}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["v"],"id":85}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["e"],"id":86}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["r"],"id":87}],[{"start":{"row":22,"column":35},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":88},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":31,"column":43},"action":"insert","lines":["url(r'^register/$','auth.views.register',name=\"register\"),","    url(r'^log_out/$','core.views.log_out',name=\"log_out\"),","    url(r'^admin/', include(admin.site.urls)),","    url(r'^notifications/$', 'active.views.notifications', name='notifications'),","    url(r'^notifications/last/$', 'active.views.last_notifications', name='last_notifications'),","      ","    #url(r'^articles/', include('articles.urls')), ","    url(r'^notifications/check/$', 'active.views.check_notifications', name='check_notifications'),","    url(r'^feeds/', include('feeds.urls')),"],"id":89}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":62},"action":"remove","lines":["url(r'^register/$','auth.views.register',name=\"register\"),"],"id":90}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "],"id":91}],[{"start":{"row":22,"column":35},"end":{"row":23,"column":0},"action":"remove","lines":["",""],"id":92}],[{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"remove","lines":["e"],"id":93}],[{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"remove","lines":["r"],"id":94}],[{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"remove","lines":["o"],"id":95}],[{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"remove","lines":["c"],"id":96}],[{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["p"],"id":97}],[{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"insert","lines":["r"],"id":98}],[{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"insert","lines":["o"],"id":99}],[{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"insert","lines":["f"],"id":100}],[{"start":{"row":25,"column":35},"end":{"row":25,"column":36},"action":"remove","lines":["e"],"id":101}],[{"start":{"row":25,"column":34},"end":{"row":25,"column":35},"action":"remove","lines":["v"],"id":102}],[{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"remove","lines":["i"],"id":103}],[{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"remove","lines":["t"],"id":104}],[{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"remove","lines":["c"],"id":105}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"remove","lines":["a"],"id":106}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["n"],"id":107}],[{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["o"],"id":108}],[{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":["t"],"id":109}],[{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":["i"],"id":110}],[{"start":{"row":25,"column":34},"end":{"row":25,"column":35},"action":"insert","lines":["f"],"id":111}],[{"start":{"row":25,"column":35},"end":{"row":25,"column":36},"action":"insert","lines":["y"],"id":112}],[{"start":{"row":26,"column":40},"end":{"row":26,"column":41},"action":"remove","lines":["e"],"id":113}],[{"start":{"row":26,"column":39},"end":{"row":26,"column":40},"action":"remove","lines":["v"],"id":114}],[{"start":{"row":26,"column":38},"end":{"row":26,"column":39},"action":"remove","lines":["i"],"id":115}],[{"start":{"row":26,"column":37},"end":{"row":26,"column":38},"action":"remove","lines":["t"],"id":116}],[{"start":{"row":26,"column":36},"end":{"row":26,"column":37},"action":"remove","lines":["c"],"id":117}],[{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"remove","lines":["a"],"id":118}],[{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"insert","lines":["n"],"id":119}],[{"start":{"row":26,"column":36},"end":{"row":26,"column":37},"action":"insert","lines":["o"],"id":120}],[{"start":{"row":26,"column":37},"end":{"row":26,"column":38},"action":"insert","lines":["t"],"id":121}],[{"start":{"row":26,"column":38},"end":{"row":26,"column":39},"action":"insert","lines":["i"],"id":122}],[{"start":{"row":26,"column":39},"end":{"row":26,"column":40},"action":"insert","lines":["f"],"id":123}],[{"start":{"row":26,"column":40},"end":{"row":26,"column":41},"action":"insert","lines":["y"],"id":124}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":50},"action":"remove","lines":["#url(r'^articles/', include('articles.urls')),"],"id":125}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "],"id":126}],[{"start":{"row":27,"column":6},"end":{"row":28,"column":1},"action":"remove","lines":[""," "],"id":127}],[{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"remove","lines":["e"],"id":128}],[{"start":{"row":28,"column":40},"end":{"row":28,"column":41},"action":"remove","lines":["v"],"id":129}],[{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"remove","lines":["i"],"id":130}],[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"remove","lines":["t"],"id":131}],[{"start":{"row":28,"column":37},"end":{"row":28,"column":38},"action":"remove","lines":["c"],"id":132}],[{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"remove","lines":["a"],"id":133}],[{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"insert","lines":["n"],"id":134}],[{"start":{"row":28,"column":37},"end":{"row":28,"column":38},"action":"insert","lines":["o"],"id":135}],[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":["t"],"id":136}],[{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"insert","lines":["i"],"id":137}],[{"start":{"row":28,"column":40},"end":{"row":28,"column":41},"action":"insert","lines":["f"],"id":138}],[{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"insert","lines":["y"],"id":139}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":46},"action":"remove","lines":["url(r'^admin/', include(admin.site.urls)),"],"id":140}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":141}],[{"start":{"row":23,"column":59},"end":{"row":24,"column":0},"action":"remove","lines":["",""],"id":142}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":68},"action":"remove","lines":["\"\"\"friend_book URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.9/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Add an import:  from blog import urls as blog_urls","    2. Import the include() function: from django.conf.urls import url, include","    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))"],"id":143}],[{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["\""],"id":144}],[{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["\""],"id":145}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["\""],"id":146}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":147}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1456856886074}