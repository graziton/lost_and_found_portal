from django.shortcuts import render, redirect
from .forms import LostItemForm, FoundItemForm, LostItem, FoundItem

def home(request):
    return render(request, 'lost_and_found/home.html')  # we’ll create this next

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
    lost_items = LostItem.objects.all().order_by('-date_reported')
    found_items = FoundItem.objects.all().order_by('-date_reported')
    context = {
        'lost_items': lost_items,
        'found_items': found_items,
    }
    return render(request, 'lost_and_found/items_list.html', context)
