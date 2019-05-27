from django.shortcuts import render
from indexapp.models import TBook,TClass,TUser


# Create your views here.




class Cartltem:
    def __init__(self,book,amount):
        self.amount = amount
        self.id = book.book_id
        self.name = book.book_name
        self.pic = book.illustration
        self.dd_price = book.dd_price
        self.price = book.price
        self.all_price = book.dd_price * amount
        self.illustration = book.illustration
        self.press = book.press
        self.state = 1



class Cart:
    def __init__(self):
        self.lst = []
        self.amount = 0
        self.dd_price = 0
        self.price = 0




    def add_book_toCart(self,info):
        for i in self.lst:
            if i.id == info.id:
                if i.state:
                    i.amount += info.amount
                else:
                    i.amount = 1
                    i.state = 1
                break

        else:
            self.lst.append(info)
        self.change()





    def remove(self, book_id):
        print(book_id,1)
        self.find(book_id).state = False
        self.change()

    def recover(self, book_id):

        self.find(book_id).state = True
        self.change()

    def change_amount(self, book_id, new_amount):

        self.find(book_id).amount = new_amount
        self.change()

    def change(self):

        self.dd_price = 0
        self.price = 0
        self.amounts = 0
        for item in self.lst:
            if item.state:
                self.dd_price += item.dd_price * item.amount
                self.price += item.price * item.amount
                self.amounts += item.amount
                item.all_price = item.dd_price * item.amount

    def find(self, book_id):
        print(1111)
        print(book_id)
        info_id = (book_id if isinstance(book_id, int) else int(book_id))
        print(info_id)
        for i in self.lst:
            if i.id == info_id:
                return i
        return False

