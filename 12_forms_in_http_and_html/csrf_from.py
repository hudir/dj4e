# @csrf_exempt
from dump import dumpdata

def postform(request):
    response = """<p>Impossible POST guessing game...</p>
<form method="POST">
    <div>
        <label for="guess">Input Guess</label>
        <input type="number" name="guess" id="guess">
        <input type="submit" value="submit">
    </div>
</form>
    """

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

def failform(request):
    response = """<p>CSRF Fail guessing game...</p>
<form method="POST">
    <div>
        <label for="guess">Input Guess</label>
        <input type="number" name="guess" id="guess">
        <input type="submit" value="submit">
    </div>
</form>
    """

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

# will get 403 forbidden csrf verficition failed
from django.middleware.csrf import get_token

def csrfform(request):
    response = """<p>CSRF Success guessing game...</p>
<form method="POST">
    <div>
        <label for="guess">Input Guess</label>
        <input type="number" name="guess" id="guess">
        <input type="submit" value="submit">
        <input type="hidden" value="__token__" name="csrfmiddlewaretoken">
    </div>
</form>
    """

    token = get_token(request)
    response = response.replace('__token__', html.escape(token))
    response += dumpdata('POST', request.POST)
    return HttpResponse(response)
    