from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/index.html', context)

def create(request):
    # 1. get방식으로 데이터를 입력할 수 있는 form을 요청한다.
    # 4. 사용자가 데이터를 입력해서 post 요청을 보낸다.
    # 9. 사용자가 적절한데이터를 입력해서 post 요청을 보낸다.
    if request.method == "POST":
        # 5. 데이터를 받아서 PostForm을 인스턴스화 한다.
        # 10. 데이터를 받아서 PostForm을 인스턴스화 한다.
        form = PostForm(request.POST)
        # 6. 데이터 검증을 한다.
        # 11. 데이터 검증을 한다.
        if form.is_valid():
            # 12. 적절한 데이터가 들어온다. 저장을 하고 인덱스로 보낸다.
            form.save()
            return redirect("posts:index")
        else:
            # 7. 적절하지 않은 데이터가 들어온다.
            pass
    else:
        # 2. PostForm을 인스턴스화 해서 form 변수에 저장
        form = PostForm()

    context = {
        'form':form
    }
    # 3. 만들어진 form을 create.html에 담아서 전송
    # 8. 사용자가 정확하게 입력한 데이터를 유지한 상태의 form을 전송
    return render(request, 'posts/form.html', context)

def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:index")
        else:
            pass
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'form':form})

def delete(request, post_id):
    return redirect("posts:")
