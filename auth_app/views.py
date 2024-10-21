from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from seller.models import Store


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_type = request.POST.get('user_type') 
        if form.is_valid():
            user = form.save()
    
            profile, created = Profile.objects.get_or_create(user=user)
            if user_type == 'seller':
                profile.is_seller = True
            elif user_type == 'buyer':
                profile.is_buyer = True
            profile.save()

            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            login(request, user)  
            try:
                profile = Profile.objects.get(user=user)  
                if profile.is_buyer:
                    return redirect('home')  
                elif profile.is_seller:
                    try:
                        store = Store.objects.get(seller=user)
                        if store.is_approved:
                            return redirect('seller_profile')  
                        else:
                            return redirect('store_request')  
                    except Store.DoesNotExist:
                        return redirect('store_request')  
            
            
            except Profile.DoesNotExist:
                return redirect('signup')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')

