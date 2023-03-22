from lib.review import Review

class Reader:
    
    usernames=[]

    def __init__(self, username):
        self.set_username(username)

    def get_username(self):
        return self._username

    def set_username(self,username):
        if(username not in Reader.usernames):
            if(len(username)>=8 and len(username)<=16):
                self._username=username
                Reader.usernames.append(username)
            else:
                raise Exception("Username must be between 8 and 16 characters long inclusive")
        else:
            raise Exception("Username already taken")

                

    # username property goes here!
    username=property(get_username,set_username)


    def reviewed_book(self, book):
        return book in self.get_reviewed_books()

    def rate_book(self, book, rating):
        if(self.reviewed_book(book)):
            for review in self.get_reviews():
                if(review.get_book()==book):
                    review.rating=rating
        else:
            Review(self,book,rating)


    def __repr__(self):
        return f"<Reader(username:{self.username})>"
    
    def get_reviews(self):
        return [review for review in Review.reviews if review.reader==self]
    
    def get_reviewed_books(self):
        return [review.get_book() for review in self.get_reviews()]