from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse

from cardapio.models import Loja

def lojas(request):
	todas_lojas = Loja.objects.all()
	return TemplateResponse(
			request,
			'cardapio/lojas.html',
			{'lojas': todas_lojas }
		)

def loja_detail(request, loja_id):
	post = get_object_or_404(Loja, pk=loja_id)
	return render(request, 'cardapio/loja_detail.html', {'loja': post})

