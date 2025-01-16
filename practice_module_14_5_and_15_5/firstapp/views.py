from django.shortcuts import render,redirect
from firstapp.forms import ExampleForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.
def home(request):
   if request.method == 'POST':
       form = ExampleForm(request.POST)
       if form.is_valid():
           form.save()
           print(form.cleaned_data)
           
   else:
        form = ExampleForm()
   return render(request,'home.html',{'form':form})


def contact(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            subject = "Contact"
            body = {
                'model_choice': form.cleaned_data['model_choice'],
                'model_choices': ', '.join(str(choice) for choice in form.cleaned_data['model_choices']),
            }
            message = "\n".join(f"{key}: {value}" for key, value in body.items())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("contact")
    else:
        form = ExampleForm()
    return render(request, "contact.html", {'form': form})
