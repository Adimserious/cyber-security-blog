from django.shortcuts import render
from django.contrib import messages
from .forms import RequestContactForm

# Create your views here.
def contact_me(request):
    """
    Renders the Contact page for getting in touch and staying connected.
    """
    if request.method == "POST":
        contact_form = RequestContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "All done, Contact request received! I endeavour to respond within 5 working days.")
    
    contact_form = RequestContactForm()

    return render(
        request,
        "contact/contact.html",
        {"contact_form": contact_form,},
    )
