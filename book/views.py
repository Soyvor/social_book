from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')  # Redirect to the dashboard if already logged in

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirec('/')  # Redirect to the dashboard (root URL)
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        public_visibility = bool(request.POST.get("public_visibility", False))
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        state = request.POST.get("state")

        # Helper functions for derived fields
        def get_location(city, state):
            return f"{city}, {state}"

        def get_birth_year(dob):
            return dob.split("-")[0]  # Assuming dob is in YYYY-MM-DD format

        location = get_location(city, state)
        birth_year = get_birth_year(dob)

        # Create and save the user
        user = CustomUser(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,  # Ensure proper hashing
            dob=dob,
            gender=gender,
            city=city,
            state=state,
            location=location,
            birth_year=birth_year,
            public_visibility=public_visibility,
        )
        try:
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return HttpResponseRedirect('/book/login/')  # Redirect to login page after successful registration
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")

    return render(request, 'register.html')



# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  # Redirect to login page


# Dashboard view (protected)
# views.py

# Ensures the user is logged in
def dashboard(request):
    return render(request, 'index.html')  # Path to your index.html



# Error views
def error_400(request, exception):
    return render(request, 'errors/400.html', status=400)

def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    return render(request, 'errors/500.html', status=500)

def error_503(request):
    return render(request, 'errors/503.html', status=503)
