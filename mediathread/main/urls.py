from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'mediathread.main.views',
    # urls prefix 'yourspace/'

    # User specific settings -- primarily used to track help visibility
    url(r'^(?P<user_name>\w[^/]*)/setting/$',
        'set_user_setting',
        name='set-user-setting'),

    # Collections box: View All Class Members' assets & work
    url(r'^projects/$',
        'all_projects',
        name='all-projects'),

    # Collections box: View a specified class member's assets & work
    url(r'^projects/(?P<record_owner_name>\w[^/]*)/$',
        'your_projects',
        name='your-projects'),
)
