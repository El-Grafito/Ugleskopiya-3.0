from django.shortcuts import render, redirect
from apps.category.models import Category
from apps.post.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import KittyForm, PostForm
from apps.user.models import UserDop

def main(request):
    posts = Post.objects.all()
    user = request.user
    context = {
        'posts': posts,
        'user': user
    }
    return render(request, 'main.html', context)

def info(request):
    return render(request, 'info.html')

@login_required()
def user(request, username):
    user = request.user
    userP = User.objects.get(username=username)
    posts = Post.objects.filter(user=userP)
    if request.user == userP:
        return redirect('profil')
    context = {
        'user': user,
        'userP': userP,
        'posts': posts,
    }
    return render(request, 'user.html', context)

@login_required()
def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)

def category(request, slug):
    user = request.user
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)
    context = {
        'category': category,
        'posts': posts,
        'user': user
    }
    return render(request, 'category.html', context)

@login_required()
def profil(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            category_list = []
            if form.cleaned_data['category']:
                categorys = form.cleaned_data['category'].split(' ')
                for category in categorys:
                    if Category.objects.filter(title=category).exists():
                        category_list.append(Category.objects.get(title=category))
                    else:
                        Catcat = Category.objects.create(title=category)
                        category_list.append(Catcat)
            post.save()                              # Заметка первая. Сейчас 1:21 ночи. Я пишу это видение, устал, сильно устал.
            for category in category_list:           # До дедлаина меньше дня, надеюсь успею
                post.category.add(category)          #Купи себе орфографичский словарь, неучь
            return redirect('profil')                #Остаось добавить удаление и изменение поста, надеюсь успею
        else:                                        #Очень надеюсь что не будут какие-то ошибки в anywhere
            messages.error(request, 'Ошибка')
    else:
        form = PostForm()
    context = {
        'user': user,
        'posts': posts,
        'form': form,
    }
    return render(request, 'profil.html', context)

@login_required()
def nazvanie_funk(request):
    user = request.user
    userD = UserDop.objects.get(user=user)
    initial = {'username': user.username, 'bio': userD.bio,}
    if request.method=='POST':
        form = KittyForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user.username = cd.get('username')
            user.save()
            userD.bio = cd.get('bio')
            image = cd.get('image')
            if image:
                userD.image.save(image.name, image, save=True)
            userD.save()
            return redirect('profil')
        else:
            messages.error(request, 'Ошибка которой не должно быть')
    else:
        form = KittyForm(initial=initial)
    context = {'form': form}
    return render(request, 'edit_user.html', context)

@login_required()
def post_delete(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if post.user == user:
        post.delete()
    return redirect('profil')

@login_required()
def post_edit(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if post.user == user:
        initial = {'title': post.title, 'text': post.text, 'category': ' '.join(post.category.values_list('title', flat=True)),}
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                post.title = cd.get('title')
                post.text = cd.get('text')
                if cd.get('image'):
                    post.image = cd.get('image')
                category_list = []
                if cd['category']:
                    categorys = form.cleaned_data['category'].split(' ')
                    for category in categorys:
                        if Category.objects.filter(title=category).exists():
                            category_list.append(Category.objects.get(title=category))
                        else:
                            Catcat = Category.objects.create(title=category)
                            category_list.append(Catcat)
                post.save()  
                post.category.clear()
                for category in category_list:      
                    post.category.add(category)
                return redirect('profil')
            else:                                       
                messages.error(request, 'Ошибка')
        else:
            form = PostForm(initial=initial)
        context = {
            'user': user,
            'post': post,
            'form': form,
        }
        return render(request, 'post_edit.html', context)
    else:
        return redirect('profil')
