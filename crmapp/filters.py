from .models import Message
import django_filters


class MessageFilter(django_filters.FilterSet):
    # kwords__word = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Message
        fields = ['kwords']
