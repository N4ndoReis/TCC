from django.http import JsonResponse

def login(request):
    if request.method == 'GET':
       user = {
           'id': '1',
           'nome':'luiz'
       } 
       return JsonResponse(user)
