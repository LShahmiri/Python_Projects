Library={}

def add_book():
    book_id=input('Enter book ID: ')
    title=input('enter book title: ')
    author=input('enter book author: ')
    genre=input('enter book genre: ')


    book={
        'title': title,
        'author':author,
          'genre':genre
    }

    Library[book_id]=book
    print('Book added successfully!')
    
