
from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
import pytz

# 1. Welcome page
def welcome(request):
    return render(request, "welcome.html")

# 2. Users list
def users_list(request):
    users = [
        {"full_name": "Alihan Satbai", "age": 22},
        {"full_name": "Maratuly Temirbolat", "age": 30},
        {"full_name": "John Doe", "age": 25},
    ]
    return render(request, "users.html", {"users": users})

# 3. City time
def city_time(request):
    city_times = {}
    cities = {


        "Almaty": "Asia/Almaty",
        "Calgary": "America/Edmonton",
        "Moscow": "Europe/Moscow",
        "UTC": "UTC",
    }
    for city, tz in cities.items():
        city_times[city] = datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %H:%M:%S")

    return render(request, "city_time.html", {"city_times": city_times})

# 4. Counter
def counter_view(request):
    count = request.session.get("count", 0)

    if "increment" in request.GET:
        count += 1
    elif "reset" in request.GET:
        count = 0

    request.session["count"] = count
    return render(request, "counter.html", {"count": count})

# Create your views here.
