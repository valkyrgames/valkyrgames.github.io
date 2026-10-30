# Valkyr Games: página web

Página de Valkyr Games, publicada con GitHub Pages.

- `index.html`: inicio (juegos, estudio, contacto).
- `relampago/`: página de Relámpago. `relampago/jugar/` es el juego armado con `tools/armar.py` del repo `relampago` (copia de `dist/web`, sin videos de anuncios).
- `atado-con-alambre/`: página de Atado con Alambre. `atado-con-alambre/jugar/` es el juego armado con `torre/build.py` del proyecto del juego, con `CONFIG=firebase/web.json` (prende el login con Google y el ranking del proyecto de Firebase `atado-con-alambre`).
- `privacidad/`: política de privacidad (es el link para Google Play).
- `assets/`: estilos, logo, íconos e imágenes.

Español e inglés en la misma página: cada texto va dos veces con `data-l="es"` y `data-l="en"`, y el botón ES/EN cambia cuál se ve.

## Dominio

- **valkyrgames.com**, comprado en Porkbun el **20 de octubre de 2026**.
- Costo: 11,08 USD por año. **Vence el 20 de octubre de 2027**. Tiene renovación automática: revisar antes de esa fecha que el pago siga andando.

Para agregar un juego nuevo: una tarjeta `.game` en `index.html` y una carpeta propia como `relampago/`.

## Sumar un juego

1. Imágenes en `assets/<slug>/`: `icono.png` (cuadrado), `og.jpg` (1200×630, para compartir) y capturas `.webp`.
2. Agregar el juego a `JUEGOS` en `tools/juegos.py` (textos en español e inglés, botones `web` y `android`, `orient` vertical u horizontal).
3. `py tools/paginas.py` arma la ficha `<slug>/index.html`, la tarjeta en la portada, el pie y el sitemap.
   Con `estado: 'borrador'` no se publica; para verlo en local: `py tools/paginas.py --borradores` (y no subir esos archivos).
4. Si se juega en el navegador, el juego va en `<slug>/jugar/index.html`.

En Android el botón de Google Play sale primero; en iPhone y compu, «Jugar gratis» en el navegador (más un aviso para iPhone).
