from django.shortcuts import render

def index(request):
    return render(request, 'bookmodule/index.html')

def list_books(request):
    # Pass the BOOKS data to the template
    return render(request, 'bookmodule/list_books.html', {'books': BOOKS})


def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


# Sample data to simulate a database
BOOKS = [
    {
        "id": 1,
        "title": "Internet & World Wide Web How to Program",
        "author": "Author Name",
        "description": (
            "Internet & World Wide Web How to Program, 5/e provides a clear, simple, engaging "
            "and entertaining introduction to Internet and web programming. It’s appropriate for both "
            "introductory and intermediate-level client-side and server-side programming courses."
        ),
        "image": "book1.jpg",
    },
    {
        "id": 2,
        "title": "C++ How to Program, Late Objects Version",
        "author": "Another Author",
        "description": "This book introduces C++ programming in depth with clear examples.",
        "image": "book2.jpg",
    },
]

def viewbook(request, bookId):
    # Find the book with the given ID
    book = next((b for b in BOOKS if b["id"] == bookId), None)
    if not book:
        return render(request, 'bookmodule/404.html', status=404)  # Handle book not found

    return render(request, 'bookmodule/one_book.html', {'book': book})
