from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cuisine  # Fixed import
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return HttpResponse("Welcome to home of first app!")

def Cuisine_list(request):
    objlist = Cuisine.objects.all()
    paginator = Paginator(objlist, 3)  # 2 items in each page
    page = request.GET.get('page')

    try:
        cuisines = paginator.page(page)
    except PageNotAnInteger:
        cuisines = paginator.page(1)
    except EmptyPage:
        cuisines = paginator.page(paginator.num_pages)

    # Ensure this matches your folder: templates/cuisine/cuisine_list.html
    return render(request, "cuisine/cuisine_list.html", {'page': page, 'cuisines': cuisines})

def Cuisine_detail(request, pk):
    # This will only show if status is 'published'
    cuisine_selected = get_object_or_404(Cuisine, pk=pk, status='published')
    context = {'cuisine': cuisine_selected}
    
    return render(request, 'cuisine/cuisine_details.html', context)