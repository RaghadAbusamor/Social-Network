from django.shortcuts import render
from .models import Profile
from django.shortcuts import render, redirect
# Create your views here.
from .forms import DweetForm
from django.shortcuts import render
def dashboard(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
           dweet = form.save(commit=False)
           dweet.user = request.user
           dweet.save()
           return redirect("dwitter:dashboard")
    form = DweetForm()
    return render(request, "dwitter/dashboard.html", {"form": form})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
           dweet = form.save(commit=False)
           dweet.user = request.user
           dweet.save()
           return redirect("dwitter:dashboard")
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(
        request,
        "dwitter/dashboard.html",
        {"form": form, "dweets": followed_dweets},
    )

def register(request):
  if request.method == "GET":
    return render(
      request, "dwitter/register.html",
      {"form": CustomUserCreationForm}
)
  elif request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
       user = form.save()
       login(request, user)
       return redirect(reverse("dashboard"))

