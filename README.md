# Object Relations Code Challenge - Books

For this challenge, we'll be working with a Book Review domain.

We have three models: `Reader`, `Book`, and `Review`.

A `Book` has many `Review`s. A `Reader` has many `Review`s. A `Review` belongs
to a `Reader` and belongs to a `Book`.

`Reader` - `Book` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge does not have tests. You cannot run `pytest`.
You'll need to create your own sample instances so that you can try out your
code on your own. Make sure your relationships and methods work in the console
before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Book

- `Book __init__(self, title)`
  - `Book` is initialized with a title (string)
  - Title **can be** changed after the `Book` is initialized
- `Book property title()`
  - Returns the `Book`'s title
  - Titles must be strings greater than 0 characters

#### Reader

- `Reader __init__(self, username)`
  - `Reader` is initialized with a username (string)
  - Usernames **can be** changed after the Reader is initialized
- `Reader property username()`
  - Returns the Reader's username
  - Usernames must be _unique_ strings between 8 and 16 characters,
    inclusive

#### Review

- `Review __init__(self, reader, book, rating)`
  - `Review` is initialized with a `Reader` instance, a `Book` instance, and a
    rating (number)
- `Review property rating()`
  - Returns the rating for the `Review` instance
  - Ratings must be integers between 1 and 5, inclusive

### Object Relationship Attributes and Properties

#### Review

- `Review property reader()`
  - Returns the reader who wrote the review
  - Readers must be `Reader` instances
    - You will need to import `Reader` _inside_ of this property to avoid a
      _circular import_.
- `Review property book()`
  - Returns the book that is being reviewed
  - Books must be `Book` instances
    - You will need to import `Book` _inside_ of this property to avoid a
      _circular import_.

#### Reader

- `Reader reviews`
  - Returns a list of `Review` instances associated with the `Reader` instance.
- `Reader reviewed_books`
  - Returns a list of `Book` instances reviewed by the `Reader` instance.

#### Book

- `Book reviews`
  - Returns a list of all the `Review` instances for the `Book`.
- `Book reviewers`
  - Returns a list of all of the `Reader` instances that reviewed the `Book`.

### Aggregate and Association Methods

#### Reader

- `Reader reviewed_book(book)`
  - Returns `True` if the `Reader` has reviewed this `Book` (if there is a
    `Review` instance that has this `Reader` and `Book`), returns `False`
    otherwise
- `Reader rate_book(book, rating)`
  - A `Book` instance and a rating (number) are passed in as arguments
  - If the `Reader` instance and the passed `Book` instance are _not_ already
    associated, this method should create a new `Review` instance
  - If this `Reader` has already reviewed this `Book`, assigns the new rating
    to the existing `Review` instance

#### Book

- `Book average_rating()`
  - Returns the average of all ratings for the `Book` instance
  - To average ratings, add all ratings together and divide by the total number
    of ratings.
- `Book classmethod highest_rated(books)`
  - Returns the `Book` instance with the highest average rating.
# relationship-practice-books
