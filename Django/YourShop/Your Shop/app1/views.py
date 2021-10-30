from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import category, item
from django.views.generic.edit import CreateView
from .models import item, item_review, delivery
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, deliveryform
from django.contrib.auth import views as auth_views

"""
    The files lists the various views the urls link to.
    All the views have been explained accordingly. 
"""
def index(request):  #the main homepage view
    items=item.objects.all()
    cats=category.objects.all()
    context={'items':items,'cats':cats}
    return render(request, 'app1/index.html', context)


def detail(request, pk): #to show the detail of an item, or the detail page
    x=get_object_or_404(item, product_id=pk)
    cats=category.objects.all()
    return render(request, 'app1/detailnew.html', {'x':x,'cats':cats})

in_cartlist=[]

def cart(request, pk): #this view function puts an item to the shopping cart
    cats=category.objects.all()
    if request.user.is_authenticated():
        x=get_object_or_404(item, product_id=pk)
        x.in_cart=True
        x.save()
        in_cartlist.append(x)
        return render(request, 'app1/detailnew.html', {'x':x,'cats':cats})
    else:
        return detail(request, pk)

def incart(request): #to show the shopping cart, all the products in the cart are shown in this view
    cats=category.objects.all()
    total = 0
    for item in in_cartlist:
        total += item.price
    total=str(total)
    if request.user.is_authenticated():
        return render(request, 'app1/incart.html', {'list':in_cartlist, 'total':total,'cats':cats})
    else:
        raise Http404("Not logged In")


def rcart(request, pk):# THIS VIEW IS USED TO REMOVE AN ITEM FROM THE CART
    cats=category.objects.all()
    x=get_object_or_404(item, product_id=pk)
    x.in_cart=False
    x.save()
    if(x in in_cartlist):
        in_cartlist.remove(x)
    total = 0
    for k in in_cartlist:
        total += k.price
    total = str(total)
    return render(request, 'app1/incart.html', {'list':in_cartlist, 'total':total,'cats':cats})


def logout(request):# THE CUSTOM LOGOUT VIEW, REDIRECTS BACK TO HOME PAGE
    cats=category.objects.all()
    for x in in_cartlist:
        x.in_cart=False
        x.save()
    in_cartlist.clear()
    items = item.objects.all()
    context = {'items': items,'cats':cats}
    return render(request, 'app1/index.html', context)


class AddItem(CreateView): # TO ADD NEW ITEM TO THE DATABASE, IT WOULD BE USED
    model = item
    fields = ['cat', 'name', 'product_id', 'price', 'pic', 'rating']


class GiveReview(CreateView):
    model = item_review
    fields = ['product', 'comment']


class UserFormView(View):
    cats=category.objects.all()
    form_class=UserForm
    template='app1/registration_form.html'

    def get(self, request):
        cats=category.objects.all()
        form = self.form_class(None)
        return render(request, self.template, {'form':form,'cats':cats})

    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            cats=category.objects.all()
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('app1:index')

        return render(request, self.template, {'form':form,'cats':cats})

def search(request): # view to implement the search of the items
    cats=category.objects.all()
    query=request.GET.get('q')
    result=item.objects.filter(name__icontains=query)
    return render(request, 'app1/search.html', {'result': result,'cats':cats})

def checkout(request): # the checkout view
    cats=category.objects.all()
    return render(request, 'checkout.html',{'cats':cats})

def log(request): #this view is to implement the custom login form, using authenticate function
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("app1:index")
    else:
        return redirect("app1:index")

def catview(request): # to show items category wise on the page
    y=request.GET.get('cate')
    x=item.objects.filter(cat__name=y)
    cats=category.objects.all()
    return render(request, 'app1/catview.html', {'x':x,'cats':cats})

# def catdisp(request):
#     cats=category.objects.all()
#     context={'cats':cats}
#     return render(request, 'app1/index.html', context)

def deliverydetails(request):
    cats=category.objects.all()
    if request.method == "POST":
        form = deliveryform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('app1:checkout')
    else:
        form = deliveryform()
    return render(request, 'app1/delivery_form.html', {'form': form,'cats':cats})
