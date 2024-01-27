from django.urls import path
from .views import contact_form, success_page, messages

urlpatterns = [
    path('', contact_form, name='contact_form'),
    path('success/', success_page, name='success'),
    path('messages/', messages, name='message'),
]