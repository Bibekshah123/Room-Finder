# from django.utils.deprecation import MiddlewareMixin

# class DevCacheControlMiddleware(MiddlewareMixin):
#     def process_response(self, request, response):
#         if request.path.startswith('/static/'):
#             response['Cache-Control'] = 'max-age=3600, public'
#         return response