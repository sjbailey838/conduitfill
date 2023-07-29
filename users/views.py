from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm 


def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def addCable(request):
    form = CableForm()
    form1 = ConduitForm()
    form2 = CableRunForm()
    form3 = ConduitRunForm()
    conduits = Conduit.objects.all()
    cables = Cable.objects.all()
    conduitruns = ConduitRun.objects.all()
    cableruns = CableRun.objects.all()
    print(conduitruns,"this is the cables assigned to this conduit")
    print(cableruns,"is the cable runs")
    cablelist = []
    for i in range(len((conduitruns))):
        print(conduitruns[i].conduittag,conduitruns[i].cable.all())
        cablelist.append(conduitruns[i].cable.all()) 
    print(cablelist, "is your list of cables")
    cablequery = conduitruns[0].cable.all()
    # print(conduitruns)
    # print(cablequery)
    if request.method == 'POST':
        # print(request.POST)
        if 'addcable' in request.POST:
            form = CableForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'addconduit' in request.POST:
            form1 = ConduitForm(request.POST)
            if form1.is_valid():
                form1.save()
        elif 'projectcable' in request.POST:
            form2 = CableRunForm(request.POST)
            if form2.is_valid():
                form2.save()
        elif 'projectconduit' in request.POST:
            form3 = ConduitRunForm(request.POST)
            if form3.is_valid():
                form3.save()
    context = {'form':form,'form1':form1,'conduits':conduits, 'cables':cables,
            'conduitruns':conduitruns,'cableruns':cableruns,'form2':form2,'form3':form3, 'cablelist':cablelist
               }
    return render(request, 'users/addcable.html',context)
    

    # if form.is_valid():
    #     form.save()
    #     return redirect('user-profile', pk=user.id)

