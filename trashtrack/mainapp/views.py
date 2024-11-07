from django.shortcuts import render, redirect
from .models import SmartBin, Vehicle, DumpingArea, Company
from .forms import CompanySignupForm
from django.contrib.auth import login

def company_signup(request):
    if request.method == 'POST':
        form = CompanySignupForm(request.POST)
        if form.is_valid():
            company_profile = form.save()
            login(request, company_profile.user)
            return redirect('company_portal')
    else:
        form = CompanySignupForm()
    return render(request, 'company_signup.html', {'form': form})

# Dashboard view to show all key data
def dashboard(request):
    context = {
        "bins": SmartBin.objects.all(),
        "vehicles": Vehicle.objects.all(),
        "waste_types": DumpingArea.objects.all(),
    }
    return render(request, "dashboard.html", context)

def map_view(request):
    bins = list(SmartBin.objects.values('bin_type', 'current_fill_level', 'location', 'latitude', 'longitude'))
    return render(request, "map.html", {"bins": bins})

# Smart Bins view
def smart_bins(request):
    bins = SmartBin.objects.all()
    return render(request, "smart_bins.html", {"bins": bins})

# Tracking and Collection view
def tracking(request):
    vehicles = Vehicle.objects.all()
    return render(request, "tracking.html", {"vehicles": vehicles})

# Dumping Area Management view
def dumping_area(request):
    waste_types = DumpingArea.objects.all()
    return render(request, "dumping_area.html", {"waste_types": waste_types})

# Company Portal view
def company_portal(request):
    companies = Company.objects.all()
    return render(request, "company_portal.html", {"companies": companies})
