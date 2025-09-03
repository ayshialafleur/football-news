from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406365351',
        'name': 'Ayshia La Fleur Felizia',
        'class': 'KKI'
    }

    return render(request, "main.html", context)