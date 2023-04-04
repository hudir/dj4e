class AwesomeView(View):
    def get(self, request):
        msg = request.session.get('msg', False)
        if msg : del(request.session['msg'])
        return render(request, "getpost/guess.html", {'message': msg})
    
    def post(self, request):
        guess = request.POST.get('guess')
        msg = checkguess(guess)
        request.session['msg'] = msg
        return redirect(request.path)
    
