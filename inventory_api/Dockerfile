# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /core

# Copia los archivos necesarios al contenedor
COPY ./requirements.txt /core/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /core/requirements.txt

# Expone el puerto en el que corre FastAPI
EXPOSE 8000

# Comando para iniciar la aplicación (ajusta "main:app" según tu configuración)
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
