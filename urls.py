from django.conf.urls.defaults import *
from django.contrib import admin
from bookingCal import settings

admin.autodiscover()

urlpatterns = patterns('',
   # (r'^booking/$', 'bookingCal.views.name'),
    (r'^booking/$', 'bookingCal.views.index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^booking/admin/', include(admin.site.urls)),
    (r'^booking/kalendar/', include('ecalendar.urls')),
    (r'^booking/equipment/', 'bookingCal.views.equip'),
    (r"^kalendar/new/guestReg/$", "bookingCal.ecalendar.views.guestReg"),
    (r"^kalendar/delete/$", "bookingCal.ecalendar.views.delete"),
    (r"^kalendar/changeadd/$", "bookingCal.ecalendar.views.changeadd"),
    (r'^booking/static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root':     settings.MEDIA_ROOT}),

)
