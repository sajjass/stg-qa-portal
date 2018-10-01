from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template import RequestContext

from .models import dailystats
from .forms import dailystatusForm, updatedailystatusForm


def home(request):
    daily_stats = dailystats.objects.all()
    return render(request, 'dailystatus/home.html', {'daily_stats' : daily_stats})

def add_dailystatus(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = dailystatusForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            dailystatus_item = form.save(commit=False)
            dailystatus_item.save()
            # redirect to a new URL:
            messages.success(request, 'Your daily status info has been Submitted Successfully!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Please correct the error below.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = dailystatusForm()

    return render(request, 'dailystatus/registration_form.html', {'form':form})

def edit_dailystatus(request, pk):
    edit_stats = dailystats.objects.get(pk = pk)

    if request.method == "POST":
        update_form = updatedailystatusForm(data=request.POST, instance=edit_stats)
        if update_form.is_valid():
            edit_dailystatus_item = update_form.save(commit=False)
            edit_dailystatus_item.save()
            # redirect to a new URL:
            messages.success(request, 'Your daily status info has been Updated Successfully!')
            return HttpResponseRedirect('/')
    else:
        update_form = updatedailystatusForm(instance=edit_stats)
    return render(request, 'dailystatus/edit_dailystatus_info.html', {'form': update_form})

def delete_dailystatus(request, pk):
    dailystats.objects.get(pk = pk).delete()
    messages.success(request, 'Your daily status info has been deleted Successfully!')
    return HttpResponseRedirect('/')
