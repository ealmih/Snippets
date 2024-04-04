from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    form = SnippetForm()
    context = {
        'pagename': 'Добавление нового сниппета',
        'form':form
        }
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets
        }
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(id = snippet_id)
    context = {
        'pagename': 'Просмотр сниппета',
        'snippet': snippet
        }
    return render(request, 'pages/snippet_detail.html', context)

def snippet_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        lang = request.POST['lang']
        code = request.POST['code']
        snippet = Snippet(name=name, lang=lang, code=code)
        snippet.save()
        return redirect('snippets-list')
    
def create_snippet(request):
   form = SnippetForm()
   return render(request, 'add_snippet.html', {'form': form})
