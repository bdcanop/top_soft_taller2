# Usar una imagen base de Python
FROM python:3.8

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Instalar Flask y otras dependencias
RUN pip install Flask

# Copiar todos los archivos de la aplicación en el directorio de trabajo
COPY . . 

# Exponer el puerto en el que se ejecutará la aplicación (por ejemplo, 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python3", "app/app.py"]
