from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from customusers.forms import CustomUserForm


class LoginView(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        user = authenticate(
            email=request.POST['email'],
            password=request.POST['password']
        )
        if user:
            # handle successful login
            login(request, user)
            return render(request, 'index.html')
        else:
            error = "Invalid email or password"
            return render(request, 'login.html', {'error': error, 'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
