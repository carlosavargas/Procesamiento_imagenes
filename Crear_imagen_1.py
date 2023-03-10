# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:15:25 2023

@author: carlo
"""

from PIL import Image

imagen=Image.new('RGB',(400,300),'green')
imagen.show()

"""
# Abrir imagen

image = Image.open('bote1.png')
image.show()
"""

#rotar imagen
"""
imagen = Image.open('bote1.png')
rotada = imagen.rotate(180)
rotada.show()
"""

#version pequeña
"""
image = Image.open('boat.jpg')
image.thumbnail((200, 200))
image.show()
"""