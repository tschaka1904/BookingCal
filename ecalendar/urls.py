from django.conf.urls.defaults import *

urlpatterns = patterns('ecalendar.views',
                       (r'^$', 'main'),
                       (r"^month/(\d+)/(\d+)/(prev|next)/$", "month"),
                       (r"^month/(\d+)/(\d+)/$", "month"),
                       (r"^month$", "month"),
                       (r"^day/(\d+)/(\d+)/(\d+)/$", "day"),
                       (r"^event/(\d+)/$", "event"),
                       (r"^new/$", "new"),
                       (r"^new/add/$", "add"),
                       (r"^new/check/$", "check"),
                       (r"^new/dbadd/$", "dbadd"),
                       (r"^history/$", "history"),
                       (r"^change/(\d+)/$", "change"),
                       (r"^delete/$", "delete"),
                       (r"^logout/$", "logout"),
                       (r"^changeadd/$", "changeadd")

)
