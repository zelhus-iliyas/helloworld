from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Orders(models.Model):

    SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA_LARGE', 'extraLarge'),

    )
    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'inTransit '),
        ('DELIVERED', 'delievered'),

    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=SIZES, default=SIZES[0][0])
    order_status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"<Order {self.size} size pizza by {self.customer}.>"
