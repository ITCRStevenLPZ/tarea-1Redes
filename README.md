# tarea-1Redes
Repositorio para tarea #1 Redes
## Introducción
SMTP es una tecnología que es usada globalmente todos los dias, es el segundo protocolo más usado después de HTTP. SMTP emula los correos postales de una manera virtual. Dentro de sus mayores virtudes es que no ocupa de plataformas centralizadas, por lo que es muy utilizado por muchos usuarios a nivel mundial.

SMTP posee limitaciones en cuanto a la recepción de mensajes en el servidor de destino, por lo que este protocolo siempre se ve acompañado de otros como POP o IMAP, dejandole a estos últimos la tarea de recibir mensajes, mientras que SMTP los envía.

Es evidente la importancia de esta tecnología, por lo que es también importante conocer cómo esta funciona. SMTP se basa en el modelo cliente-servidor (MUA-MTA-MSA), es totalmente basado en texto y la comunicación es lograda mediante la implementación de secuencias de comandos. Dentro de sus problemas se encuentra la falta de autenticación de emisiones y el spam, este último siendo el problema más grave.

Este documento, describe el ambiente de desarrollo y otros aspectos iniciales de la tarea número uno del curso de Redes del Tecnológico de Costa Rica. Dicha tarea consiste en la implementación del protocolo SMTP, acompañado del protocolo IMAP y el notificador NNTP en el lenguaje de programación Python y la biblioteca Twisted para GNU/Linux.
