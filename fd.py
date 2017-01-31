#!/usr/bin/python3

fich=open("/etc/passwd","r")
usuarios=fich.readlines()
for usuario in usuarios:
    token=usuario.split(':')
    print("Usuario:", token[0], " Shell: ", token[-1], end='')
