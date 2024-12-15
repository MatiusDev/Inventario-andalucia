# Inventario andalucia

## Development
### Frontend (React + Vite)
    Descargar la carpeta "app" del proyecto y ejecutar los siguientes comandos para su uso:
    - cd app (Para estar dentro de la carpeta)
    - npm install
    - npm run dev

#### Comandos
`npm install`
`npm run dev`

### Backend (FastAPI)
    Descargar la carpeta "inventory_api", revisar también que se descarguen los archivos de docker dentro de esta y ejecutar los siguientes comandos:
    - cd inventory_api (Para estar dentro de la carpeta)
    - docker-compose up --build (Cuando finalice el proceso debes de finalizarlo: Ctrl + C)
    - docker-compose up -d (Para ejecutar el programa en segundo plano o hacerlo desde la app de docker)
    - docker logs -f app_server (Para revisar los logs del contenedor de app)

#### Comandos
`docker-compose up --build`
`docker-compose up -d`
`docker logs -f app_server`
`docker logs -f mysql_server`
    
## Production
### Despliegue
Este proyecto fue desplegado en Back4app para el backend (FastAPI) y Vercel para el frontend (React).

#### App: [Vercel](https://inventario-andalucia.vercel.app/)
#### Inventory_api: [Back4App](https://inventoryapi-58qfwaym.b4a.run/)