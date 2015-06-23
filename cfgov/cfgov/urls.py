from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

from sheerlike.views.generic import SheerDetailView

urlpatterns = [
    url(r'^blog/', include([
        url(r'^$', TemplateView.as_view(template_name='blog/index.html'),
                   name='index'), 
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerDetailView.as_view(doc_type='posts',
                                           local_name='post',
                                           template_name='blog/_single.html',),
                   name='detail'),], namespace='blog')),

    url(r'^newsroom/', include([
        url(r'^$', TemplateView.as_view(template_name='newsroom/index.html'),
                   name='index'), 
        url(r'^press-resources/$',
            TemplateView.as_view(template_name='newsroom/press-resources/index.html'),
            name='press-resources'),
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerDetailView.as_view(doc_type='newsroom',
                                           local_name='newsroom',
                                           template_name='newsroom/_single.html',),
                   name='detail'),], namespace='newsroom')),

    url(r'^budget/',include([
        url(r'^$', TemplateView.as_view(template_name='budget/index.html'), name='home'),
        url(r'^strategic-plan/$',
            TemplateView.as_view(template_name='budget/strategic-plan/index.html'),
            name='strategic-plan'),
        url(r'^performance-plan-report/$',
            TemplateView.as_view(template_name='budget/performance-plan-report/index.html'),
            name='performance-plan-report'),
        url(r'^financial-report/$',
            TemplateView.as_view(template_name='budget/financial-report/index.html'),
            name='financial-report'),
        url(r'^funding-request/$',
            TemplateView.as_view(template_name='budget/funding-request/index.html'),
            name='funding-request'), ], namespace="budget")),

    url(r'^the-bureau/', include([
        url(r'^$', TemplateView.as_view(template_name='the-bureau/index.html'),
            name='index'),
        url(r'^history/$',
            TemplateView.as_view(template_name='the-bureau/history/index.html'),
            name='home'),
        url(r'^about-rich-cordray/$',
            TemplateView.as_view(template_name='the-bureau/about-rich-cordray/index.html'),
            name='home'),
        url(r'^about-steve-antonakes/$',
            TemplateView.as_view(template_name='the-bureau/about-steve-antonakes/index.html'),
            name='home'),
        url(r'^bureau-structure/$',
            TemplateView.as_view(template_name='the-bureau/bureau-structure/index.html'),
            name='home'),
        url(r'^leadership-calendar/$',
            TemplateView.as_view(template_name='the-bureau/leadership-calendar/index.html'),
            name='home'), ], namespace='the-bureau')),

    url(r'^doing-business-with-us/', include([
        url(r'^$',
            TemplateView.as_view(template_name='doing-business-with-us/index.html'),
            name='index'),
        url(r'^upcoming-procurement-needs/$',
            TemplateView.as_view(template_name='doing-business-with-us/upcoming-procurement-needs/index.html'),
            name='upcoming-procurement-needs'),
        url(r'^past-awards/$',
            TemplateView.as_view(template_name='doing-business-with-us/past-awards/index.html'),
            name='past-awards'),
        url(r'^small-businesses/$',
            TemplateView.as_view(template_name='doing-business-with-us/small-businesses/index.html'),
            name='small-business'),

    ], namespace='business')),

        url(r'^contact-us/', include([
        url(r'^$',
            TemplateView.as_view(template_name='contact-us/index.html'),
            name='index'),
        url(r'^upcoming-procurement-needs/$',
            TemplateView.as_view(template_name='doing-business-with-us/upcoming-procurement-needs/index.html'),
            name='upcoming-procurement-needs'),
        url(r'^past-awards/$',
            TemplateView.as_view(template_name='doing-business-with-us/past-awards/index.html'),
            name='past-awards'),
        url(r'^small-businesses/$',
            TemplateView.as_view(template_name='doing-business-with-us/small-businesses/index.html'),
            name='small-business'),

    ], namespace='business')),

    url(r'^activity-log/$', TemplateView.as_view(template_name='activity-log/index.html'), name='activity-log'),

]

from sheerlike import register_permalink

register_permalink('posts', 'blog:detail')
register_permalink('newsroom', 'newsroom:detail')
