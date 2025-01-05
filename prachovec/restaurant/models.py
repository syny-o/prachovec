from django.db import models

# Food Models
class FoodCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Jídelní lístek - kategorie'      


class FoodItem(models.Model):
    category = models.ForeignKey(FoodCategory, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50, default='---')  # Price as string if not numeric

    def __str__(self):
        return f"{self.name} - {self.price}"
    
    class Meta:
        verbose_name = 'Jídelní lístek - produkty'      


# Drink Models
class DrinkCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Nápojový lístek - kategorie'    


class DrinkItem(models.Model):
    category = models.ForeignKey(DrinkCategory, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50, default='---')  # Price as string if not numeric

    def __str__(self):
        return f"{self.name} - {self.price}"
    

    class Meta:
        verbose_name = 'Nápojový lístek - produkty'   
