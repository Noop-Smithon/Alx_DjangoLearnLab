from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.shortcuts import render
from .models import UserProfile

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profille': user_profile})