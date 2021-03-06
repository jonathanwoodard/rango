from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    # Request the context of the request
    # The context contains info like the client's machine details, for example
    context = RequestContext(request)

    # Construct a dict to pass to the template engine as it's context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Here are some robots!"}
    return render_to_response('rango/about.html', context_dict, context)
