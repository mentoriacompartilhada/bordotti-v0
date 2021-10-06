# from typing import OrderedDict
# from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
# from django.http import HttpResponse
# from django.core.paginator import EmptyPage
from rest_framework.exceptions import ErrorDetail, ReturnDict, ReturnList


# from rest_framework.exceptions import NotFound  
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR


class PersonalizedPagination2(PageNumberPagination):

    this_page = 0

    def paginate_queryset(self, queryset, request, view=None):

        self.page_size_query_param = 'size'
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)
        self.this_page = page_number
        try:
            self.page = paginator.page(page_number)
        except:
            return []

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)


    def get_paginated_response(self, data):
        try:
            self.page.paginator.page(self.page.number+1)
        except Exception:
            pass

        return Response({
            'page': self.this_page,
            'size': len(data),
            'total': self.page.paginator.count,
            'items': data
        })



class PersonalizedPagination(PageNumberPagination):    
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'size'
    param_page = 0
    param_total = 0

    def paginate_queryset(self, queryset, request, view):
        
        pagina = int(request.query_params['page'])
        
        if not request.query_params._mutable:
            request.query_params._mutable = True
        
        request.query_params['page'] = str(pagina+1)
        self.param_page = pagina
        self.param_total = len(queryset)

        page_size = self.get_page_size(request)

        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)
        
        try:
            self.page = paginator.page(page_number)            
        except:
            return list()

        if paginator.num_pages > 1 and self.template is not None:            
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    def get_paginated_response(self, data):
        pagina =  {
            'page': self.param_page,
            'size': len(data),
            'total': self.param_total,
            'items': data
        }
        return Response(pagina)
