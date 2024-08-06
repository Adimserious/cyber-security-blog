from django.shortcuts import render
from .models import About_page


# Create your views here.
def about_page(request):
    """
    Renders the updated information of the Cybersecurity Mindset.
    """

    about = About_page.objects.all().order_by('-updated').first()

    return render(
        request,
        "about_page/about_page.html",
        {"about": about, }

    )
