from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Санат атауы")

    class Meta:
        verbose_name = "Санат"
        verbose_name_plural = "Санаттар"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200, verbose_name="Тауар атауы")
    description = models.TextField(verbose_name="Сипаттамасы")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бағасы")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Тауар"
        verbose_name_plural = "Тауарлар"

    def __str__(self):
        return f"{self.title} ({self.price} тг)"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    customer_name = models.CharField(max_length=100, verbose_name="Тұтынушы")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Саны")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Тапсырыс уақыты")

    class Meta:
        verbose_name = "Тапсырыс"
        verbose_name_plural = "Тапсырыстар"
        ordering = ['-order_date']

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, 
        related_name='reviews',
        verbose_name="Өнім"
    )
    author = models.CharField(max_length=100, verbose_name="Автордың есімі")
    text = models.TextField(verbose_name="Пікір мәтіні")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Рейтинг (1-5)",
        default=5
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Жарияланған уақыты")

    class Meta:
        verbose_name = "Пікір"
        verbose_name_plural = "Пікірлер"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} - {self.product.title} ({self.rating}★)"