class Review:
    
    reviews=[]

    def __init__(self, reader, book, rating):
        self.set_rating(rating)
        self.set_book(book)
        self.set_reader(reader)
        Review.reviews.append(self)

    def get_rating(self):
        return self._rating
    
    def set_rating(self,rating):
        if(type(rating) in (int,) and (1<=rating and rating<=5 ) ):
            self._rating=rating
        else:
            raise Exception("Rating must be an integer between 1 and 5 inclusive")

    def get_reader(self):
        return self._reader
    
    def set_reader(self,reader):
        from lib.reader import Reader
        if(isinstance(reader,Reader)):
            self._reader=reader
        else:
            raise Exception("Reader must be a reader object.")

    def get_book(self):
        return self._book
    
    def set_book(self,book):
        from lib.book import Book
        if(isinstance(book,Book)):
            self._book=book
        else:
            raise Exception("Book must be a book object")
        
    def __repr__(self):
        return f"<Review(reader={self.reader} book={self.book} rating={self.rating})>"

    # rating property goes here!
    rating=property(get_rating,set_rating)

    # reader property goes here!
    reader=property(get_reader,set_reader)

    # book property goes here!
    book=property(get_book,set_book)