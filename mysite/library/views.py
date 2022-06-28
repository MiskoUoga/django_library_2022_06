from django.shortcuts import render
from .models import (Book,
                     BookInstance,
                     Author)


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='g').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)


def authors(request):
    my_authors = Author.objects.all()
    my_context = {
        "authors": my_authors,
    }
    return render(request, 'authors.html', context=my_context)
