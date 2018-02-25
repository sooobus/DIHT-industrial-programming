from django.shortcuts import render
from .models import ToDoItem
from .forms import ToDoItemForm
from .forms import CheckDoneForm
# Create your views here.

def items_list(request):
    items = ToDoItem.objects.filter(done=False)
    if request.method == "POST":
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
        for item in items:
            if item.title in request.POST:
                item.done = True
                item.save()
    else:
        form = ToDoItemForm()
    return render(request, 'core/items_list.html', {'items': items, 'form': form})
