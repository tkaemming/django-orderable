from django.test import TestCase
from books.models import Book, Chapter

class OrderableTestCase(TestCase):
    def test_book_ordering(self):
        dip = Book.objects.get(title='Dive into Python')
        lpthw = Book.objects.get(title='Learn Python the Hard Way')

        books = Book.objects.in_order()
        self.assertEqual(books[0].pk, dip.pk)
        self.assertEqual(books[1].pk, lpthw.pk)

        books = Book.objects.in_order(reverse=True)
        self.assertEqual(books[0].pk, lpthw.pk)
        self.assertEqual(books[1].pk, dip.pk)

        self.assertEqual(Book.objects.get_next(dip).pk, lpthw.pk)
        self.assertEqual(dip.get_next().pk, lpthw.pk)

        self.assertEqual(Book.objects.get_previous(lpthw).pk, dip.pk)
        self.assertEqual(lpthw.get_previous().pk, dip.pk)

        self.assertRaises(Book.DoesNotExist, lambda: Book.objects.get_previous(dip))
        self.assertRaises(Book.DoesNotExist, dip.get_previous)

        self.assertRaises(Book.DoesNotExist, lambda: Book.objects.get_next(lpthw))
        self.assertRaises(Book.DoesNotExist, lpthw.get_next)

    def test_chapter_ordering(self):
        dip = Book.objects.get(title='Dive into Python')
        dip_chapters = list(dip.chapter_set.in_order())

        lpthw = Book.objects.get(title='Learn Python the Hard Way')
        lpthw_chapters = list(lpthw.chapter_set.in_order())

        self.assertRaises(Chapter.DoesNotExist, dip_chapters[0].get_previous)
        self.assertEqual(dip_chapters[0].get_next().pk, dip_chapters[1].pk)
        self.assertEqual(dip_chapters[1].get_previous().pk, dip_chapters[0].pk)
        self.assertRaises(Chapter.DoesNotExist, dip_chapters[-1].get_next)

        self.assertRaises(Chapter.DoesNotExist, lpthw_chapters[0].get_previous)
        self.assertEqual(lpthw_chapters[0].get_next().pk, lpthw_chapters[1].pk)
        self.assertEqual(lpthw_chapters[1].get_previous().pk, lpthw_chapters[0].pk)
        self.assertRaises(Chapter.DoesNotExist, lpthw_chapters[-1].get_next)
