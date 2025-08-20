from django.db import models
from accounts.models import CustomUser
from datetime import date

        

class Diary(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # Autor do diário
    name = models.CharField(max_length=50, null=True, blank=True)   # Nome do diário
    public_access = models.BooleanField(default=False)  # Define se o diário é público ou privado
    public_access_date = models.DateField(blank=True, null=True)    # Data de publicação do diário
    last_access_date = models.DateTimeField(auto_now_add=True)  # Apenas usado para dados       Data do último acesso no diário
    diary_creation_date = models.DateTimeField(auto_now_add=True)   # Apenas usado para dados   Data de criação do diário
    
    # Algoritmo para definir quando o diário ficará público
    def save(self, *args, **kwargs):
        if self.public_access_date and self.public_access_date < date.today():
            self.public_access = True
        
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["name"]    
    


class Page(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=50, null=True, blank=True)  # Título da página
    content = models.TextField(max_length=1200) # Conteúdo da página
    page_creation_date = models.DateTimeField(auto_now_add=True)    # Data de criação da pagina
    page_num = models.DecimalField(decimal_places=0, max_digits=1000, default=1) # Apenas usado para dados Número de páginas no diário 
    
    class Meta:
        ordering = ['page_num']     