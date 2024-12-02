# INTRODUCCION

Este es el principal OOT para GNU Radio creado en la Escuela de Ingenierías Eléctrica Electrónica y Telecomunicaciones (E3T) de la UIS con el propósito de la formación en las asignaturas de comunicaciones. Esta versión está adaptada y probad con GNU Radio version 3.8.1 con Python 3.8.2. Como es bien sabido, un OOT es una especie de libreria, pero no de Python sino de GNURadio, por eso tiene una forma especial de instalación.

# PRERREQUISITOS (DEPENDENCIAS)
## Cosas que se supone que ya tienes:
- Debe estar instalado previamente gnuradio. No te decimos como porque depende de la version y tus intereses.
- git
- cmake
- make

Aquí se describe lo que hay que instalar previamente. Lo que se instala solo la primera vez. Usted no debe hacer esto si ya ha instalado antes este paquere y ahora solo quiere actualizarlo.

Todo lo siguiente se instala en forma de comandos por terminal ubuntu.

## Ahora sí a instalar dependencias
$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo apt install --fix-broken xterm python3-pip python3-click-plugins

$ pip3 install numpy scipy mako sphinx lxml pyqt5 click zmq markdown cython matplotlib pyyaml

$ pip3 install git+https://github.com/pyqtgraph/pyqtgraph@master

$ pip3 install git+https://github.com/hortegab/comdig_DiagramaOjo.3.8

# LA INSTALACION DEL OOT E3TRADIO
- Entra a la carpeta principal del paquete bajado del github y crea allí la subcarpeta "build"
- Entra a esa subcarpeta "build" y allí abre una terminal de comandos de ubunto
- Envía por el terminal los siguientes comandos:

$ sudo cmake ..

$ sudo make

$ sudo make install

$ sudo ldconfig

# CORRECCION DE PATH (solo para usuarios de maquinas de Carlos Mario en Google Cloud)
OJO: ignora esta parte, solo aplica para maquinas virtuales en Google Cloud, hechas por Carlos Mario

- La instalación con Python 3.8.2 tiene por ahora un bug a corregir. Al parecer el problema es por usar Python 3.8.2, pues al parecer GNURadio 3.1 está siendo más frecuentemente usado en versiones anteriores. El problema consiste en que:

  -- Los paquetes aparecen instalados en la carpeta:  /usr/local/lib/python3
  -- pero necesitamos que aparezca en /usr/local/lib/python3.8

- Eso se soluciona con el comando:
sudo cp -r /usr/local/lib/python3/dist-packages/E3TRadio /usr/local/lib/python3.8/dist-packages/











