from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152336',
        'name': 'Filbert Aurelian Tjiaranata',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)