from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def main(request):
    return render(request, 'login.html')

@login_required
def hello(request):
    """Login complete view, displays user data"""
    user = User.objects.get(username=request.user)
    return render(request, 'hello.html', { 'first': user.first_name,
                                           'last': user.last_name})
