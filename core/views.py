from django.shortcuts import render, redirect
from .forms import SignUpForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# def authenticate(username=None, password=None):
#     try:
#         user_profile = UserProfile.objects.get(username=username)
#         print(f"\n\n{user_profile}\n\n")
#         if user_profile.check_password(password):
#             return user_profile.user
#     except UserProfile.DoesNotExist:
#         return None
#     except Exception as e:
#         return None

def Home(request):
    authenticated = request.user.is_authenticated if hasattr(request, 'user') else False
    context = {
        'auth': authenticated,
    }
    if authenticated:
        context['profile_picture'] = request.user.profile_picture
    return render(request, 'core/index.html', context)

def About(request):
    return render(request, 'core/about.html')

def Contact(request):
    return render(request, 'core/contact.html')

def Signup(request):
    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('Login')
            messages.error(request, 'Please Enter Valid Input Only!')
        else:
            form = SignUpForm()     
        return render(request, 'core/signup.html', {'form': form})
    except Exception as e:
        print(e.__str__())
        form = SignUpForm()
        messages.error(request, 'Something Went Wrong')
        return render(request, 'core/signup.html', {'form': form})

def Login(request):
    try:
        if request.method == 'POST':
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request=request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('Home')
                else:
                    messages.error(request, 'Wrong username or password.')
            else:
                messages.error(request, 'Form is not valid.')
        else:
            form = UserLoginForm()
        return render(request, 'core/login.html', {'form': form})
    except Exception as e:
        print(e)
        messages.error(request, 'Something went wrong.')
        form = UserLoginForm()
        return render(request, 'core/login.html', {'form': form})