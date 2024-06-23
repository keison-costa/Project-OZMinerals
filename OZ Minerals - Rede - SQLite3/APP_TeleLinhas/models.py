from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Aparelhos(models.Model):
    IMEI_APARELHO = models.CharField(max_length=15, unique=True, verbose_name="IMEI do Telefone")
    MODELO = models.CharField(max_length=20, verbose_name="Modelo")
    FABRICANTE = models.CharField(max_length=20, verbose_name="Fabricante")
    UTILIZADOR = models.CharField(max_length=50, verbose_name="Nome Completo do Utilizador")
    EMAIL = models.EmailField(unique=True, verbose_name="E-mail")
    LOGIN_ADMANAGER = models.CharField(max_length=50, unique=True, verbose_name="Login ADManager")

    class Meta:
        verbose_name = "Aparelho"
        verbose_name_plural = "Aparelhos"

    def save(self, *args, **kwargs):
        self.UTILIZADOR = self.UTILIZADOR.upper()
        super(Aparelhos, self).save(*args, **kwargs)

    def __str__(self):
        return self.UTILIZADOR

class LinhaTelefonica(models.Model):
    telefone = PhoneNumberField(unique=True, verbose_name="Número de Telefone")
    imei_number = models.CharField(max_length=15, unique=True, verbose_name="IMEI do CHIP")
    user = models.ForeignKey(Aparelhos, on_delete=models.CASCADE, verbose_name="Linha Atribuida a")
    registration_datetime = models.DateTimeField(default=timezone.now, verbose_name="Data/Hora de Registro")

    class Meta:
        verbose_name = "Linha Telefônica"
        verbose_name_plural = "Linhas Telefônicas"

    def __str__(self):
        return self.imei_number
    
    

