# Call as dumpdata('GET', request.GET)

def dumpdata(place, data):
    retval = ""
    if len(data) > 0:
        retval += '<p>Incoming ' + place + ' data:<br>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + "<br>\n"
            retval += "<p>\n"
    return retval