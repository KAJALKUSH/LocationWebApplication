from django.shortcuts import render
from django.conf import settings

'''
Basic view for routing 
'''
def route_view(request):
	return render(request, 'main/route.html')

'''
Basic view for displaying a map 
'''
def map_view(request):
	return render(request, 'main/map.html')
