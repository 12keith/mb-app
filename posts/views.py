from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_oblect_name = 'all_posts_list'
    


# Create your views here.
