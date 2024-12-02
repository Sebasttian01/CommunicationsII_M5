# INTRODUCCION

comdig_Lib_Bloques.3.8 es una libreria de bloques jerarquicos para GNU Radio. Ha sido adaptada  y probada en la versión 3.8.1 de GNU Radio y con Python 3.8. Pero al dia de hoy ya se han 
probado con GNU Radio 3.9 y funcionan de maravilla. Claro está que para GNU Radio 3.9 tuvimos que retirar los bloques que permitian hallar el diagrama de ojo usando graficas externas de Matplotlib,
pero no nos ha importado porque esta nueva version trae su propio bloque para diagramas de hoy

# PRERREQUISITOS
- debe estar instalado GNURadio 3.8.1 o superior. Ya usamos al dia de hoy GNU Radio 3.9
- debe estar instalada el OOT E3TRadio3.8 ya que muchos de los bloques de este paquete reusan bloques de ese OOT 
enlace: https://github.com/hortegab/comdig_Lib_OOT_E3TRadio.3.8.git

# LA INSTALACION PRINCIPAL
- No hay que hacer una instalación por terminal de comandos
- Simplemente, abra GRC de GNURadio e instale bloque por bloque siguiendo este proceso:
  -- comienza por los bloques que están en la carpeta principal. Los abres desde gnuradio y los corres uno por uno. Entonces gnuradio los memorizará para su uso futuro
  -- Reinicia gnuradio y luego corre los bloques que están en la subcarpeta BloquesDependientes. Eso es debido a que estos dependen de la instalación previa de los primeros
  -- Finalmente corre los que aparecen en la subcarpeta "Bloques de cuidado en GNURadio 3.8.1"

# LA INSTALACION DE "Bloques de cuidado en GNURadio 3.8.1" (esto solo aplica a máquinas creadas con imagen para google cloud)
OJO: debes ignorar lo que dice aquí a menos que estés instalando estos bloques en una maquina en google cloud hecha a partir de una imagen de Carlos Mario. Es que el problema en realidad lo creó Carlos Mario con la manera en que creó los usuarios.
- Se refiere a los bloques que se encuentran en la carpeta "Bloques de cuidado en GNURadio 3.8.1"
- Lo que esos bloques jerarquicos tienen de particular es que incluyen uno o más bloques "Python Module" y/o "Python Block". Al correrlo de manera tradicional, un Python Module o un Python Block genera un .py que se almacena en el mismo lugar de donde ha sido leido el bloque jerarquico. Pero el lugar donde GNU Radio lo necesita es en "/home/usuario/.grc_gnuradio/" , donde usuario es el nombre del usuario Ubuntu.
- Una manera de hacer una instalación exitosa es la siguiente:
  * pase una copiaa de todos los bloques que desee instalar de la carpeta "Bloques de cuidado en GNURadio 3.8.1" a la carpeta "/home/usuario/.grc_gnuradio/" , donde usuario es el nombre del usuario Ubuntu.
  * desde GNURadio vaya a la carpeta  "/home/usuario/.grc_gnuradio/", desde allí llame cada uno de los bloques jerarquicos a instalar y corralos  uno por uno.
  
# LA INSTALACION DE "Bloques Fatales"
- Aquí se tienen unos bloques que definitivamente no pueden ser instalados en GNURadio 3.8.1 ya que usan elementos que han quedado obsoletos con esa versión de GNURadio
- El consejo es simple: no insista en instalarlos, olvídese de que existen. Si se llegaren a necesitar es necesario pensar en una manera de implementarlos con elementos de GNURadio 3.8.1. 

# LA COMPROBACION
- Actualiza librerias del GRC: oprime el ícono de la fecha circular de actualización "Reload Blocks"
- En el panel derecho del GRC revisa que existe la categoría "comdiguis".  

## Algunos consejos o notas:
- Es posible que un bloque no se pueda instalar debido a que consume un bloque que ya ha sido instalado pero que aún GNU Radio no lo reconoce porque la instalación fue muy reciente. En ese caso debes oprimir el ícono de la fecha circular de actualización "Reload Blocks"
- Es posible que un bloque no se pueda instalar debido a que consume un bloque que ya aún no ha sido instalado. En ese caso debes dejarlo para cuando ya tengas instalado esos los bloques.
- Note que los bloques de esta librería tienen un nombre que comienza por “_b”, pero si el bloque es tipo QT GUI, este comienza con “QT GUI_b”. Esto puede ser clave para reconocer qué tipo de bloque está usando un flujograma determina.

