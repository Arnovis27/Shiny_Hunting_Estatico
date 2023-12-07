# Proyecto Pokémon Shiny Finder

Este proyecto está diseñado para ayudarte a encontrar Pokémon Shiny en el juego Pokémon Esmeralda mediante el reconocimiento de imágenes.

## Características Principales

- **Emulador Automático:** Abre el emulador VisualBoyAdvance con el juego Pokémon Esmeralda automáticamente.
- **Soft-Reset Automático:** Realiza un soft-reset en el juego utilizando la combinación de teclas `Ctrl+R`.
- **Encuentro Inicial:** Pulsa la tecla `Z` para iniciar el encuentro con el Pokémon salvaje.
- **Análisis de Imágenes:** Utiliza técnicas de reconocimiento de imágenes para analizar si el encuentro es un Pokémon Shiny.

## Configuracion del emulador  
Para aumentar la velocidad del emulador y funcione mas rapido la busqueda  
**Options** > **Frame Skip** > **Throttle** > **Other** > **1000**


## Configuracion del juego  
Muy importante que te dirijas a opciones del juego y realices:  
- Velocidad del texto: Rapida  
- Animacion de Combate: No  
Esto con el fin de optimizar el tiempo en los encuentros ya que el script se tarde
alrededor de 6 segundos en realizar todas las acciones antes de realizar el soft-reset

## Configuración y Uso

1. **Clona el Repositorio:**
   ```bash
   git clone https://github.com/TuUsuario/PokemonShinyFinder.git
   cd PokemonShinyFinder

2. **Instala Dependencias**
    ```bash
    pip install -r requirements.txt

3. **Configuracion del sprite**  
    -Asegúrate de proporcionar la ruta correcta del sprite de Pokémon Shiny en ´main.py´. Esto es crucial para el reconocimiento preciso.
    Guiate del que encuetras en la carpeta Imagenes con nombre Estatico.PNG

4. **Ejecuta el programa**
    ```bash
    python main.py

## Contribuciones  
¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.