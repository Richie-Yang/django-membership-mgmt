from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Question, Six, Visit, Register
from .forms import RegisterForm

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the quiz index.")


@login_required()
def play(request):
    question = Question.objects.all()
    # 當測驗者提出表單(submit)
    if request.method == 'POST':
        # 匯集測驗者每題的得分
        total = []
        for q in question:
            # 獲得測驗者選擇的選項
            select = request.POST[str(q.id)]
            choice = q.choice_set.all().values()
            # loop四個選項
            for i in choice:
                if i['choice_text'] == select:
                    # 選項對照的得分
                    total.append(i['score'])
        # 傳送表單完就跳轉至結果畫面
        return redirect('result', total=sum(total))
    return render(request, 'play.html', {'question': question})


def result(request, total):
    score = total
    six = Six.objects.all()
    for s in six:
        if score in range(s.range_start, s.range_end):
            # 判斷測驗分數位在哪個區間
            grade = s.grade
            photo = s.photo
        else:
            pass
    return render(request, 'result.html', locals())


def visitor_count(request):
    visit_model = Visit.objects.get(pk=1)
    if 'quiz' not in request.session:
        request.session['quiz'] = True
        visit_model.times += 1
    visit_model.save()
    context = {'visit_template': visit_model.times}
    return render(request, 'visitor_count.html', context)


def register_create_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        Register.objects.create(form.cleaned_data)
        form = RegisterForm
    context = {
        'form': form
    }
    return render(request, 'register_create.html', context)


def register(request):
    # 當使用者提交資料
    if request.method == 'POST':
        # 內建的form，model為User。
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quiz')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'register.html', context)


def post_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_staff is False:
            auth.login(request, user)
            return redirect('/login/')
        elif user and user.is_staff is True:
            auth.login(request, user)
            return redirect('/quiz/')
        else:
            return redirect('/login/')
    else:
        return render(request, 'login.html', locals())
