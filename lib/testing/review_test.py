import pytest

from lib.book import Book
from lib.review import Review
from lib.reader import Reader

class TestReview:
    '''Review in review.py'''

    def test_has_rating_reader_book(self):
        '''has the rating, reader, and book passed into __init__.'''
        book = Book(title="To Kill a Mockingbird")
        reader = Reader(username="sam")
        rating = 9
        review = Review(book=book, reader=reader, rating=rating)
        assert review.book == book
        assert review.reader == reader
        assert review.rating == rating

    def test_requires_1_to_5_rating(self):
        '''requires ratings to be between 1 and 5, inclusive.'''
        book = Book(title="The Catcher in the Rye")
        reader = Reader(username="Will")
        with pytest.raises(Exception):
            Review(book=book, reader=reader, rating="fine")
        with pytest.raises(Exception):
            Review(book=book, reader=reader, rating=0)

    def test_requires_reader_of_reader_class(self):
        '''requires reader to be instance of Reader class.'''
        book = Book(title="To Kill a Mockingbird")
        rating = 2
        with pytest.raises(Exception):
            reader = "Patty"
            Review(book=book, reader=reader, rating=rating)

    def test_requires_book_of_book_class(self):
        '''requires book to be instance of Book class.'''
        reader = Reader(username="Ben")
        rating = 3
        with pytest.raises(Exception):
            book = "1984"
            Review(book=book, reader=reader, rating=rating)