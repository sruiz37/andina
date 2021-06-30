#processor nombre del procesador
from platform import processor, python_implementation, python_version, python_version_tuple
print (processor ())

#system nombre del sistema operativo
from platform import system
print (system ())

#machine caracteristicas de la maquina
from platform import machine 
print (machine ())

#platform informacion sobre sistema operativo, v. interprete, descrupcion de entorno
from platform import platform
print (platform ())

print(python_implementation())
print(python_version_tuple())