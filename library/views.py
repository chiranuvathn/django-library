from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm

def sign_up(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form': form}

    return render(request, 'registration/sign_up.html', context)
