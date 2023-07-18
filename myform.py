from django.views import View
from django.shortcuts import render
from .forms import MyForm

class MyFormView(View):
    form_class = MyForm
    template_name = 'form_template.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # process the data
            pass

        return render(request, self.template_name, {'form': form})
