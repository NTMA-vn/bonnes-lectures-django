from django.http import HttpResponse

def about(request):
    return HttpResponse("Application Bonnes Lectures, développée en TP de Framework Web, Université d’Orléans, 2026")

# Create your views here.
