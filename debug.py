#!/usr/bin/env python3
import ipdb;

from lib.book import Book
from lib.reader import Reader
from lib.review import Review

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    book_1=Book("To Kill a Mockingbird")
    book_2=Book("The Catcher in the Rye")
    book_3=Book("Native Sun")

    reader_1=Reader("Annabelle")
    reader_2=Reader("PetePete")
    reader_3=Reader("JackJack")

    review_1=Review(reader_1,book_1,5)
    review_2=Review(reader_1,book_1,5)
    review_3=Review(reader_1,book_2,4)








# DO NOT REMOVE THIS
    ipdb.set_trace()
