from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import  Daily,Todo_Trophy,Wish,Inspiration,Reference,Trophy
from .forms import DailyForm, Todo_TrophyForm, WishForm, InspirationForm, ReferenceForm, TrophyForm
from django.contrib.auth.decorators import login_required

def index(request):
    dailys = Daily.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/index.html',{'dailys':dailys})

def daily(request):
    dailys = Daily.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/daily_hs.html',{'dailys':dailys})

def daily_detail(request,pk):
    daily = get_object_or_404(Daily, pk=pk)
    return render(request, 'blog/details/daily_detail.html',{'daily':daily})
@login_required
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
@login_required
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
@login_required
def daily_remove(request, pk):
    daily = get_object_or_404(Daily, pk=pk)
    daily.delete()
    return redirect('daily')

def todo(request):
    todos=Todo_Trophy.objects.filter(success=False).order_by('date')
    return render(request, 'blog/todo.html',{'todos':todos})

def todo_detail(request,pk):
    todo = get_object_or_404(Todo_Trophy, pk=pk)
    return render(request, 'blog/details/todo_detail.html',{'todo':todo})
@login_required
def todo_new(request):
    if request.method == "POST":
        form = Todo_TrophyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('todo_detail', pk=post.pk)
    else:
        form = Todo_TrophyForm()
    return render(request, 'blog/form/todo_edit.html', {'form': form})
@login_required
def todo_edit(request, pk):
    todo_trophy = get_object_or_404(Todo_Trophy, pk=pk)
    if request.method == "POST":
        form = Todo_TrophyForm(request.POST, instance=todo_trophy)
        if form.is_valid():
            todo_trophy = form.save(commit=False)
            todo_trophy.save()
            return redirect('todo_detail', pk=todo_trophy.pk)
    else:
        form =Todo_TrophyForm(instance=todo_trophy)
    return render(request, 'blog/form/todo_edit.html', {'form': form})

def wish(request):
    wishs=Wish.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/wish.html',{'wishs':wishs})

def wish_detail(request,pk):
    wish = get_object_or_404(Wish, pk=pk)
    return render(request, 'blog/details/wish_detail.html',{'wish':wish})
@login_required
def wish_new(request):
    if request.method == "POST":
        form = WishForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('wish_detail', pk=post.pk)
    else:
        form = WishForm()
    return render(request, 'blog/form/wish_edit.html', {'form': form})
@login_required
def wish_edit(request, pk):
    wish = get_object_or_404(Wish, pk=pk)
    if request.method == "POST":
        form = WishForm(request.POST, instance=wish)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.save()
            return redirect('wish_detail', pk=wish.pk)
    else:
        form =WishForm(instance=wish)
    return render(request, 'blog/form/wish_edit.html', {'form': form})

def inspiration(request):
    inspirations=Inspiration.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/inspiration.html',{'inspirations':inspirations})

def inspiration_detail(request,pk):
    inspiration = get_object_or_404(Inspiration, pk=pk)
    return render(request, 'blog/details/inspiration_detail.html',{'inspiration':inspiration})
@login_required
def inspiration_new(request):
    if request.method == "POST":
        form = InspirationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('inspiration_detail', pk=post.pk)
    else:
        form = InspirationForm()
    return render(request, 'blog/form/inspiration_edit.html', {'form': form})
@login_required
def inspiration_edit(request, pk):
    inspiration = get_object_or_404(Inspiration, pk=pk)
    if request.method == "POST":
        form = InspirationForm(request.POST, instance=inspiration)
        if form.is_valid():
            inspiration = form.save(commit=False)
            inspiration.save()
            return redirect('inspiration_detail', pk=inspiration.pk)
    else:
        form =InspirationForm(instance=inspiration)
    return render(request, 'blog/form/inspiration_edit.html', {'form': form})

def reference(request):
    references = Reference.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/reference.html',{'references':references})

def reference_detail(request,pk):
    reference = get_object_or_404(Reference, pk=pk)
    return render(request, 'blog/details/reference_detail.html',{'reference':reference})
@login_required
def reference_new(request):
    if request.method == "POST":
        form = ReferenceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('reference_detail', pk=post.pk)
    else:
        form = ReferenceForm()
    return render(request, 'blog/form/reference_edit.html', {'form': form})
@login_required
def reference_edit(request, pk):
    reference = get_object_or_404(Reference, pk=pk)
    if request.method == "POST":
        form = ReferenceForm(request.POST, instance=reference)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.save()
            return redirect('reference_detail', pk=reference.pk)
    else:
        form =ReferenceForm(instance=reference)
    return render(request, 'blog/form/reference_edit.html', {'form': form})

def trophy(request):
    trophys = Todo_Trophy.objects.filter(success=True).order_by('date')
    return render(request, 'blog/trophy.html',{'trophys':trophys})

def trophy_detail(request,pk):
    trophy = get_object_or_404(Todo_Trophy, pk=pk)
    return render(request, 'blog/details/trophy_detail.html',{'trophy':trophy})
@login_required
def trophy_new(request):
    if request.method == "POST":
        form = Todo_TrophyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('trophy_detail', pk=post.pk)
    else:
        form = Todo_TrophyForm()
    return render(request, 'blog/form/trophy_edit.html', {'form': form})
@login_required
def trophy_edit(request, pk):
    todo_trophy = get_object_or_404(Todo_Trophy, pk=pk)
    if request.method == "POST":
        form = Todo_TrophyForm(request.POST, instance=todo_trophy)
        if form.is_valid():
            todo_trophy = form.save(commit=False)
            todo_trophy.save()
            return redirect('trophy_detail', pk=todo_trophy.pk)
    else:
        form =Todo_TrophyForm(instance=todo_trophy)
    return render(request, 'blog/form/trophy_edit.html', {'form': form})
