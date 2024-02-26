from django.shortcuts import render, redirect
from .forms import AlbumForm

# Create your views here.
def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect("home")
    else: 
        form = AlbumForm()
    return render(request, 'create_album.html', {"form": form})