from rest_framework.routers import DefaultRouter, SimpleRouter
from booking.views import BookingViewSet
from menu.views import MenuViewSet
from restaurant.views import RestaurantViewSet
from review.views import ReviewViewSet
from table.views import TableViewSet

router = DefaultRouter()
simrouter = SimpleRouter()

router.register('booking', BookingViewSet)
router.register('menu', MenuViewSet)
router.register('restaurant', RestaurantViewSet)
router.register('review', ReviewViewSet)
router.register('table', TableViewSet)

