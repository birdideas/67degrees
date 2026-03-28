import random
from django.shortcuts import render
from django.http import JsonResponse
from .celebrities import search_celebrities, CELEBRITIES
import gemini
from django.views.decorators.csrf import csrf_exempt

def index(request):
    featured = random.sample(CELEBRITIES, min(6, len(CELEBRITIES)))
    return render(request, "search/index.html", {"featured": featured})

def results(request):
    # The page is mostly JS-driven now
    return render(request, "search/results.html")

@csrf_exempt
def api_connections(request):
    person_a = request.GET.get("a")
    person_b = request.GET.get("b")

    if not person_a or not person_b:
        return JsonResponse({"results": []})

    data = gemini.send_prompt(person_a, person_b)
    return JsonResponse({"results": data})

def suggestions(request):
    query = request.GET.get("q", "").strip()
    results = search_celebrities(query)
    return JsonResponse({"results": results})