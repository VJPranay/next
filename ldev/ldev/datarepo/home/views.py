from django.shortcuts import render 
from datarepo.models import Home  
# Create your views here. 




def pages_list(request):
    all_homes = Home.objects.all()
    final = []
    for temp_home in all_homes:
        dict = {
            'name' : temp_home.slug
        }
        final.append(dict)
    return {'main_menu_list':final }
    
    
def home(request,slug="pranay"):
    if slug is None:
        return render(request, "not_found.html")
    else:
        try:
            page_info = Home.objects.get(slug=slug)
            page_data = {
                "image" : page_info.image.url,
                "title" : page_info.title,
                "description" : page_info.description,
                "button_text" : page_info.button_text,
                "button_link" : page_info.button_link
            }
            return render(request, context=page_data, template_name="home.html") 
        except Home.DoesNotExist:
            return render(request, "not_found.html")
    
