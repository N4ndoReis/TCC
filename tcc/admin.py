from django.contrib import admin
from tcc.models import Register,Login, Create

class Registers(admin.ModelAdmin):
    list_display = ('name','email','cpf','date_of_birth','cell' )
    list_display_links = ('name', 'cpf',)
    list_per_page = 20
    search_fields = ('name',)

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