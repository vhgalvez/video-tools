
Crear carpeta del proyecto
mkdir video-tools
cd video-tools
2. Crear entorno virtual
python -m venv .venv
3. Activarlo
.\.venv\Scripts\activate

Verás algo así:

(.venv) PS C:\...\video-tools>
4. Instalar MoviePy
pip install moviepy
5. Verificar
python -c "import moviepy; print(moviepy.__version__)"
6. Ejecutar tu script

Guarda tu archivo como:

unir_clips.py

Y ejecuta:

python unir_clips.py
Si falla por FFmpeg

Instala también:

pip install imageio-ffmpeg
