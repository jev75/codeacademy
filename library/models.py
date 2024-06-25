from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField



from django.db import models
class Genre(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite knygos žanrą (pvz. detektyvas)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Žanras'
        verbose_name_plural = 'Žanrai'

class Book(models.Model):
    """Modelis reprezentuoja knygą (bet ne specifinę knygos kopiją)"""
    title = models.CharField('Pavadinimas', max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField('Aprašymas', max_length=1000, help_text='Trumpas knygos aprašymas')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>')
    genre = models.ManyToManyField(Genre, help_text='Išrinkite žanrą(us) šiai knygai')
    cover = models.ImageField('Viršelis', upload_to='covers', null=True, blank=True)

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Žanras'

    class Meta:
        verbose_name = 'Knyga'
        verbose_name_plural = 'Knygos'

class BookInstance(models.Model):
    """Modelis, aprašantis konkrečios knygos kopijos būseną"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, verbose_name='Knyga')
    due_back = models.DateField('Bus prieinama', null=True, blank=True)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Skaitytojas')

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas', verbose_name='Statusas'
    )
    class Meta:
        ordering = ['due_back']
        verbose_name = 'Knygos egzempliorius'
        verbose_name_plural = 'Knygos egzemplioriai'


    def __str__(self):
        return f'{self.id} ({self.book.title if self.book else "Nėra knygos"})'

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

class Author(models.Model):
    """Modelis, atvaizduojantis autorių."""
    first_name = models.CharField('Vardas', max_length=100)
    last_name = models.CharField('Pavardė', max_length=100)
    description = HTMLField('Aprašymas', default='')


    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        """Eilutė, atvaizduojanti Modelio objektą."""
        return f'{self.last_name} {self.first_name}'

    def display_books(self):
        return ', '.join(book.title for book in self.books.all()[:3])

    display_books.short_description = 'Knygos'

    class Meta:
        verbose_name = 'Autorius'
        verbose_name_plural = 'Autoriai'