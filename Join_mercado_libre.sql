--  Visualizar mejor relación de tablas 
SELECT  idCostos, Carr.carrier_id, Cde.zona, Tiempo_de_entrega, Carr.Name, Capacity, Cost.Costo, Cantidad_de_envios
FROM envios.costos as Cost
Left  join envios.carrier as Carr 
on Cost.carrier_id=Carr.carrier_id 
Left  join envios.cantidad_de_envios as Cde
on Cost.Zona=Cde.zona;

-- Obtener para el mes 1 cuánto costaría enviar con cada carrier los envíos de la tabla Cantidad de envíos
-- SELECT   distinct (Cde.zona) AS ZONA , sum(Cost.Costo) AS Costo_Enviar_Carrier
 -- FROM envios.costos as Cost
 -- Left  join envios.carrier as Carr 
 -- on Cost.carrier_id=Carr.carrier_id 
 -- Left  join envios.cantidad_de_envios as Cde 
 -- on Cost.Zona=Cde.zona
 -- Group by Cde.zona;

-- Justificación Pregunta 2 parte a
SELECT   distinct (Cde.zona) AS ZONA , sum(Capacity)  AS Capacidad_total_Carrier, Cantidad_de_envios
FROM envios.costos as Cost
Left  join envios.carrier as Carr 
on Cost.carrier_id=Carr.carrier_id 
Left  join envios.cantidad_de_envios as Cde
on Cost.Zona=Cde.zona
Group by Cde.zona;


-- Justificación Pregunta 2 parte b
SELECT distinct (Cde.zona) AS ZONA, Cantidad_de_envios/sum(Capacity)*sum(Cost.Costo) AS Costo_Zona
FROM envios.costos as Cost
Left  join envios.carrier as Carr 
on Cost.carrier_id=Carr.carrier_id 
Left  join envios.cantidad_de_envios as Cde
on Cost.Zona=Cde.zona
Group by Cde.zona;