from django.shortcuts import render, redirect
from .models import Portfolio, speak_me

# Create your views here.
def main(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        messege = request.POST.get('mensagem')

        # Cria uma nova instância do modelo SpeakMe e salva no banco de dados
        novo_contato = speak_me(name=nome, email=email, messege=messege)
        novo_contato.save()

        # Redireciona para uma página de agradecimento ou de sucesso
        return redirect('success')  

    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolio})
