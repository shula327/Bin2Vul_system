from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def binary_compare(request):
    result = None
    if request.method == 'POST':
        # Comparison
        pass
    return render(request, 'core/binary_compare.html', {'result': result})

@login_required
def vulnerability_analysis(request):
    vulnerabilities = None
    if request.method == 'POST':
        # Analysis
        pass
    return render(request, 'core/vulnerability_analysis.html', {'vulnerabilities': vulnerabilities}) 