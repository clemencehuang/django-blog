from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)

# 1) When we create a custom model and we want it to appear in the admin site, then we need to tell Django by registering it in the admin.py file. That is what admin.site.register does.
# 2) If you said that Post refers to the Post model we just created, then well done! You're absolutely right. We import our custom Post model on line 2.
# 3) The dot in front of models on line 2 indicates that we are importing Post from a file named models, which is in the same directory as our admin.py file. If you have multiple models 
# that you want to import, then you can separate them with a comma. For example, in future topics, you will create a Comment model, which will need to be imported at that point.
# admin.site.register(Post)
# admin.site.register(Comment)
# It is worth noting that the admin.site.register method takes only one argument. If you are registering multiple models, you would need a separate line for each model. 
# The code for multiple models would look like this:
# admin.site.register(Post)
# admin.site.register(Comment)

