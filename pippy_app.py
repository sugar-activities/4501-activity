#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Copyright (C) 2011 Ezequiel Pereira <eze2307@gmail.com>
#       Copyright (C) 2011, 2012 Daniel Francis <francis@sugarlabs.org>.
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       

import os, time, snack
salida = False
os.chdir(os.path.join(os.environ['HOME'],
                      "Activities/YumDownloader.activity/descarga"))
while not salida:
	screen = snack.SnackScreen()
	_salida, modo = snack.ListboxChoiceWindow(screen, "Modo de descarga",
				  "Elije un modo para descargar el paquete",
				  ["Descargar el RPM",
				   "Descargar el contenido del RPM (RPM descomprimido)", 					   "Descargar el RPM y el contenido del mismo",
				   "Descargar el RPM y sus dependencias",
				"Descargar un grupo"], buttons=["Ok", "Salir"])
	if _salida != "salir":
		data = snack.EntryWindow(screen, "Paquete a descargar", "Escribe los siguientes datos", ["Nombre del paquete o grupo: ", "Directorio donde se guardará lo descargado: "])
		if data[0] == "ok":
			pack, dir = data[1]
			screen.suspend()
			if modo == 0:
				os.system("yumdownloader --disablerepo=dextrose " + pack)
				os.system("mv *.rpm " + dir)
				raw_input("Presiona enter para continuar")
				screen.resume()
			elif modo == 1:
				os.system("yumdownloader --disablerepo=dextrose " + pack)
				os.system("rpm2cpio *.rpm | cpio -ivd")
				os.system("rm *.rpm")
				os.system("mv * " + dir)
				raw_input("Presiona enter para continuar")
				screen.resume()
			elif modo == "3":
				os.system("yumdownloader --disablerepo=dextrose " + pack)
				os.system("rpm2cpio *.rpm | cpio -ivd")
				os.system("mv * " + dir)
				raw_input("Presiona enter para continuar")
				screen.resume()
			elif modo == "4":
				os.system("yumdownloader --disablerepo=dextrose --resolve " + pack)
				os.system("mv *.rpm " + dir)
				raw_input("Presiona enter para continuar")
				screen.resume()
			elif modo == "5":
				os.system("yumdownloader --disablerepo=dextrose --resolve @" + pack)
				os.system("mv *.rpm " + dir)
				raw_input("Presiona enter para continuar")
				screen.resume()
	else:
		salida = True
	screen.finish()
