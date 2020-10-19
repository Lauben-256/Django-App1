from django.contrib import admin

# Register your models here.
from .models import Question, Choice

#admin.site.register(Question)
#admin.site.register(Choice)

"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
"""

"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Questions', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
           
    ]

admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Choices', {'fields': ['choice_text']}),
        ]

admin.site.register(Choice, ChoiceAdmin)
"""
"""
class ChoiceInline(admin.StackedInline):
   model = Choice
   extra = 1
"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('Questions', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
           
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

