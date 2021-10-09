from django.shortcuts import render
from .forms import DatabaseForm
from rest_framework import viewsets
from .serializers import DatabaseSerializer
from .models import DatabaseModel


# Create your views here.
# declare the REST api view provided by the django rest framework
class DatabaseViewSet(viewsets.ModelViewSet):
    # the queryset reads all data from the selected database table and orders them by id
    queryset = DatabaseModel.objects.all().order_by('col_id')
    # the serializer is required to format the JSON response properly
    serializer_class = DatabaseSerializer


# this is our standard web form interface
def showform(request):

    """ initialize a user feedback variable """
    status = ""

    # if the user has POSTed data
    if request.method == 'POST':

        # initialize the ModelForm object
        form = DatabaseForm(request.POST or None)

        # check if our form is valid
        if form.is_valid():

            # try to save the form data to the MySQL database and set the Success message
            try:
                form.save()
                status = "Success!"

            # if there is an exception, set a Failure message
            except Exception as e:
                status = 'Failure: %s (%s)' % (e.args, type(e))

    # else load an empty form
    else:
        form = DatabaseForm()

    # construct the context dictionary to send to the template,
    # i.e. the form elements and status message
    context = {
            'form': form,
            'status': status,
    }

    # send all data to the html template for rendering to the user's browser
    return render(request, 'webform.html', context)
