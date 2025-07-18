from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'  # same here
# from .forms import CustomUserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
