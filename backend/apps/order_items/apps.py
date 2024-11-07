from django.apps import AppConfig # type: ignore


class OrderItemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.order_items'