from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Person
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#@login_required(login_url='/wallet/login')




def home(request):
    #if request.user.is_authenticated():
   # print(request.user.get_username())
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.get_username())
        # print(user.id)
        # user1=User.objects.get(pk=user.id)
        # print(user1)
        # print(Person.objects.all())
        try:
            wallet_person = Person.objects.get(person=user)
        except:
            wallet_person = None
        if wallet_person:
            # wallet_person=Person.objects.get(person=user)
            # print(Person.objects.all())
            money_in_wallet = wallet_person.wallet;
        else:
            wallet_person = Person(person=user, wallet=0, pk=user.id)
            money_in_wallet = 0
            wallet_person.save()

        print('in the making')
        return (render(request, 'home.html', {'money_in_wallet': money_in_wallet}))
    else:
        return (render(request, 'home.html'))


@login_required(login_url='/wallet/login')
def add(request):
    print('in the working')
    if request.method =='POST':
        money=int(request.POST['money']);
        user=User.objects.get(username=request.user.get_username());
        person=Person.objects.get(person=user,pk=user.id)
        person.wallet=person.wallet +money
        money_in_wallet=person.wallet
        person.save()
        return HttpResponseRedirect("/wallet")



@login_required(login_url='/wallet/login')
def subtract(request):
    print('in the working')
    if request.method =='POST':
        money=int(request.POST['money']);
        user=User.objects.get(username=request.user.get_username());
        person=Person.objects.get(person=user,pk=user.id)
        person.wallet=person.wallet-money
        money_in_wallet=person.wallet
        person.save()

        return HttpResponseRedirect("/wallet")
