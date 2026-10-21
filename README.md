# Valkyr Games: página web

Página de Valkyr Games, publicada con GitHub Pages.

- `index.html`: inicio (juegos, estudio, contacto).
- `relampago/`: página de Relámpago. `relampago/jugar/` es el juego armado con `tools/armar.py` del repo `relampago` (copia de `dist/web`, sin videos de anuncios).
- `privacidad/`: política de privacidad (es el link para Google Play).
- `assets/`: estilos, logo, íconos e imágenes.

Español e inglés en la misma página: cada texto va dos veces con `data-l="es"` y `data-l="en"`, y el botón ES/EN cambia cuál se ve.

## Dominio

- **valkyrgames.com**, comprado en Porkbun el **20 de octubre de 2026**.
- Costo: 11,08 USD por año. **Vence el 20 de octubre de 2027**. Tiene renovación automática: revisar antes de esa fecha que el pago siga andando.

Para agregar un juego nuevo: una tarjeta `.game` en `index.html` y una carpeta propia como `relampago/`.
