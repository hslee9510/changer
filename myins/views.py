from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import  Daily,Todo,Wish,Inspiration,Reference,Trophy
from .forms import DailyForm, TodoForm

def index(request):
    dailys = Daily.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/index.html',{'dailys':dailys})

def daily(request):
    dailys = Daily.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/daily_hs.html',{'dailys':dailys})

def daily_detail(request,pk):
    daily = get_object_or_404(Daily, pk=pk)
    return render(request, 'blog/details/daily_detail.html',{'daily':daily})

def daily_new(request):
    if request.method == "POST":
        form = DailyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('daily_detail', pk=post.pk)
    else:
        form = DailyForm()
    return render(request, 'blog/form/daily_edit.html', {'form': form})

def daily_edit(request, pk):
    daily = get_object_or_404(Daily, pk=pk)
    if request.method == "POST":
        form = DailyForm(request.POST, instance=daily)
        if form.is_valid():
            daily = form.save(commit=False)
            daily.save()
            return redirect('daily_detail', pk=daily.pk)
    else:
        form = DailyForm(instance=daily)
    return render(request, 'blog/form/daily_edit.html', {'form': form})

def todo(request):
    todos=Todo.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/todo.html',{'todos':todos})

def todo_detail(request,pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'blog/details/todo_detail.html',{'todo':todo})

def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('todo_detail', pk=post.pk)
    else:
        form = TodoForm()
    return render(request, 'blog/form/todo_edit.html', {'form': form})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form =TodoForm(instance=todo)
    return render(request, 'blog/form/todo_edit.html', {'form': form})

def wish(request):
    wishs=Wish.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/wish.html',{'wishs':wishs})

def wish_detail(request,pk):
    wish = get_object_or_404(Wish, pk=pk)
    return render(request, 'blog/details/wish_detail.html',{'wish':wish})

def inspiration(request):
    inspirations=Inspiration.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/inspiration.html',{'inspirations':inspirations})

def inspiration_detail(request,pk):
    inspiration = get_object_or_404(Todo, pk=pk)
    return render(request, 'blog/details/inspiration_detail.html',{'inspiration':inspiration})

def reference(request):
    references = Reference.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/reference.html',{'references':references})

def reference_detail(request,pk):
    reference = get_object_or_404(Todo, pk=pk)
    return render(request, 'blog/details/reference_detail.html',{'reference':reference})

def trophy(request):
    trophys = Trophy.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/trophy.html',{'trophys':trophys})

def trophy_detail(request,pk):
    trophy = get_object_or_404(Todo, pk=pk)
    return render(request, 'blog/details/trophy_detail.html',{'trophy':trophy})
