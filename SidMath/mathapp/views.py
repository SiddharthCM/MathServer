from django.shortcuts import render
def fmiles(request):
    km = int(request.POST.get('kilometer', 0))
    l = int(request.POST.get('liters', 0))
    miles = km / l if request.method == 'POST' else 0
    print("kilometer=",km)
    print("liters=",l)
    print("Mileage=",miles)
    return render(request, 'mathapp/sidmaths1.html', {'km': km, 'l': l, 'miles': miles})
