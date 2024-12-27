from django.test import TestCase, Client
from .models import *
import datetime


class MemberTest(TestCase):
    def setUp(self):
        self.client = Client()
        saeid = Author.objects.create(first_name='Saeid', last_name='Zamani', date_of_birth=datetime.date(2000, 1, 1),
                                      date_of_death=datetime.date(2010, 1, 1))
        asghar = Author.objects.create(first_name='Ali', last_name='Shafiee',
                                       date_of_birth=datetime.date(2000, 2, 2), date_of_death=None)
        karim = Author.objects.create(first_name='SAli', last_name='Babaie', date_of_birth=datetime.date(1950, 1, 1),
                                      date_of_death=datetime.date(2010, 1, 1))
        book1 = Book.objects.create(title='Book1', author=saeid, summary='this is book1.',
                                    date_of_publish=datetime.date(2000, 1, 1))
        book2 = Book.objects.create(title='Book2', author=asghar, summary='this is book2.',
                                    date_of_publish=datetime.date(2010, 1, 1))
        book3 = Book.objects.create(title='Book3', author=karim, summary='this is book3.',
                                    date_of_publish=datetime.date(2010, 1, 1))

    def test_is_alive(self):
        saeid = Author.objects.get(first_name='Saeid')
        ali = Author.objects.get(first_name='Ali')
        self.assertTrue(ali.is_alive())
        self.assertFalse(saeid.is_alive())

    def test_get_age_author(self):
        saeid = Author.objects.get(first_name='Saeid')
        ali = Author.objects.get(first_name='Ali')
        self.assertEqual(saeid.get_age().days, (saeid.date_of_death - saeid.date_of_birth).days)
        self.assertNotEqual(saeid.get_age().days, (datetime.date.today() - saeid.date_of_birth).days + 1)
        self.assertEqual(ali.get_age().days, (datetime.date.today() - ali.date_of_birth).days)
        self.assertNotEqual(ali.get_age().days, (datetime.date.today() - ali.date_of_birth).days + 1)

    def test_str_author(self):
        saeid = Author.objects.get(first_name='Saeid')
        self.assertEqual(saeid.__str__(), saeid.first_name + ' ' + saeid.last_name)

    def test_get_age_book(self):
        book1 = Book.objects.get(title='Book1')
        book2 = Book.objects.get(title='Book2')
        self.assertEqual(book1.get_age().days, (datetime.date.today() - book1.date_of_publish).days)
        self.assertNotEqual(book1.get_age().days, (datetime.date.today() - book1.date_of_publish).days + 1)
        self.assertEqual(book2.get_age().days, (datetime.date.today() - book2.date_of_publish).days)
        self.assertNotEqual(book2.get_age().days, (datetime.date.today() - book2.date_of_publish).days + 1)

    def test_str_book(self):
        book1 = Book.objects.get(title='Book1')
        self.assertEqual(str(book1), 'Book1')

    def test_booklist(self):
        author_age, book_age = 28, 20
        response = self.client.get('/booklist/{}/{}/'.format(author_age, book_age))
        body = response.content.decode('utf-8')

        books = Book.objects.all()
        good_books = []
        bad_books = []
        for book in books:
            if book.get_age().days // 365 < book_age:
                if book.author.get_age().days // 365 < author_age:
                    good_books.append(book)
                else:
                    bad_books.append(book)
            else:
                bad_books.append(book)

        self.assertTrue("<title>Booklist</title>" in body)
        self.assertEqual(response.context['good_books'], good_books)
        self.assertEqual(response.context['bad_books'], bad_books)
        self.assertTrue("Bad Books" in body)
        self.assertTrue('Book2' in body)
