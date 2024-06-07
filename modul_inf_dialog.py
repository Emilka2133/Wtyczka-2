# -*- coding: utf-8 -*-
"""
/***************************************************************************
 qgis_klasaDialog
                                 A QGIS plugin
 wtyczka_proj2
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-03
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Magdalena Frąckiewicz i Emilia Felczak
        email                : magdalena.eler1@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsProject, QgsGeometry, QgsPointXY, Qgis, QgsWkbTypes, QgsVectorLayer
from qgis.utils import iface
from qgis.PyQt.QtWidgets import QMessageBox

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'modul_inf_dialog_base.ui'))


class qgis_klasaDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(qgis_klasaDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.pushButton_oblicz_dh.clicked.connect(self.calculate_dh)
        self.pushButton_oblicz_pole.clicked.connect(self.calculate_pole)
    
    def calculate_dh(self):
        """
        Funkcja licząca różnicę wysokosci między dwoma punktami.

        Parameters
        ----------
        Parametry pobrane za pomocą self. 
        h_1, h_2 - float
        h_1, h_2 - wysokosc punktu 1 i 2

        Returns
        -------
        dh - float
        dh - różnica wysokosci między dwoma punktami [m]

        """
        warstwa = self.mMapLayerComboBox.currentLayer()
        if not warstwa or warstwa.wkbType() != QgsWkbTypes.Point:
            QMessageBox.warning(self, 'Błąd', 'Proszę wybrać warstwę punktową')
            return
        features = warstwa.selectedFeatures()
        if len(features) != 2:
            QMessageBox.warning(self,'Błąd','Na obecnej warstwie nie wybrano dokładnie 2 punktów.')
            return 
        try:
            h_1 = float(features[0]['wysokosc'])
            h_2 = float(features[1]['wysokosc'])
        except KeyError as e:
            QMessageBox.warning(self, 'Błąd', 'Brak atrybutu: wysokosc')
            return
        except ValueError:
            QMessageBox.warning(self, 'Błąd', 'Nieprawidłowa wartość wysokości w jednym z punktów')
            return
        dh = h_2 - h_1
        dh = round(dh,3)
        self.label_wynik_dh.setText(f'{dh} m') 
        
        
    def calculate_pole(self):
        """
        Funkcja licząca pole pomiędzy conajmniej trzema punktami.

        Parameters
        ----------
        Parametry pobrane za pomocą self. 
        x, y - float
        x, y - współrzędne conajmniej trzech punktów

        Returns
        -------
        pole - int
        pole - pole pomiędzy conajmniej trzema punktami [m²]

        """
        warstwa = self.mMapLayerComboBox.currentLayer()
        if not warstwa or warstwa.wkbType() != QgsWkbTypes.Point:
            QMessageBox.warning(self, 'Błąd', 'Proszę wybrać warstwę punktową')
            return
        features = warstwa.selectedFeatures()
        if len(features) <3:
            QMessageBox.warning(self,'Błąd',' Na obecnej warstwie nie wybrano co najmniej 3 punktów. ')
            return
        punkty = []
        id_punktow = []
        for p in features:
            geom = p.geometry()
            punkt = geom.asPoint()
            punkty.append(QgsPointXY(punkt.x(), punkt.y()))
            id_punktow.append(p.id())
        n = len(punkty)
        pol_e = 0.0
        for i in range(n):
            x1, y1 = punkty[i].x(), punkty[i].y()
            x2, y2 = punkty[(i + 1) % n].x(), punkty[(i + 1) % n].y()
            pol_e += (x1 + x2)*(y2 - y1)
            pole=abs(pol_e/2)
            i=+1
        pole = int(pole)
        self.label_wynik_pole.setText(f'{pole} m²')
        
        
        

        

        