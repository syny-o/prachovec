from django.db import models

# Food Models
class FoodCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name = "Název")
    position = models.PositiveIntegerField(default=10, verbose_name = "Pozice v tabulce", help_text="Position for ordering categories in the final template. Lower values appear first.")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Jídelní lístek - kategorie'      
        verbose_name_plural = 'Jídelní lístek - kategorie'
        ordering = ['position']  # Categories will be ordered by the 'position' field
 


class FoodItem(models.Model):
    category = models.ForeignKey(FoodCategory, related_name='items', on_delete=models.CASCADE, verbose_name = "Kategorie")
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50, default='-')
    position = models.PositiveIntegerField(default=10, verbose_name = "Pozice v tabulce")

    def __str__(self):
        return f"{self.name} - {self.price}"
    
    class Meta:
        verbose_name = 'Jídelní lístek - produkty'      
        verbose_name_plural = 'Jídelní lístek - produkty'    
        ordering = ['position']    


# Drink Models
class DrinkCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name = "Název")
    position = models.PositiveIntegerField(default=10, verbose_name = "Pozice v tabulce", help_text="Position for ordering categories in the final template. Lower values appear first.")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Nápojový lístek - kategorie'    
        verbose_name_plural = 'Nápojový lístek - kategorie'  
        ordering = ['position']  


class DrinkItem(models.Model):
    category = models.ForeignKey(DrinkCategory, related_name='items', on_delete=models.CASCADE, verbose_name = "Kategorie")
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50, default='-')
    position = models.PositiveIntegerField(default=10, verbose_name = "Pozice v tabulce")

    def __str__(self):
        return f"{self.name} - {self.price}"
    

    class Meta:
        verbose_name = 'Nápojový lístek - produkty'
        verbose_name_plural = 'Nápojový lístek - produkty'
        ordering = ['position']  

         
