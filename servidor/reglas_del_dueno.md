# Lo que el dueño ha dicho de las láminas

## Las reglas que salen de sus veredictos (no negociables)

1. **Un objeto real en un sitio real** (le encantaron el disco de Bebop y la
   caja de Bocchi; no le convencieron paneles de interfaz sueltos). Si el
   objeto se puede hacer en **Blender** (caja, cuaderno, vinilo, teclado,
   recreativa), se hace: la tinta sigue las arrugas, la luz es real.
2. **Personajes con pose y cara que vayan con lo que dicen.** Nada de bustos
   cortados en recto flotando. Si el marco es una pantalla, va un fotograma.
3. **Recortes siempre por `v3/integrar.py`** (borde sin halo, línea ×2, luz y
   tono de la escena) y comprobados a 1:1.
4. **Textos cortos, en la voz de la serie**: una idea cada uno; sin «·», «—»
   ni paréntesis de relleno. Info completa, pero repartida.
5. **Si una lámina se satura → lámina 2** que explique (etiquetas, rangos,
   formatos). Ejemplo hecho: #demos-canto 2 con el teclado.
6. **Tono de la serie**: Death Note sangriento (`v3/sangre.py`), Bebop sobrio…
   nada de colores alegres en un mundo sombrío.
7. **Cuando él señala algo en una, se revisa en todas.** (Ej.: una mano sin brazo visible no se apoya en nada: «parece que sale de la piedra».)
8. Voz latina comprobada (Doblaje Wiki por la API `action=parse`).
9. 🔴 **No saturar su PC** (23-sep, noche: «te comiste mi SSD, mi RAM y mi
   procesador», tuvo que reiniciar): una herramienta pesada a la vez; en
   Photoshop borrar las capas tras exportar cada recorte; no ampliar por
   encima de ~4000 px; pruebas a ×2 y sólo la final a ×3.
10. Render a ×3 (`node render.js v3/<x>.html 3`), JPEG q92, galería a tamaño completo.

