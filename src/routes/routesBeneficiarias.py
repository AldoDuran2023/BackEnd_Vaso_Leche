from flask import Blueprint, request
from src.services.servicesBeneficiaria import get_beneficiarias, registrar_beneficiaria, actualizar_beneficiaria, reporte_beneficiarias

beneficiarias = Blueprint('beneficiarias', __name__)

@beneficiarias.route('/', methods=['GET'])
def lista_beneficiarias():
    return get_beneficiarias()

@beneficiarias.route('/registrar', methods=['POST'])
def nueva_beneficiaria():
    return registrar_beneficiaria(request)

# Ruta para actualizar una beneficiaria
@beneficiarias.route('/actualizar', methods=['PUT'])
def actualizar_datos():
    return actualizar_beneficiaria(request)

# Ruta para los reportes
@beneficiarias.route('/reporte/beneficiarias', methods=['GET'])
def reporte_pdf():
    return reporte_beneficiarias()
