from django.utils.deprecation import MiddlewareMixin
from main.models import Blog

class BlogViewMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'slug' in view_kwargs:
            slug = view_kwargs['slug']
            try:
                blog = Blog.objects.get(slug=slug)
                blog.views += 1
                blog.save()
            except Blog.DoesNotExist:
                pass
        return None