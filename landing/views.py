from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request,'index.html')

def mostrar_pombos(request):
    return render(request, 'pombos.html')

def mostrar_rolezinho(request):
    roles = ['bailão', 'shopping união', 'quermesse da paroquia de são joão','calçadão de osasco','SESC']
    bairro = 'rochidale'
    return render(request, 'rolezinho.html',{'roles':roles,'bairro':bairro})


def mostrar_assalto(request):
    armamento = ['pistola','fuzil','bazuca','pombo','faca']
    return render(request, 'asalto.html',{'armamento':armamento})