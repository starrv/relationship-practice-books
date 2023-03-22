import pytest

from lib.book import Book

class TestBook:
    '''Book in book.py'''

    def test_has_title(self):
        '''has the title passed into __init__.'''
        book = Book(title="To Kill a Mockingbird")
        assert book.title == "To Kill a Mockingbird"

    def test_requires_nonzero_string_title(self):
        '''requires titles to be strings of >0 characters.'''
        with pytest.raises(Exception):
            Book(title=1)
        with pytest.raises(Exception):
            Book(title="")
    
    def test_has_reviews(self):
        '''contains an instance attribute, reviews, a list of its reviews.'''
        book = Book(title="The Catcher in the Rye")
        assert hasattr(book, "reviews")
        assert isinstance(book.reviews, list)

    def test_has_reviewers(self):
        '''contains an instance attribute, reviewers, a list of its readers who left reviews.'''
        book = Book(title="Native Sun")
        assert hasattr(book, "reviewers")
        assert isinstance(book.reviewers, list)

    def test_calculates_average_rating(self):
        '''has a method "average_rating" that returns the average of self.reviews.'''
        book = Book(title="1984")
        book.reviews = [1, 3, 2, 4, 5, 4, 2]
        assert book.average_rating() == 3

    def test_shows_highest_rated(self):
        '''has a method "highest_rated" that returns the highest rated book.'''
        Book.all = []
        book_1 = Book(title="To Kill a Mockingbird")
        book_1.reviews = [1, 1, 1, 2, 3, 4, 4, 5]
        book_2 = Book(title="The Catcher in the Rye")
        book_2.reviews = [1, 1, 1, 1, 1, 1]
        book_3 = Book(title="Native Sun")
        book_3.reviews = [5, 5, 5, 5, 5, 5, 5]
        book_4 = Book(title="1984")
        book_4.reviews = [4, 3, 4, 3, 2, 5, 4]
        assert Book.highest_rated().title == "Native Sun"
