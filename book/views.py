from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from book.models import CustomUser


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

def blank_view(request):
    return render(request, 'book/blank.html')

def blog_detail_view(request):
    return render(request, 'book/blog-detail.html')

def blog_view(request):
    return render(request, 'book/blog.html')

def calendar_view(request):
    return render(request, 'book/calendar.html')

def chat_view(request):
    return render(request, 'book/chat.html')

def color_settings_view(request):
    return render(request, 'book/color-settings.html')

def contact_directory_view(request):
    return render(request, 'book/contact-directory.html')

def custom_icon_view(request):
    return render(request, 'book/custom-icon.html')

def datatable_view(request):
    return render(request, 'book/datatable.html')

def faq_view(request):
    return render(request, 'book/faq.html')

def font_awesome_view(request):
    return render(request, 'book/font-awesome.html')

def forgot_password_view(request):
    return render(request, 'book/forgot-password.html')

def form_basic_view(request):
    return render(request, 'book/form-basic.html')

def form_pickers_view(request):
    return render(request, 'book/form-pickers.html')

def form_wizard_view(request):
    return render(request, 'book/form-wizard.html')

def foundation_view(request):
    return render(request, 'book/foundation.html')

def gallery_view(request):
    return render(request, 'book/gallery.html')

def getting_started_view(request):
    return render(request, 'book/getting-started.html')

def highchart_view(request):
    return render(request, 'book/highchart.html')

def html5_editor_view(request):
    return render(request, 'book/html5-editor.html')

def image_cropper_view(request):
    return render(request, 'book/image-cropper.html')

def image_dropzone_view(request):
    return render(request, 'book/image-dropzone.html')

def index_view(request):
    return render(request, 'book/index.html')

def index2_view(request):
    return render(request, 'book/index2.html')

def introduction_view(request):
    return render(request, 'book/introduction.html')

def invoice_view(request):
    return render(request, 'book/invoice.html')

def ionicons_view(request):
    return render(request, 'book/ionicons.html')

def pricing_table_view(request):
    return render(request, 'book/pricing-table.html')

def product_detail_view(request):
    return render(request, 'book/product-detail.html')

def product_view(request):
    return render(request, 'book/product.html')

def profile_view(request):
    return render(request, 'book/profile.html')

def reset_password_view(request):
    return render(request, 'book/reset-password.html')

def sitemap_view(request):
    return render(request, 'book/sitemap.html')

def themify_view(request):
    return render(request, 'book/themify.html')

def third_party_plugins_view(request):
    return render(request, 'book/third-party-plugins.html')

def ui_buttons_view(request):
    return render(request, 'book/ui-buttons.html')

def ui_cards_hover_view(request):
    return render(request, 'book/ui-cards-hover.html')

def ui_cards_view(request):
    return render(request, 'book/ui-cards.html')

def ui_carousel_view(request):
    return render(request, 'book/ui-carousel.html')

def ui_list_group_view(request):
    return render(request, 'book/ui-list-group.html')

def ui_modals_view(request):
    return render(request, 'book/ui-modals.html')

def ui_notification_view(request):
    return render(request, 'book/ui-notification.html')

def ui_progressbar_view(request):
    return render(request, 'book/ui-progressbar.html')

def ui_range_slider_view(request):
    return render(request, 'book/ui-range-slider.html')

def ui_sweet_alert_view(request):
    return render(request, 'book/ui-sweet-alert.html')

def ui_tabs_view(request):
    return render(request, 'book/ui-tabs.html')

def ui_timeline_view(request):
    return render(request, 'book/ui-timeline.html')

def ui_tooltip_popover_view(request):
    return render(request, 'book/ui-tooltip-popover.html')

def ui_typography_view(request):
    return render(request, 'book/ui-typography.html')

def video_player_view(request):
    return render(request, 'book/video-player.html')
