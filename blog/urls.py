from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^blog/$', "blog.views.home", name='blog'),
                       url(r'^cont/$', "blog.views.cont", name='cont'),
                       url(r'^dr/$', "blog.views.dr", name='dr'),
                       url(r'^ejs/$', "blog.views.ejs", name='ejs'),
                       url(r'^calc/$', "blog.views.calc", name='calc'),
                       url(r'^cron/$', "blog.views.cron", name='cron'),
                       url(r'^load/$', "blog.views.load", name='load'),
                       url(r'^troll/$', "blog.views.troll", name='troll'),
                       url(r'^trolling/$', "blog.views.trolling", name='trolling'),
                       url(r'^conv/$', "blog.views.conv", name='conv'),
                       url(r'^save_message/$', 'blog.views.save_message', name='save_message'), 
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', "blog.views.ver_post", name='vermipost'),
                      )