from lib.review import Review

class Book:

    all=[]
    
    def __init__(self, title):
        self.set_title(title)
        self.all.append(self)

    # title property goes here!
    def set_title(self,title):
        if(type(title) in (str,) and (len(title)>0)):
            self._title=title
        else:
            raise Exception("Title must be a string with at least 1 character")

    def get_title(self):
        return self._title

    title=property(get_title,set_title)
    
    def average_rating(self):
        ratings=[review.get_rating() for review in Review.reviews if review.get_book()==self]
        if(len(ratings)<=0):return 0
        return sum(ratings)/len(ratings)


    @classmethod
    def highest_rated(cls):
        max_book=Book.all[0]
        for i in range(1,len(Book.all)):
            if(Book.all[i].average_rating()>max_book.average_rating()):
                max_book=Book.all[i]
        return max_book


    def __repr__(self):
        return f"<Book(title={self.title})>"

   