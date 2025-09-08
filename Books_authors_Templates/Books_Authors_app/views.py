from django.shortcuts import render ,redirect
from . models import Book,Author
# Create your views here.
def index(request):
    data={
        'Book':Book.objects.all(),
        'Author':Author.objects.all()
    }
    return render(request,'index.html',data)


def authors(request):
    data={
        'Book':Book.objects.all(),
        'Author':Author.objects.all()
    }
    return render(request,'authors.html',data)


def add_book(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        Book.objects.create(title=title,description=description)
        return redirect('/')
    return redirect ('/')


def add_author(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        notes=request.POST.get('notes')
        Author.objects.create(first_name=first_name,last_name=last_name,notes=notes)
        return redirect('authors')
    return redirect('authors')


def display_book(request,num):
    book=Book.objects.filter(id=num).first()
    if request.method=='POST':
        author_ids=request.POST.getlist('author_ids')
        if author_ids:
            book.authors.add(*author_ids)
        return redirect('/')
    
    data={
        'Book':Book.objects.all(),
        'Author':Author.objects.all(),
        'book':book
    }

    return render(request,'book_info.html',data)


def display_author(request,num):
    author=Author.objects.filter(id=num).first()
    if request.method=='POST':
        book_ids=request.POST.getlist('book_ids')
        if book_ids:
            author.books.add(*book_ids)
        return redirect('authors') 
    
    data={
        'Book':Book.objects.all(),
        'Author':Author.objects.all(),
        'author':author,
    }
        
    return render(request,'author_info.html',data)