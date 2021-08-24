from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.html import format_html

from .models import Category,Tag,Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_nav','owner','created_time') # 控制列表展示的字段
    fields =('name','status','is_nav')  #控制新增页面展示的字段
    #设置登录账户为作者
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin,self).save_model(request,obj,form,change)

    #统计该分类下的文章数量
    def post_count(self,obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status','owner','created_time')
    fields = ('name','status')
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin,self).save_model(request,obj,form,change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','desc','content','status','category','owner','created_time')
    fields = ('title','desc','content','status','category','tag')
    list_display_links = []
    list_filter = ['category']
    search_fields = ['title','category__name']

    actions_on_top = True
    actions_on_bottom = True

    #编辑页面
    save_on_top = True

    #新增自定义字段
    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',reverse('admin:blog_post_change',args=(obj.jd,))
        )
    operator.short_description = '操作'

    #登录账户为作者
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin,self).save_model(request,obj,form,change)

