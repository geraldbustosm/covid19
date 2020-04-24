# Web scrapping a Minsal

## Resumen

Debido a que la mayoría de la información recopilada sobre el COVID-19 en Chile estaba solo a nivel nacional se decidió recopilar información de la cantidad de  contagiados y fallecidos **por región** desde el primer contagiado en Chile, el 3 de marzo de 2019 hasta el 5 de abril de 2019.  Posterior a esto, empezó a utilizar el web scrapping rellenando de manera automática el archivo *coronavirus.csv* con los nuevos datos proporcionados por el gobierno en el sitio https://www.gob.cl/coronavirus/cifrasoficiales.

## ¿Cómo funciona?

Se almacena el archivo *coronavirus.csv* en http://geraldbustos.000webhostapp.com/coronavirus.csv el cual se actualiza automáticamente todos los días a las 11:40 am (minutos previos a esta hora ya está actualizada la tabla en la pagina del gobierno) gracias a la ejecución en la nube de *scrapping.py*.

El archivo *coronavirus.csv* subido en este repositorio posee los datos obtenidos manualmente para que vean a modo de ejemplo como es el formato del data-set.

## Estructura

Ejemplo: primer día de contagio en Chile (03 de marzo de 2019).

| Región             | Fecha      | Contagiados | Decesos |
| ------------------ | ---------- | ----------- | ------- |
| Arica y Parinacota | 03-03-2020 | 0           | 0       |
| Tarapacá           | 03-03-2020 | 0           | 0       |
| Antofagasta        | 03-03-2020 | 0           | 0       |
| Atacama            | 03-03-2020 | 0           | 0       |
| Coquimbo           | 03-03-2020 | 0           | 0       |
| Valparaíso         | 03-03-2020 | 0           | 0       |
| RM                 | 03-03-2020 | 0           | 0       |
| O’Higgins          | 03-03-2020 | 0           | 0       |
| Maule              | 03-03-2020 | 1           | 0       |
| Ñuble              | 03-03-2020 | 0           | 0       |
| Biobío             | 03-03-2020 | 0           | 0       |
| Araucanía          | 03-03-2020 | 0           | 0       |
| Los Ríos           | 03-03-2020 | 0           | 0       |
| Los Lagos          | 03-03-2020 | 0           | 0       |
| Aysén              | 03-03-2020 | 0           | 0       |
| Magallanes         | 03-03-2020 | 0           | 0       |

## Uso

La idea es simplemente consumir *coronavirus.csv* sin la necesidad de pasar por alguna API.

Una de las utilidades que le podemos dar a esto es cargar el archivo a power bi y generar reportes con los datos. Además power bi tiene la opción de actualizar la fuente de datos de manera automática dejando el trabajo totalmente automatizado.

## Ejemplo de uso

Gráfico generado en Power BI.

![](https://i.imgur.com/McH79nv.png)

## Nota

Se empleó una verificación simple en la comunicación con la API a modo de ejemplo.