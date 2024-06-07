# Wtyczka-2
PROJEKT_2
Wtyczka do Qgisa
Aby wtyczka poprawnie działała i pojawiła się w Qgisie należy z repozytorium o nazwie "Wtyczka-2" skopiować wszystkie pliki oprócz .git i skopiować do nowo utworzonego folderu w folderze "plugins".
W projekcie o nazwie "proj2.qgz" są zaimportowane punkty na dwóch warstawach. Aby użyć wtyczki należy wejść w ten plik i otworzyć go w Qgisie.
Należy zainstalować wtyczkę w Qgisie o nazwie "proj2_inf"
Cel ćwiczenia: Napisanie wtyczki do Qgisa za pomocą Pythona, która dla zaznaczonych punktów obliczy przewyższenie pomiędzy dwoma punktami albo pole poligonu utworzonego przez punkty (conajmniej 3).
Sposób użycia wtyczki: 
-Użytkownik musi wybrać punkty poleceniem 'zaznacz obiekty' na jednej warstwie
-Następnie wczytać wtyczkę "proj2_inf", co spowoduje otwarcie okna dialogowego
-Należy wybrać warstwę, na której są zaznaczone punkty oraz wybrać jedną z dwóch opcji: 'Oblicz dh' lub 'Oblicz pole' 
Pole oblicza z punktów na warstwie "punkty_uklad_2000_6 "
Przwyższenie dh oblicza z warstwy "agencje_zatrudnienia"
-Wynik pojawi się po prawej stronie użytego przycisku
-Aby wyjść z okna należy nacisnąć 'ok' lub 'anuluj'
-Wtyczka obsługuje kilka błędów. Gdy program odczyta błąd wyświetli się okno o danym błędzie;
przykładowe błędy:
  - Użytkownik wybierze inną ilość punktów niż 2 a chce obliczyć dh. Należy pamiętać, że jeśli użytkownik wybierze złą warstwę a dobrą ilość punktów, to także pojawi się ten komunikat, ponieważ NA DANEJ WARSTWIE jest wybrane 0 punktów. (Pojawi się błąd: "Na obecnej warstwie nie wybrano dokładnie 2 punktów.")
  - Użytkownik wybierze mniej niż 3 punkty a chce obliczyć pole.  Należy pamiętać, że jeśli użytkownik wybierze złą warstwę a dobrą ilość punktów, to także pojawi się ten komunikat, ponieważ NA DANEJ WARSTWIE jest wybrane 0 punktów.  (Pojawi się błąd: "Na obecnej warstwie nie wybrano co najmniej 3 punktów.")
  - Jeśli zaznaczone punkty do obliczenia dh nie miałyby w tabeli atrybutów atrybutu wysokosc: (Pojawi się błąd : "Brak atrybutu: wysokosc"
  - Jeśli zaznaczone punkty do obliczenia dh miałyby nieprawidłowe wartości atrybutu wysokosc: (Pojawi się błąd : "Nieprawidłowa wartość wysokości w jednym z punktów"

