{"filter":false,"title":"decorators.py","tooltip":"/friend_book/decorators.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":15},"action":"insert","lines":["from django.http import HttpResponseBadRequest, HttpResponseRedirect","from functools import wraps","","def ajax_required(f):","    def wrap(request, *args, **kwargs):","        if not request.is_ajax():","            return HttpResponseBadRequest()","        return f(request, *args, **kwargs)","    wrap.__doc__=f.__doc__","    wrap.__name__=f.__name__","    return wrap"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":15},"end":{"row":10,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1456854281988,"hash":"c3974dc3ac0add7f71a48a82646042f723ca1f71"}