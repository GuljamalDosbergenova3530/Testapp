from django.shortcuts import render,redirect
from django.http import Http404
from .models import Category,Product
from .forms import CategoryForm

def home(request):
    
    return render(request, 'luck/home.html')

def category(request):
    category =Category.objects.all()
    context ={
        'category': category
    }
    return render(
        request, 'luck/category.html', context
    )

def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return render(request, 'errors/404.html')
    #category = get_object_or_404(Category, id=pk)
    context = {'category': category }
    return render(request, 'luck/category_detail.html',context)

def about(request):
    return render(request, 'luck/about.html')

def contact(request):
    return render(request, 'luck/contact.html')

def create_category(request):
    if request.method =='POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Category.objects.create(
                name=cd['name'],
                image=cd['image'],
                description=cd['description'],
                price=cd['price']
            )
            return redirect(to='category')
    else:
         form = CategoryForm() 
    context = {
        'form' : form
    } 
    return render(request, 'luck/create_category.html', context)
