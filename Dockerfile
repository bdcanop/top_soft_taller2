# Utiliza una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de la aplicación Flask al contenedor
COPY app.py /app/

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Define el comando de inicio de la aplicación
CMD ["python", "app.py"]
