def cookie(request):
    print(request.COOKIES)
    resp = HttpResponse("C is for cookie and that is good enough for me")
    resp.set_cookie('zap', 42) # no expired date = until browser close
    resp.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire
    return resp
