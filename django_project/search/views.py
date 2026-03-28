import random
from django.shortcuts import render
from django.http import JsonResponse
from .celebrities import search_celebrities, CELEBRITIES

import gemini

def index(request):
    featured = random.sample(CELEBRITIES, min(6, len(CELEBRITIES)))
    return render(request, "search/index.html", {"featured": featured})

def suggestions(request):
    query = request.GET.get("q", "").strip()
    results = search_celebrities(query)
    return JsonResponse({"results": results})

def results(request):
    celebrity_name = request.GET.get("q", "").strip()
    gemini.send_prompt(celebrity_name)

    query = request.GET.get("q", "").strip()
    celebrities = search_celebrities(query, limit=20) if query else []
    return render(request, "search/results.html", {
        "query": query,
        "celebrities": celebrities,
        "count": len(celebrities),
    })

