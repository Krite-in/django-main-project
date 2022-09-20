from distutils.command.build_scripts import first_line_re
from re import template
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.
def about(request):
    template = loader.get_template('index.html')
    return HttpResponse("<html><body>working</body></html>")
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def account(request):
    template = loader.get_template('index.html')
    return HttpResponse("<html><body>working</body></html>")
def tour(request):
    template = loader.get_template('index.html')
    return HttpResponse("<html><body>working</body></html>")
def gallery(request):
    template = loader.get_template('index.html')
    return render(template)
def dashboard(request):
    template = loader.get_template('index.html')
    return HttpResponse("<html><body>working</body></html>")
