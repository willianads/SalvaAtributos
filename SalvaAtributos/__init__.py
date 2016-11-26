# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SalvaAtributos
                                 A QGIS plugin
 extrai atributos de arquivos vetoriais paa CSV
                             -------------------
        begin                : 2016-11-26
        copyright            : (C) 2016 by IBGE Willian Alves
        email                : willianads@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SalvaAtributos class from file SalvaAtributos.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .salva_atributos import SalvaAtributos
    return SalvaAtributos(iface)
