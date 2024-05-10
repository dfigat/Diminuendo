from rest_framework import routers

from api.viewsets import *

router = routers.DefaultRouter()
router.register('user', UserViewset)