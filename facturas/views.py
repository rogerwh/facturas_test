from django.shortcuts import render
from .models import Factura
from empresa.models import Empresa

def factura_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    facturas_empresa = Factura.objects.select_related("forma_pago").filter(empresa=empresa)
    total_facturas = facturas_empresa.count()
    return render(request, 'facturas_empresa.html', {
        "facturas": facturas_empresa, "empresa":empresa, "total_facturas": total_facturas})