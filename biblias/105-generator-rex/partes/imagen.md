# Parte de IMAGEN · Generator Rex (105)

Investigador de imagen. Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Libreta de datos, no prosa.
`datos-imagen.md` de recolectar.py salió casi todo inútil: mezcló a Rex con personajes de Teen Titans,
Adventure Time y Powerpuff Girls (búsqueda genérica «rex» sin wiki fijada) y el Sketchfab/Openverse
salió por coincidencia de la palabra «rex» (T-Rex, OSIRIS-REx, Stephen King). Sólo se aprovecha lo de
`rex_salazar` en Danbooru/Safebooru; el resto se descarta y se repite bien en esta parte.

Wiki real: `generatorrex.fandom.com` (imágenes alojadas en `static.wikia.nocookie.net/generatorrexpedia/`).

## 1 · Arte oficial, en cantidad y variado

Hojas de contacto con `investigar_serie.py --wiki generatorrex --min-px 90000` sobre Rex Salazar, Agent Six,
Bobo Haha, Providence, Van Kleiss, Breach, White Knight, Rex Salazar's machines, Nanites, Circe, Noah Nixon
y Rebecca Holiday: 121 imágenes enlazadas, 113 grandes, 3 hojas (en `hojas/`). Miradas fotograma a fotograma.

- Retrato oficial de infobox de Rex Salazar (chaqueta roja, camiseta verde oscuro, goggles naranjas en la cabeza) · https://static.wikia.nocookie.net/generatorrexpedia/images/e/e5/Rex_Salazar.png · ✅ (wiki + usado en cientos de fan pages) · 333×250
- Arte de personaje de Agent Six (traje verde oscuro, gafas de sol, katanas a la espalda) · https://static.wikia.nocookie.net/generatorrexpedia/images/9/94/Agent_Six.png · ✅ · 333×250
- Arte de personaje de Bobo Haha (mono con chaleco caqui y arnés, cresta roja) · https://static.wikia.nocookie.net/generatorrexpedia/images/9/97/Bobo.png · ✅ · 333×250
- Arte de personaje de Van Kleiss (abrigo/capa negra con hombreras y cuello oliva) · https://static.wikia.nocookie.net/generatorrexpedia/images/d/d6/Van_Kleiss.png · ✅ · 333×250
- Arte de personaje de White Knight (abrigo blanco largo, cuello de tortuga negro) · https://static.wikia.nocookie.net/generatorrexpedia/images/9/92/White_Knight.png · ✅ · 333×250
- Arte de personaje de Circe (peto rojo sobre top gris, botas y guantes tostados) · https://static.wikia.nocookie.net/generatorrexpedia/images/7/75/Circe.png · ✅ · 333×250
- Certificado/diploma de Providence con sello institucional (prop oficial, útil para tipografía de mundo) · https://static.wikia.nocookie.net/generatorrexpedia/images/7/7a/Providence_Certificate.jpg · ✅ (hoja 1 nº3) · 1208×920
- «Rex Build Omnitrix.webp», arte promocional del crossover Ben 10/Generator Rex: Heroes United (Rex con un Omnitrix) · https://static.wikia.nocookie.net/generatorrexpedia/images/e/e4/Rex_Build_Omnitrix.webp · ✅ (hoja 1 nº2, se ve el hilo de Twitter de Duncan Rouleau -co-creador- confirmando que era técnicamente posible) · 1125×1377
- Fotograma de Rex en su forma EVO completa/Omega-1 (transformación de cuerpo entero, textura dorada-armadura) · https://static.wikia.nocookie.net/generatorrexpedia/images/...(320-Full_Omega-1_form.png, hoja 1 nº30) · ⚠️ (una sola fuente, wiki) · 511×288

Sigue en «Bitácora» las búsquedas de arte fuera de wiki (portadas DVD/Blu-ray, artbook) que no dieron nada verificable en la red abierta de este contenedor.

## 15 · Vestuario, colores medidos

Hex medidos con Pillow (recorte de zona de tela, sin bordes de línea) sobre el arte oficial de personaje de la wiki citado en el punto 1. Método en la Bitácora.

Personaje | Prenda | Hex medido | De qué imagen
---|---|---|---
Rex Salazar | Chaqueta/chamarra (roja, su prenda icónica) | #A04D47 | Rex_Salazar.png (retrato infobox, wiki)
Rex Salazar | Camiseta interior (verde oscuro grisáceo) | #394B45 | Rex_Salazar.png (retrato infobox, wiki)
Agent Six | Traje (verde botella oscuro) | #3F4C43 | Agent_Six.png (dominante, estilo.py)
Agent Six | Corbata (negra) | #3F3F3F | Agent_Six.png
Bobo Haha | Chaleco/arnés (caqui claro) | #838370 | Bobo.png (retrato infobox)
Bobo Haha | Franja central del arnés (turquesa apagado) | #495D68 | Bobo.png
Van Kleiss | Capa/abrigo (negro) | #140D07 | Van_Kleiss.png
Van Kleiss | Cuello y hombreras (oliva-mostaza) | #736B58 | Van_Kleiss.png
White Knight | Abrigo largo (blanco roto) | #E5E5E4 | White_Knight.png
White Knight | Cuello alto/corbata (negro puro) | #050504 | White_Knight.png (medido en píxel de la sombra del cuello, no en zona con luz)
Circe | Peto/overol (rojo oscuro, en sombra de calle) | #56262A | Circe.png
Circe | Top interior (gris azulado) | #838694 | Circe.png
Circe | Guantes/botas (tostado) | #554E43 | Circe.png

Nota: son capturas de wiki en baja resolución (333×250), colores «planos» del cel-shading de la serie sin degradado
fuerte; el hex es representativo del tono base de cada prenda, no un Pantone exacto. Rex NO lleva camiseta blanca
(como asumen algunos resúmenes en inglés): es verde oscuro, confirmado mirando el arte oficial.
