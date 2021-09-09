from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework.exceptions import NotFound  
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class NotFound(APIException):
    status_code = HTTP_200_OK
    default_detail = ('bad_request.')
    default_code = 'bad_request'


class PersonalizedPagination(PageNumberPagination):

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        self.page_size_query_param = 'size'
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)

        try:
            self.page = paginator.page(page_number)
        except Exception as exc:
            msg = {
                'page': int(page_number)-1,
                'size': 0,
                'total': int(paginator.count),
                'items': []
                }
            raise NotFound(msg)

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
            # msg = {
            #     'page': self.page.number,
            #     'size': self.page.paginator.per_page,
            #     'total': self.page.paginator.count,
            #     'items': []
            #     }
            # raise NotFound(msg)

        return Response({
            'page': self.page.number,
            'size': len(data),
            'total': self.page.paginator.count,
            'items': data
        })