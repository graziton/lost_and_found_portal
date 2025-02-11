from django.shortcuts import render, redirect, get_object_or_404
from .forms import LostItemForm, FoundItemForm, UserRegistrationForm
from .models import LostItem, FoundItem
from django.db.models import Q
from datetime import datetime

def home(request):
    return render(request, 'lost_and_found/home.html')

def report_lost(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LostItemForm()
    return render(request, 'lost_and_found/report_lost.html', {'form': form})

def report_found(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoundItemForm()
    return render(request, 'lost_and_found/report_found.html', {'form': form})

def items_list(request):
    query = request.GET.get('q', '')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()

    if query:
        lost_items = lost_items.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query)
        )
        found_items = found_items.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query)
        )

    if start_date:
        lost_items = lost_items.filter(date_reported__gte=start_date)
        found_items = found_items.filter(date_reported__gte=start_date)
    if end_date:
        lost_items = lost_items.filter(date_reported__lte=end_date)
        found_items = found_items.filter(date_reported__lte=end_date)

    context = {
        'lost_items': lost_items,
        'found_items': found_items,
        'query': query,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'lost_and_found/items_list.html', context)

def lost_item_detail(request, pk):
    item = get_object_or_404(LostItem, pk=pk)
    return render(request, 'lost_and_found/lost_item_detail.html', {'item': item})

def found_item_detail(request, pk):
    item = get_object_or_404(FoundItem, pk=pk)
    return render(request, 'lost_and_found/found_item_detail.html', {'item': item})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'lost_and_found/register.html', {'form': form})
