from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User 
from .models import ManagementProfile 
from .forms import ManagementProfileForm
from .models import GalleryImage
from .forms import GalleryImageForm

@login_required
def gallery_crud(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Hash the password before saving
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/gallery_crud/')  # Redirect to your main page
    else:
        form = UserForm()

    return render(request, 'management/crud.html', {'form': form})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash password
            user.save()
            return redirect('/gallery_crud/')  # stay on the page or redirect elsewhere
    else:
        form = UserForm()
    return render(request, 'management/crud.html', {'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'management/user_list.html', {'users': users})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('/user_list/')


def add_profile(request):
    if request.method == "POST":
        form = ManagementProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save to DB
            return redirect('/gallery_crud/')  # Redirect back to your panel
    else:
        form = ManagementProfileForm()
    return render(request, 'frontend/about.html', {'form': form})

@login_required
def management_updates_list(request):
    # Get all management updates, newest first
    updates = ManagementProfile.objects.all().order_by('-created_at')
    
    # Pass them to template
    return render(request, 'management/updates_list.html', {'updates': updates})

@login_required
def add_management_update(request):
    if request.method == 'POST':
        form = ManagementProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/management/updates_list/')  # redirect after adding
    else:
        form = ManagementProfileForm()
    return render(request, '/management/add_update.html/', {'form': form})

def delete_management_update(request, pk):
    update = get_object_or_404(ManagementProfile, pk=pk)
    update.delete()
    return redirect('/management_updates/')

def gallery_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        section = request.POST.get("section")

        if title and image and section:
            GalleryImage.objects.create(
                title=title,
                image=image,
                section=section,
                uploaded_by=request.user
            )
            return redirect("gallery_list")  # prevent duplicate submission

    # **Filter images by section correctly**
    first_section_images = GalleryImage.objects.filter(section="first").order_by("created_at")
    second_section_images = GalleryImage.objects.filter(section="second").order_by("created_at")
    third_section_images = GalleryImage.objects.filter(section="third").order_by("created_at")
    
    context = {
        "first_section_images": first_section_images,
        "second_section_images": second_section_images,
        "third_section_images": third_section_images,
    }

    return render(request, "management/gallery_list.html", context)

from django.shortcuts import render, redirect
from .models import Career

def add_career(request):
    if request.method == "POST":
        title = request.POST.get("title")
        location = request.POST.get("location")
        job_type = request.POST.get("job_type")
        duties = request.POST.get("duties")
        apply_note = request.POST.get("apply_note")

        Career.objects.create(
            title=title,
            location=location,
            job_type=job_type,
            duties=duties,
            apply_note=apply_note
        )

        return redirect("career_list")   # redirect to list page

    return render(request, "crud.html")   # show the add form



def career_list(request):
    careers = Career.objects.all().order_by("-created_at")
    return render(request, "management/career_list.html", {"careers": careers})

def delete_career(request, pk):
    Career.objects.filter(id=pk).delete()
    return redirect("/career_list/")


@login_required
def delete_image(request, pk):
    img = get_object_or_404(GalleryImage, pk=pk)
    img.delete()
    return redirect('gallery_list')

@login_required
def delete_image(request, pk):
    img = get_object_or_404(GalleryImage, pk=pk)
    img.delete()
    return redirect('gallery_list')