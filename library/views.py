from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages



def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='g').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits
    }
    return render(request, 'library/index.html', context=context)

def authors(request):
    paginator = Paginator(Author.objects.all(), 5)
    page_number = request.GET.get('page')
    authors = paginator.get_page(page_number)
    context = {
        'authors': authors
    }
    return render(request, 'library/authors.html', context=context)

def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'library/author.html', {'author': single_author})

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5
    template_name = 'library/book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Book.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    return render(request, 'library/search.html', {'books': search_results, 'query': query})

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name ='library/user_books.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(reader=self.request.user).filter(status__exact='p').order_by('due_back')

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'library/register.html')