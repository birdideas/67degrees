import time
import random
from django.shortcuts import render
from django.http import JsonResponse
from .celebrities import search_celebrities, CELEBRITIES
import gemini
from django.views.decorators.csrf import csrf_exempt

# Global in-memory rate limiter
RATE_LIMIT = 5          # requests
RATE_PERIOD = 60        # seconds
rate_data = {
    "last_reset": time.time(),
    "count": 0
}

def check_global_rate_limit():
    now = time.time()
    if now - rate_data["last_reset"] > RATE_PERIOD:
        # Reset every RATE_PERIOD seconds
        rate_data["last_reset"] = now
        rate_data["count"] = 0
    rate_data["count"] += 1
    return rate_data["count"] <= RATE_LIMIT

def index(request):
    featured = random.sample(CELEBRITIES, min(6, len(CELEBRITIES)))
    return render(request, "search/index.html", {"featured": featured})

def results(request):
    return render(request, "search/results.html")

@csrf_exempt
def api_connections(request):
    if not check_global_rate_limit():
        return JsonResponse({"error": "Too many requests. Try again later."}, status=429)

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