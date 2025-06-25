from flask import jsonify, request
from src.database.db import mysql
import MySQLdb

# Funcion para registrar a un nuevo hijo
def insert_hijo():
    try:
        data = request.get_json()

        dni = data['dni']
        nombres = data['nombres']
        ap_paterno = data['ap_paterno']
        ap_materno = data['ap_materno']
        direccion = data['direccion']
        fecha_nacimiento = data['fecha_nacimiento']
        partida = data['partida']
        dni_madre = data['dni_madre']

        cursor = mysql.connection.cursor()
        cursor.callproc('registrar_hijo', (
            dni, nombres, ap_paterno, ap_materno,
            direccion, fecha_nacimiento, partida, dni_madre
        ))

        # 🚨 Muy importante para evitar el error 2014
        while cursor.nextset():
            pass

        mysql.connection.commit()

        return jsonify({
            'success': True,
            'message': "Registro exitoso del hijo"
        })

    except MySQLdb.Error as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

    finally:
        cursor.close()