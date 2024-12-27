from django.test import TestCase
from .models import Borrowed, Book, Member

class BorrowedTests(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(title='first_book', genre='comedy')
        self.book2 = Book.objects.create(title='second_book', genre='tarikhi')
        self.book3 = Book.objects.create(title='third_book', genre='tarikhi')        
        self.member1 = Member.objects.create(first_name='ali', last_name='alavi')
        self.member2 = Member.objects.create(first_name='mohammad', last_name='mahammadi')
        Borrowed.objects.create(member=self.member2, book=self.book2)
        Borrowed.objects.create(member=self.member1, book=self.book1)
        Borrowed.objects.create(member=self.member2, book=self.book3)

    def test_is_young(self):        
        self.assertEqual(self.member1.borrowed_books('tarikhi'), [])        
        self.assertEqual(self.member1.borrowed_books('comedy'), [self.book1.id])    
        self.assertEqual(self.member2.borrowed_books('tarikhi'), [self.book2.id, self.book3.id])    

