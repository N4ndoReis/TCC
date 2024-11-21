from django.contrib import admin
from tcc.models import Register,Login, Create, BringNote

class Registers(admin.ModelAdmin):
    list_display = ('id','name','email','date_of_birth','cell' )
    list_display_links = ('id','name',)
    list_per_page = 20
    search_fields = ('name','email',)
    ordering = ('name',)

admin.site.register(Register,Registers)

class Logins(admin.ModelAdmin):
    list_display = ('email','password' )
    list_display_links = ('email', 'password',)
    list_per_page = 20
    search_fields = ('email',)

admin.site.register(Login,Logins)

class Creates(admin.ModelAdmin):
    list_display = ('task', 'description', 'priority')
    list_display_links = ('task', 'description',)
    search_fields = ('task',)
    
admin.site.register(Create,Creates)

class BringNotes(admin.ModelAdmin):
    list_display = ('title','content','created_in','updated_in')
    list_display_links = ('title','content',)
    search_fields = ('title',)
    
admin.site.register(BringNote,BringNotes)