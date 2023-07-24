from rest_framework import filters
from rest_framework.settings import api_settings


class QueryParamsFilter(filters.SearchFilter):
    def __init__(self, request, view):
        self.search_param = getattr(
            view, 'search_param', api_settings.SEARCH_PARAM)

    # def filter_queryset(self, request, queryset, view):
    #     return super().filter_queryset(request, queryset, view)
