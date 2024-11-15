from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomBasePagination(PageNumberPagination):
    """
        Specifying the page size in api
    """
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response({
            "default_page_size": self.page_size,
            "count_objects": self.page.paginator.count,
            "count_pages": self.page.paginator.num_pages,
            "current_page_number": self.page.number,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
        })


class CustomPageNumberFewerPagination(CustomBasePagination):
    page_size = 7
    max_page_size = 10


class CustomPageNumberAveragePagination(CustomBasePagination):
    page_size = 15
    max_page_size = 15


class CustomPageNumberMorePagination(CustomBasePagination):
    page_size = 20
    max_page_size = 30
