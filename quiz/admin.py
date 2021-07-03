from django.contrib import admin
from .models import Question, Choice, Visit


class ChoiceInline(admin.StackedInline):
    # class StackedInline
    model = Choice
    # 一個問題有四個選項
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # 詳細說明參考附錄圖一
    list_display = ('id', 'question_text')
    # 詳細說明參考附錄圖二
    fieldsets = [
        (None, {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]


class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'times')
    fieldsets = [
        (None, {'fields': ['times']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Visit, VisitAdmin)



