import pytest

from lib.book import Book
from lib.reader import Reader

class TestReader:
    '''Reader in reader.py'''

    def test_has_username(self):
        '''has the username passed into __init__.'''
        reader = Reader(username="Tom")
        assert reader.username == "Tom"

    def test_requires_username_between_8_and_16_characters(self):
        '''requires titles to be strings between 8 and 16 characters, inclusive.'''
        with pytest.raises(Exception):
            Reader(username="53636")
        with pytest.raises(Exception):
            Reader(username=53636)

    def test_requires_unique_username(self):
        '''requires username to be unique.'''
        Reader(username="Tom")
        with pytest.raises(Exception):
            Reader(username="Tom")

    def test_has_reviews(self):
        '''has a list of reviews.'''
        reader = Reader(username="Sam")
        assert hasattr(reader, "reviews")
        assert isinstance(reader.reviews, list)

    def test_has_reviewed_books(self):
        '''has a list of reviewed books.'''
        reader = Reader(username="Fantasia")
        assert hasattr(reader, "reviewed_books")
        assert isinstance(reader.reviewed_books, list)

    def test_checks_if_reviewed_book(self):
        '''has a method "reviewed_book" that checks if a book has been reviewed or not.'''
        reader = Reader(username="Annabelle")
        book_1 = Book("Native Sun")
        reader.reviewed_books.append(book_1)
        assert reader.reviewed_book(book_1)
        book_2 = Book("The Catcher in the Rye")
        assert not reader.reviewed_book(book_2)

    def test_reviews_book(self):
        '''adds review to a reader's reviews if it has not been reviewed, otherwise updates existing review.'''
        reader = Reader(username="pretty")
        book = Book("To Kill a Mockingbird")
        reader.rate_book(book, 3)
        assert book in reader.reviewed_books
        assert reader.reviews[0].rating == 3
        reader.rate_book(book, 4)
        assert len(reader.reviewed_books) == 1
        assert reader.reviews[0]
