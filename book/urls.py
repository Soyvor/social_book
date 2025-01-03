from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('advanced-components/', views.advanced_components_view, name='advanced_components'),
    path('apexcharts/', views.apexcharts_view, name='apexcharts'),
    path('basic-table/', views.basic_table_view, name='basic_table'),
    path('blank/', views.blank_view, name='blank'),
    path('blog-detail/', views.blog_detail_view, name='blog_detail'),
    path('blog/', views.blog_view, name='blog'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('chat/', views.chat_view, name='chat'),
    path('color-settings/', views.color_settings_view, name='color_settings'),
    path('contact-directory/', views.contact_directory_view, name='contact_directory'),
    path('custom-icon/', views.custom_icon_view, name='custom_icon'),
    path('datatable/', views.datatable_view, name='datatable'),
    path('faq/', views.faq_view, name='faq'),
    path('font-awesome/', views.font_awesome_view, name='font_awesome'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('form-basic/', views.form_basic_view, name='form_basic'),
    path('form-pickers/', views.form_pickers_view, name='form_pickers'),
    path('form-wizard/', views.form_wizard_view, name='form_wizard'),
    path('foundation/', views.foundation_view, name='foundation'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('getting-started/', views.getting_started_view, name='getting_started'),
    path('highchart/', views.highchart_view, name='highchart'),
    path('html5-editor/', views.html5_editor_view, name='html5_editor'),
    path('image-cropper/', views.image_cropper_view, name='image_cropper'),
    path('image-dropzone/', views.image_dropzone_view, name='image_dropzone'),
    path('index/', views.index_view, name='index'),
    path('index2/', views.index2_view, name='index2'),
    path('introduction/', views.introduction_view, name='introduction'),
    path('invoice/', views.invoice_view, name='invoice'),
    path('ionicons/', views.ionicons_view, name='ionicons'),
    path('pricing-table/', views.pricing_table_view, name='pricing_table'),
    path('product-detail/', views.product_detail_view, name='product_detail'),
    path('product/', views.product_view, name='product'),
    path('profile/', views.profile_view, name='profile'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('sitemap/', views.sitemap_view, name='sitemap'),
    path('themify/', views.themify_view, name='themify'),
    path('third-party-plugins/', views.third_party_plugins_view, name='third_party_plugins'),
    path('ui-buttons/', views.ui_buttons_view, name='ui_buttons'),
    path('ui-cards-hover/', views.ui_cards_hover_view, name='ui_cards_hover'),
    path('ui-cards/', views.ui_cards_view, name='ui_cards'),
    path('ui-carousel/', views.ui_carousel_view, name='ui_carousel'),
    path('ui-list-group/', views.ui_list_group_view, name='ui_list_group'),
    path('ui-modals/', views.ui_modals_view, name='ui_modals'),
    path('ui-notification/', views.ui_notification_view, name='ui_notification'),
    path('ui-progressbar/', views.ui_progressbar_view, name='ui_progressbar'),
    path('ui-range-slider/', views.ui_range_slider_view, name='ui_range_slider'),
    path('ui-sweet-alert/', views.ui_sweet_alert_view, name='ui_sweet_alert'),
    path('ui-tabs/', views.ui_tabs_view, name='ui_tabs'),
    path('ui-timeline/', views.ui_timeline_view, name='ui_timeline'),
    path('ui-tooltip-popover/', views.ui_tooltip_popover_view, name='ui_tooltip_popover'),
    path('ui-typography/', views.ui_typography_view, name='ui_typography'),
    path('video-player/', views.video_player_view, name='video_player'),
]


