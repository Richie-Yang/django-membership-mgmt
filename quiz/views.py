from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Six

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the quiz index.")


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
