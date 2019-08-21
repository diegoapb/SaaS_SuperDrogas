from django.urls import path
from apps.ecommerce import views as core_views

app_name = 'ecommerce'

urlpatterns = [

    path('', core_views.HomeView.as_view(), name='home-ecommerce'),
    path('product/<slug>/', core_views.ItemDetailView.as_view(), name='product-ecommerce'),


    # No testeadas aun
    path('checkout/', core_views.CheckoutView.as_view(), name='checkout'),
    path('order-summary/', core_views.OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', core_views.add_to_cart, name='add-to-cart'),
    path('add-coupon/', core_views.AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', core_views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/',
         core_views.remove_single_item_from_cart,
         name='remove-single-item-from-cart'
         ),
    path('payment/<payment_option>/', core_views.PaymentView.as_view(), name='payment'),
    path('request-refund/', core_views.RequestRefundView.as_view(), name='request-refund')
]
