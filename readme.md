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
**Options** > **Video** > **x2**  
**Options** > **Video** > **Render Method** > **Direct 3D**  
**Options** > **Gameboy** > **Real Colors**


## Configuracion del juego  
Muy importante que te dirijas a opciones del juego y realices:  
- Velocidad del texto: Rapida  
- Animacion de Combate: No  
Esto con el fin de optimizar el tiempo en los encuentros ya que el script se tarde
alrededor de 6 segundos en realizar todas las acciones antes de realizar el soft-reset

## Configuración y Uso

1. **Clona el Repositorio:**
   ```bash
   git clone https://github.com/Arnovis27/Shiny_Hunting_Estatico.git
   cd Shiny_Hunting_Estatico

2. **Instala Dependencias**
    ```bash
    pip install -r requirements.txt

3. **Configuracion ruta del juego y Rom**
    - Dentro del archivo ´funciones.py´ encontraras dos variables indispensables para colocar la ubicacion de la ruta donde se encuentra
    la Rom del juego (ROM_PATH) y el .exe del emulador (EMULATOR_PATH) 

4. **Configuracion del sprite**  
    - Asegúrate de proporcionar la ruta correcta del sprite de Pokémon Shiny en ´main.py´. Esto es crucial para el reconocimiento preciso.
    Guiate del que encuetras en la carpeta Imagenes con nombre Estatico.PNG

5. **Ejecuta el programa**
    ```bash
    python main.py

## Demostracion en Video
[![Demo del Pokémon Shiny Finder](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wikidex.net%2Fwiki%2FPok%25C3%25A9mon_Esmeralda&psig=AOvVaw3OwtW9d5AGz9YZu7KNNWop&ust=1702066029147000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMDOs56Q_oIDFQAAAAAdAAAAABAD)](https://youtu.be/Qk6nX8HbVF8)

## Contribuciones  
¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.
