def sessfun(request):
    num_visits = request.session.get('num_visite', 0) + 1
    request.session["num_visits"] = num_visits
    if num_visits > 4: del(request.session["num_visits"])
    return HttpResponse("view count=" + str(num_visits))