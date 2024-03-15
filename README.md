---Tor Ghost---
![g1](https://github.com/Nebur22/Tor-Ghost/assets/55068123/49e46f08-d87c-4443-96c1-6c61328296c6)

Cambiador de MAC y Anonimizador

-Este script de Python está diseñado para proporcionar una capa adicional de privacidad y anonimato en línea al cambiar la dirección MAC de tu dispositivo y utilizar la red TOR para ocultar tu dirección IP real. Ofrece varios modos de funcionamiento para adaptarse a diferentes necesidades y niveles de privacidad.

Modos de Funcionamiento:


1. Tor Normal:

Este modo utiliza la red TOR para enrutar tu tráfico a través de una serie de nodos anónimos, lo que oculta tu ubicación geográfica y dirección IP original.
Al seleccionar este modo, el script te guiará a través de los pasos para cambiar la dirección MAC de tu interfaz de red y luego iniciará TOR para establecer la conexión anónima.


2. Tor + Proxys:

Este modo va un paso más allá al permitirte configurar proxies SOCKS5 adicionales para mejorar aún más tu anonimato.
Después de cambiar la dirección MAC, el script te pedirá que ingreses una lista de proxies y puertos para utilizar en la configuración de ProxyChains, que se integrará con TOR para enrutar tu tráfico a través de los proxies seleccionados.


3. Modo Paranoico:

Diseñado para usuarios que buscan el máximo nivel de anonimato y privacidad en línea.
Este modo cambia periódicamente la dirección MAC de tu dispositivo, reinicia TOR para obtener una nueva dirección IP y actualiza la lista de proxies utilizados para complicar aún más el seguimiento del tráfico en línea.
Funcionamiento General:

Al ejecutar el script, se verifica si TOR está instalado en el sistema. Si no lo está, se ofrece al usuario la opción de instalarlo.
El usuario elige uno de los modos de funcionamiento disponibles según sus necesidades de privacidad y anonimato.
El script guía al usuario a través de los pasos necesarios en cada modo, como cambiar la dirección MAC, configurar proxies (en el caso del modo Tor + Proxys), y luego iniciar TOR para establecer la conexión segura y anónima.
Después de completar el modo seleccionado, el script proporciona instrucciones adicionales, como cómo detener TOR si es necesario y cómo reiniciar el proceso de anonimización si se utiliza el modo paranoico.
¡Con este script, puedes proteger tu privacidad en línea y navegar de forma más segura y anónima por la web!
