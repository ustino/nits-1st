from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from accounts.forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


@login_required
def profile(request):
#   if not request.user.is_authenticated():
#       return redirect(settings.LOGIN_URL + '?next=' + request.get_full_path())

    return render(request, 'accounts/profile.html')

