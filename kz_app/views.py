
from django.views import View
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import EmailMessage

from .models import *
from .forms import *


# Create your views here.

def index1(request):
    return render(request, 'kz_app/index1.html')

def foods(request):
    context = {
        'foods': Food.objects.all(),
    }
    return render(request, 'kz_app/foods.html', context=context)

def feedback(request):
    shelf = Feedback.objects.all()
    return render(request, 'kz_app/feedback.html', {'shelf': shelf})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Feedback.objects.get(id = book_id)
    except Feedback.DoesNotExist:
        return redirect('feedbacks')
    book_form = FeedbackCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('feedbacks')
    return render(request, 'kz_app/upload_feedback.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Feedback.objects.get(id = book_id)
    except Feedback.DoesNotExist:
        return redirect('feedbacks')
    book_sel.delete()
    return redirect('feedbacks')

def womens(request):
    return render(request, 'kz_app/womens.html', context={'women': Sportmasters_of_Kazakhstan.objects.order_by('-id')})

def women_slug(request ,women_slug):
    women = get_object_or_404(Sportmasters_of_Kazakhstan, slug=women_slug)
    context = {
        'women': women,
    }
    return render(request, 'kz_app/women.html', context=context)

def upload(request):
    upload = FeedbackCreate()
    if request.method == 'POST':
        upload = FeedbackCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('feedbacks')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{% url 'feedbacks' %}">reload</a>""")
    else:
        return render(request, 'kz_app/upload_feedback.html', {'upload_form':upload})

class RegisterUser(CreateView):
    form_class = CreateUserForm
    template_name = 'kz_app/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_user_context(title='Registration')
        return dict(list(context.items()))

    def get_user_context(self, title):
        pass

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'kz_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_user_context(title="Login")
        return dict(list(context.items()))

    def get_user_context(self, title):
        pass

    def get_success_url(self):
        return reverse_lazy('index1')


def logout_user(request):
    logout(request)
    return redirect('login')


class EmailView(View):
    form_class = contactForm
    templates_name = 'kz_app/contact.html'

    def get(self, request):
        form = self.form_class()
        return render(request, 'kz_app/contact.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER
            try:
                mail = EmailMessage(subject, message, from_email, [to_email])
                mail.send()
                return render(request, 'kz_app/contact.html',
                              {'form': form, 'error_message': 'Your message was successfully sent to %s' % email})
            except:
                return render(request, 'kz_app/contact.html',
                              {'form': form, 'error_message': 'Form is invalid .'})

        return render(request, 'kz_app/contact.html', {'form': form, 'error_message': 'Try again !!!'})







