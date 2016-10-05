import django.shortcuts
import forms
 
def getAddress(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.MailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            html = '<html><body>%s<br>%s<br>%s<br>%s</body></html>' % (
                         form.cleaned_data['name'],
                         form.cleaned_data['address1'],
                         form.cleaned_data['address2'],
                         form.cleaned_data['postalcode'])
            return HttpResponse(html)
    else:
        # GET method -- create a blank form
        form = forms.MailForm()
    return django.shortcuts.render(request, 'address.html', {'form': form})
