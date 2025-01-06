from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from book.models import CustomUser
from django.http import HttpResponse  
from book.functions.functions import handle_uploaded_file  
from .models import UploadedFile
from .form import UploadedFileForm
from django.http import JsonResponse
from .utils.db_operations import fetch_data
import logging
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser


# Serializer for User model
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Viewset for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer  # Assuming you have a serializer named UserSerializer




def index(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save file and metadata to the database
            uploaded_file = UploadedFile(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                visibility=form.cleaned_data['visibility'],
                cost=form.cleaned_data['cost'],
                year_published=form.cleaned_data['year_published'],
                file=request.FILES['file']
            )
            uploaded_file.save()
            return HttpResponse("File uploaded successfully with metadata!")
    else:
        form = UploadedFileForm()
    return render(request, "book/apexcharts.html", {'form': form})
    
def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'login.html')  # Directly render the index.html if the user is logged in

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')  # Render the index.html after successful login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


logger = logging.getLogger(__name__)

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

        # Log registration details for debugging
        logger.debug(f'Username: {username}, Email: {email}, First Name: {first_name}, Last Name: {last_name}')

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
            password=make_password(password),  # Ensure password is hashed
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

            # Create JWT token after successful registration
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Optionally send the token to the user or store it in response
            response = JsonResponse({
                "message": "Account created successfully! Please log in.",
                "access_token": access_token,
            })
            return response
        except Exception as e:
            logger.error(f"Error creating account: {str(e)}")
            messages.error(request, f"Error creating account: {str(e)}")
    return render(request, 'register.html')


def fetch_data_view(request):
    data = fetch_data()
    return HttpResponse('Data fetched')


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


from django.shortcuts import render

# Example for the first few HTML files
def advanced_components_view(request):
    return render(request, 'book/advanced-components.html')

def apexcharts_view(request):
    return render(request, 'book/apexcharts.html')

def basic_table_view(request):
    # Filter users who have opted for public visibility
    users = CustomUser.objects.filter(public_visibility=True)

    # Render the 'basic-table.html' template with the filtered users
    return render(request, 'book/basic-table.html', {'users': users})

