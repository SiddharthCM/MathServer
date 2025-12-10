# Ex.04 Design a Website for Server Side Processing
## Date:10.12.25

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```

sidmaths1.html:
<html>
<head>
    <title>Mileage Calculator</title>
    <style>
        body 
        {
            background: linear-gradient(orange, pink);
        }
        
        .Calmile
        {
            text-align: center;
            width: 40%;
            background: linear-gradient(pink,cyan);
            border: solid 4px whitesmoke;
            padding-left: 20px;
            margin-left: 450px;
            margin-top: 150
        }
        footer
        {
            bottom: 0;
            position: fixed;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="Calmile">
        <h2><u>Calculate Mileage</u></h2>
        <h3><i>Siddharth CM 25009900</i></h3>

        <form method="post">
            {% csrf_token %}
            <label>Distance Travelled</label><br>
            <input type="number" name="kilometer"> km<br><br>
            <label>Liters Consumed</label><br>
            <input type="number" name="liters"> l<br><br>
            <button type="submit">Mileage</button>
            <br>
            <h2><u>Mileage: {{miles}}</u></h2>
            <br>
        </form>
    </div>
</body>
<footer>SiddhuMiles&copy;</footer>
</html>

views.py:

from django.shortcuts import render
def fmiles(request):
    km = int(request.POST.get('kilometer', 0))
    l = int(request.POST.get('liters', 0))
    miles = km / l if request.method == 'POST' else 0
    print("kilometer=",km)
    print("liters=",l)
    print("Mileage=",miles)
    return render(request, 'mathapp/sidmaths1.html', {'km': km, 'l': l, 'miles': miles})

urls.py:

from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.fmiles, name='fmiles'),
]

```
## OUTPUT - SERVER SIDE:
![alt text](image.png)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2025-12-10 113149.png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
