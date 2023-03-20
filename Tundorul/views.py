from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import View

class MyView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        return render(
            request,
            'index.html',
            {}
        )
        return HttpResponse('')
