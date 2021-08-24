from django.contrib import admin

from .models import Link,SideBar
# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title','href','status','weight','owner','created_time')
    fields = ('title','href','status','weight')
    
    #定义登录账户为作者
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin,self).save_model(request,obj,form,change)

@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title','display_type','content','status','owner','created_time')
    fields = ('title','display_type','content','status')

    #定义登录账户为作者
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request,obj,form,change)