from django.contrib import admin
from .models import Question, Choice


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


admin.site.register(Question, QuestionAdmin)
