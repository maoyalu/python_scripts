#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    LibraryManagement.py
# @Author:      Yalu
# @Time:        2/10/2018 8:34 PM
"""
A program that allows to borrow and return books from a library.
Suppose that the library cannot own more than one copy of each book.
A list of books will be stored in a file “exercise 8.dat” that will automatically be read at the start of the program.
Duplicate books are not allowed in the file, and each book is assigned a unique ID (a positive integer).
Every book is available at the start of the program.
The program allows the following operations:
• “display” displays for each book in the collection displays the title, their ID, as well as their availability,
• “check ID” checks the availability of a book given its ID,
• “borrow ID” marks the book with that ID as borrowed,
• “return ID” Return a book with that ID.
Finally, the commands should display appropriate error messages when:
• trying to borrow or return a book with an invalid ID (i.e. it does not belong to the collection),
• trying to borrow a book that is not available (i.e. it has been borrowed already),
• trying to return a book that has not been borrowed.
"""


class Book:
    def __init__(self, title, number):
        self.name = title
        self.id = number
        self.availability = True

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_availability(self):
        return self.availability

    def set_name(self, new_name):
        self.name = new_name

    def set_id(self, new_id):
        self.id = new_id

    def set_availability(self, new_status):
        self.availability = new_status

    def display(self):
        print('Title:', self.name, '\nID:', self.id, '\nAvailability:', self.availability, '\n')


class Library:
    def __init__(self):
        self.books = []
        self.book_count = 0
        self.load_books()

    def load_books(self):
        # Use a string instead just because I don't want to make that .bat file.
        # Anyways, I know they both work.
        # If you want to read from the file, uncomment line 272-274, comment line 275-283,
        # and make the 'exercise_8.dat' file to store the string content in one line.

        # f = open('exercise_8.dat', 'r')
        # book_list = f.readline().split(' - ')
        # f.close()
        book_list = "In Search of Lost Time - " \
                    "Alice's Adventures in Wonderland - " \
                    "East of Eden - " \
                    "The Odyssey - " \
                    "Twenty Thousand Leagues Under the Sea - " \
                    "Man’s Fate - The Picture of Dorian Gray - " \
                    "Adventures of Huckleberry Finn - " \
                    "Nineteen Eighty Four - " \
                    "Reveries of a Solitary Walker".split(' - ')
        for book in book_list:
            self.book_count += 1
            self.books.append(Book(book, self.book_count))

    def display(self):
        for book in self.books:
            book.display()

    def check_id(self, book_id):
        if 0 < book_id <= self.book_count:
            for book in self.books:
                if book.get_id() == book_id:
                    print(book.get_availability())
        else:
            print('Invalid ID')

    def borrow_id(self, book_id):
        if 0 < book_id <= self.book_count:
            for book in self.books:
                if book.get_id() == book_id:
                    if book.get_availability():
                        book.set_availability(False)
                    else:
                        print(book.get_name(), 'is not available.')
                    break
        else:
            print('Invalid ID')

    def return_id(self, book_id):
        if 0 < book_id <= self.book_count:
            for book in self.books:
                if book.get_id() == book_id:
                    if not book.get_availability():
                        book.set_availability(True)
                    else:
                        print(book.get_name(), 'is not borrowed.')
                    break
        else:
            print('Invalid ID')


if __name__ == '__main__':
    lib = Library()
    lib.display()
    lib.check_id(0)
    lib.check_id(11)
    lib.return_id(0)
    lib.return_id(11)
    lib.borrow_id(0)
    lib.borrow_id(11)
    lib.return_id(2)
    lib.borrow_id(2)
    lib.borrow_id(2)
    lib.display()
