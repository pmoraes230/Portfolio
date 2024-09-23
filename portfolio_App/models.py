from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    url = models.URLField()

    def __str__(self):
        return self.title
     
class speak_me(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    messege = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
# Sinal para envio de e-mail após a criação de um novo objeto speak_me
@receiver(post_save, sender=speak_me)
def send_email_on_create(sender, instance, created, **kwargs):
    if created:  # Verifica se é uma criação, não apenas uma atualização
        subject = 'Nova mensagem recebida'
        message = f'Nome: {instance.name}\nEmail: {instance.email}\nMensagem: {instance.messege}'
        recipient_list = ['pmoraes230nascimento@gmail.com']  # Substitua pelo e-mail do destinatário
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)