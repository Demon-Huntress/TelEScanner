# TelEScanner
Buscador de números de teléfono españoles para outputs de "Facebook Latest Comments Scraper" (APIFY)

DESCRIPCIÓN

Este programa extrae los posibles teléfonos de España que figuren previamente en comentarios de grupos de facebook,
scrapeados mediante la aplicacion APIFY "Facebook Latest Comments Scraper", por lo que este programa está condicionado
a su formato de salida (.json).

- Ejecuta este script e introduce en la consola el nombre del archivo JSON ej.: "miArchivo.json"
- Se generará un archivo "listaNumeros.txt" con todos los números. Guardado en la carpeta "/Output"

Los archivos generados por APIFY deben colocarse en el directorio "APIFY/FBLCS". Además, allí se encontrará un archivo
de prueba llamado "fblcs_test.json"
