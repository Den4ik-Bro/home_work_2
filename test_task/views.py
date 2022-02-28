import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .serializers import TableSerializer
from django.views.generic import ListView, FormView
from .models import Table
from .forms import SearchForm
from .filters import TableFilters


class MainListView(ListView, FormView):
    queryset = Table.objects.all()
    template_name = 'test_task/main.html'
    paginate_by = 5
    form_class = SearchForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        return context

    def get_queryset(self):
        # queryset = super().get_queryset()
        if 'q' in self.request.GET and 'colomn' in self.request.GET and 'condition' in self.request.GET:
            form = SearchForm(self.request.GET)
            if form.is_valid():
                field = form.cleaned_data['colomn']
                condition = form.cleaned_data['condition']
                # поиск по названию
                if field == 'title' and condition == 'gt' or condition == 'lt':
                    return super(MainListView, self).get_queryset()
                if field == 'title' and condition == 'exact':
                    return super(MainListView, self).get_queryset().filter(
                        title__exact=form.cleaned_data['q']
                    )
                if field == 'title' and condition == 'contains':
                    return super(MainListView, self).get_queryset().filter(
                        title__contains=form.cleaned_data['q']
                    )
                # поиск по количеству
                if field == 'count' and condition == 'contains':
                    return super(MainListView, self).get_queryset()
                if field == 'count' and condition == 'gt':
                    return super(MainListView, self).get_queryset().filter(
                        count__gt =form.cleaned_data['q']
                    )
                if field == 'count' and condition == 'lt':
                    return super(MainListView, self).get_queryset().filter(
                        count__lt=form.cleaned_data['q']
                    )
                if field == 'count' and condition == 'exact':
                    return super(MainListView, self).get_queryset().filter(
                        count__exact=form.cleaned_data['q']
                    )
                # поиск по дистанции
                if field == 'distance' and condition == 'contains':
                    return super(MainListView, self).get_queryset()
                if field == 'distance' and condition == 'gt':
                    return super(MainListView, self).get_queryset().filter(
                        distance__gt=form.cleaned_data['q']
                    )
                if field == 'distance' and condition == 'lt':
                    return super(MainListView, self).get_queryset().filter(
                        distance__lt=form.cleaned_data['q']
                    )
                if field == 'distance' and condition == 'exact':
                    return super(MainListView, self).get_queryset().filter(
                        distance__exact=form.cleaned_data['q']
                    )
        return super().get_queryset()


class ListApiTable(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TableFilters
    # search_fields = ['title', 'count', 'distance']





