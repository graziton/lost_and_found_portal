from django.shortcuts import render, redirect, get_object_or_404
from .forms import LostItemForm, FoundItemForm, LostItem, FoundItem
from django.db.models import Q

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
    query = request.GET.get('q', '')  # Get the search query from the URL
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()

    if query:
        lost_items = lost_items.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query)
        )
        found_items = found_items.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query)
        )

    context = {
        'lost_items': lost_items,
        'found_items': found_items,
        'query': query,
    }
    return render(request, 'lost_and_found/items_list.html', context)

def lost_item_detail(request, pk):
    item = get_object_or_404(LostItem, pk=pk)
    return render(request, 'lost_and_found/lost_item_detail.html', {'item': item})

def found_item_detail(request, pk):
    item = get_object_or_404(FoundItem, pk=pk)
    return render(request, 'lost_and_found/found_item_detail.html', {'item': item})