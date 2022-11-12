from django.shortcuts import render

# Create your views here.
from . models import Post

def index(request):
    
    postingan= Post.objects.all()
    contex={'Posting': postingan}
    return render(request, 'buku/index.html', contex)