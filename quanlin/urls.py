from django.conf.urls import patterns, url
from django.utils import timezone
from quanlin import views

from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from quanlin.models import Dingdan

urlpatterns = patterns('',

    (r'^xadd$', 'quanlin.views.contact' ),
    # ListView.as_view(
    #     queryset = Dingdan.objects.all(),
    #     context_object_name='dingdan_list',
    #     template_name='quanlin/index.html'
    #     ),
    # # url(r'^$',
    # #     ListView.as_view(
    # #         queryset=Poll.objects.order_by('-pub_date')[:5],
    # #         context_object_name='latest_poll_list',
    # #         template_name='polls/index.html'),
    # #     name='index'),
    # url(r'^$',
    # ListView.as_view(
    #     queryset = Dingdan.objects.all(),
    #     context_object_name='dingdan_list',
    #     template_name='quanlin/index.html'
    #     ),
    # name='index'),
    #  url(r'^(?P<pk>\d+)/$',
    #      DetailView.as_view(
    #          model=Dingdan,
    #          template_name='quanlin/detail.html'),
    #      name='detail'),
    # url(r'^(?P<pk>\d+)/results/$',
    #     DetailView.as_view(
    #         model=Poll,
    #         template_name='polls/results.html'),
    #     name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name='vote'),
)
