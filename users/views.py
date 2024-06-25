from django.http import HttpResponseNotFound,HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Šis vartotojo vardas užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Šis el. pašto adresas jau užregistruotas!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.success(request, 'Registracija sėkminga! Dabar galite prisijungti!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    else:
        return render(request, 'registration/register.html')

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Jūsų profilis buvo sėkmingai atnaujintas!')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def about(request):
    return render(request, 'users/about.html')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Puslapis nerastas</h1>")


def facebook_login(request):
    return HttpResponse("<h2>Čia bus prisijungimas per Facebook paskyrą</h2>")

def google_login(request):
    return HttpResponse("<h2>Čia bus prisijungimas per Google paskyrą</h2>")