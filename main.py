from PyQt6 import uic, QtWidgets
import sys
import pandas as pd
import os
from datetime import datetime

from database_lists import Database

# třída pro zobrazení a funkčnost okna pro zápis nového uživatele
class NovaOsobaForm(QtWidgets.QWidget):

    def __init__(self, **kwargs):
        super(NovaOsobaForm, self).__init__(**kwargs)

        # načtení okna
        self.generated_class, self.base_class = uic.loadUiType("New_profile.ui") 
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")

        # tlačítka
        self.form.Button_Save_Continue.clicked.connect(lambda:self.save_continue())  # tlačítko pro uložení jména
        self.form.Button_Cancel.clicked.connect(lambda:self.widget.close()) # tlačítko pro ukončení aplikace

    # metoda pro uležní uživatele
    # pokud není nic vyplněno, vypíše se chybová hláška
    def save_continue(self):
        self.vuf.nacteni_uzivatelu()
        if len(self.form.Input_name.text()) == 0:
            self.form.Label_error_message.setText("Chybné zadání, prosím opakujte.")
        else:
            self.vuf.ulozeni_uzivatele()
            self.vuf.vypis_uzivatelu()
            self.widget.close()

    # závislosti
    def setup(self):
        self.nof = app.nof
        self.vuf = app.vuf
        self.sl = app.sl
        self.fil = app.fil
        self.np = app.np

# třída pro zobrazení a funkčnost úvodního okna s výběrem uživatele 
class VyberUzivateleForm(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(VyberUzivateleForm, self).__init__(**kwargs)

        # načtení okna 
        self.generated_class, self.base_class = uic.loadUiType("Users_menu.ui")
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")

        # tlačítka
        self.form.Button_Cancel.clicked.connect(lambda:sys.exit(app.exec()))  # tlačítko pro ukončení aplikace
        self.form.Button_Create.clicked.connect(lambda:self.nof.widget.show()) # tlačítko pro zavolání (zobrazení) okna pro zápis nového uživatele
        self.form.Button_Delete.clicked.connect(lambda:self.dur.widget.show()) # tlačítko pro odebrání vybraného uživatele
        self.form.Button_Select.clicked.connect(lambda:self.vyber_uzivatele()) # tlačítko pro výběr požadovaného uživatele

        self.widget.show() # zobrazení okna s výběrem uživatele

    # metoda pro správu výběru uživatele a zobrazením dalšího okna (nákupního seznamu) po kliknutí na tlačítko
    def vyber_uzivatele(self):
        if self.form.Users.currentRow() >= 0:
            self.vybrany_uzivatel = self.form.Users.currentRow() # načte do proměnné vybraného uživatele
            self.sl.nacteni() # připraví data vybraného uživatele
            self.sl.widget.show() # zobrazí další okno s nákupním seznamem
            self.widget.close() # zavře okno s výběrem uživatele
        else:
            self.form.Label_error_message.setText("Prosím vyberte uživatele.")  


    # metoda pro uložení uživatele - nejprve ověří, zda již existuje csv soubor s uživateli
    # pokud ano: 
    #       - přidá na konec seznamu "members" (v kterém jsou načteny všechny již existující) nového uživatele
    #       - následně přepíše existující soubor csv a uloží zde všechny uživatele ze seznamu 
    # pokud ne:
    #       - vytvoří nový csv soubor a zapíše nové jméno 
    def ulozeni_uzivatele(self):
        self.members_ = []
        if os.path.exists("members.csv"): # ověří, zda soubor již existuje
            self.members.append(self.nof.form.Input_name.text()) # připojí na konec seznamu jméno zadané do kolonky tabulky
            self.nof.form.Input_name.setText("") # vymaže pole pro zadání textu
            for y in self.members:
                self.members_.append(y) # přepíše všechny uživatele do pomocného listu "members_"
            self.members = pd.DataFrame(data = self.members_, columns = ["name"]) # z pomocného listu "members_" zapíše do listu "members" všechny data ve formátu DataFrame
            self.members.to_csv("members.csv", encoding="utf-8")    # přepíše csv soubor a nahraje data z listu
        else:
            self.members = pd.DataFrame(data = [self.nof.form.Input_name.text()],columns = ["name"]) # přečte vepsané jméno z kolonky jména a nahraje do seznamu ve formátu DataFrame
            self.nof.form.Input_name.setText("") # vymaže pole pro zadání textu
            self.members.to_csv("members.csv", encoding="utf-8")    # vytvoří csv soubor a nahraje data ze seznamu

    # metoda zkontroluje, zda již existuje soubor scv se jmény
    # pokud ano, načte z něho data a uloži do seznamu "members"
    # pokud ne, nedělá nic 
    # spustí se při zapnutí aplikace
    def nacteni_uzivatelu(self):
        self.members = []
        if os.path.exists("members.csv"):
            self.data = pd.read_csv("members.csv")
            if self.data.shape[0] > 0:
                for i in range(self.data.shape[0]):
                    self.members.append(self.data["name"][i])

    # metoda vypíše uživatele ze seznamu "members" do tabulky widgetu 
    def vypis_uzivatelu(self):
        self.form.Users.clear()
        for uzivatel in self.members:
            self.form.Users.addItem(uzivatel)

    # metoda pro odebrání uživatele ze seznamu "members"
    def odebrat_uzivatele(self):
        if self.form.Users.currentRow() >= 0:
            del self.members[self.form.Users.currentRow()]
            self.vypis_uzivatelu()
            self.dur.widget.close()

    # závislosti
    def setup(self):
        self.nof = app.nof
        self.vuf = app.vuf
        self.sl = app.sl
        self.fil = app.fil
        self.np = app.np
        self.dur = app.dur

# třída pro zobrazení a funkčnost hlavního okna nákupního seznamu
class ShoppingList(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(ShoppingList, self).__init__(**kwargs)

        # načtení a zobrazení okna
        self.generated_class, self.base_class = uic.loadUiType("SList.ui")
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")

        self.form.Button_Cancel.clicked.connect(lambda:sys.exit(app.exec()))  # tlačítko pro ukončení aplikace
        self.form.Button_Filter.clicked.connect(lambda:self.fil.widget.show())
        self.form.Button_Change.clicked.connect(lambda:self.zmena_uzivatele())
        self.form.Button_Create.clicked.connect(lambda:self.np.widget.show())
        self.form.Button_Delete.clicked.connect(lambda:self.dr.widget.show())
        self.form.Button_Edit.clicked.connect(lambda:self.zmena_produktu())

    # metoda načte a vypíše data pro vybraného uživatele
    def nacteni(self):
        self.uzivatel_cislo = self.vuf.vybrany_uzivatel
        self.uzivatel = self.vuf.members[self.uzivatel_cislo]
        self.form.User_selected.setText(self.uzivatel)
        self.dat.main() # vytvoří databázi pokud neexistuje

        # výpis dat do tabulky
        self.vypis = self.dat.vypis(self.uzivatel) # podle zvoleného uživatele se do proménné uloží všechny jeho produkty
        column = 0
        try: # použité "try" pro případy, kdy je tabulak prázdná, aby nebyla chyba
            self.form.List.setRowCount(len(self.vypis))
            for items in self.vypis:
                for item in items:
                    self.form.List.setItem(0, column, QtWidgets.QTableWidgetItem(str(item)))
                    column=column+1
        except:
            pass

    # metoda se zavolá v případech, kdy je potřeba si vytáhnout aktuálního uživatele
    def ulozeny_uzivatel(self):
        return self.uzivatel

    # metoda pro změnu uživatele - vrátí okno s výběrem uživatele
    def zmena_uzivatele(self):
        self.vuf.widget.show()
        self.widget.close()

    # metoda pro smazání vybraného uživatele
    def smazat(self):
        self.dr.widget.close()
        if self.form.List.currentRow() >= 0:
            vybrany_produkt = self.form.List.currentRow() # nahraje se číslo řádku vybraného produktu
            vypis_radek = self.vypis[vybrany_produkt] # z výpisu se nahraje část dat podle řádku
            vypis_id = vypis_radek[9] # z požadovaných dat se vybere ID produktu
            self.dat.smazat(str(vypis_id))
            self.nacteni()

    # metoda pro úpravu/změnu označeného produktu
    def zmena_produktu(self):
        if self.form.List.currentRow() >= 0:
            vybrany_produkt = self.form.List.currentRow() # nahraje se číslo řádku vybraného produktu
            self.vypis_radek = self.vypis[vybrany_produkt] # z výpisu se nahraje část dat podle řádku
            self.vypis_id = self.vypis_radek[9] # z požadovaných dat se vybere ID produktu
            self.cp.widget.show()
            self.cp.vypis_produktu()   

    # závislosti
    def setup(self):
        self.nof = app.nof
        self.vuf = app.vuf
        self.sl = app.sl
        self.fil = app.fil
        self.np = app.np
        self.dr = app.dr
        self.cp = app.cp

        self.dat = app.dat

# třída pro okno filtru v hlavním okně nákupního lístku
class Filter(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(Filter, self).__init__(**kwargs)

        self.generated_class, self.base_class = uic.loadUiType("Filter_setup.ui")
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")

        self.form.Button_Back.clicked.connect(lambda:self.fil.widget.close())  # tlačítko pro ukončení aplikace
        self.form.Button_Search.clicked.connect(lambda:self.filtr())

    # propíšou se hodnoty do proměnných, dotáže se databáze a pošle zpět požadovaný výběr 
    def filtr(self):
            self.mnozstvi = self.form.Amount_choose.text()
            self.mesto = self.form.City_choose.text()
            self.nazev = self.form.Product_choose.text()  
            self.datum = self.form.Date_choose.text()
            self.sleva = self.form.Discount_choose.text()
            self.cena = self.form.Price_choose.text()
            self.obchod = self.form.Shop_choose.text()
            self.jednotka = self.form.Unit_choose.text()
            self.komentar = self.form.Comment_choose.text()

            self.chyba = ""
            self.uzivatel = self.sl.ulozeny_uzivatel() # načte si zvoleného uživatele do proměnné

            # pokud je kolonka prázdná, propíše se znak pro vyhledání všeho
            if len(self.mnozstvi) == 0:
                self.mnozstvi = "%"
            if len(self.mesto) == 0:
                self.mesto = "%"
            if len(self.nazev) == 0:
                self.nazev = "%"
            if len(self.datum) == 0:
                self.datum = "%"
            if len(self.sleva) == 0:
                self.sleva = "%"
            if len(self.cena) == 0:
                self.cena = "%"
            if len(self.obchod) == 0:
                self.obchod = "%"
            if len(self.jednotka) == 0:
                self.jednotka = "%"
            if len(self.komentar) == 0:
                self.komentar = "%"

            self.vypis = self.dat.filtr(self.uzivatel, self.nazev, self.cena, self.datum, self.mnozstvi, self.jednotka, self.sleva, self.obchod, self.mesto, self.komentar)
            # výpis dat do tabulky
            column = 0
            try: # použité "try" pro případy, kdy je tabulak prázdná, aby nebyla chyba
                self.sl.form.List.setRowCount(len(self.vypis))
                for items in self.vypis:
                    for item in items:
                        self.sl.form.List.setItem(0, column, QtWidgets.QTableWidgetItem(str(item)))
                        column=column+1
                
                #self.form.Message.setText(f"Špatně zadané hodnoty ({self.dat.chyba}).")
            except:
                pass

            self.widget.close()


    def setup(self):
        self.nof = app.nof
        self.vuf = app.vuf
        self.sl = app.sl
        self.fil = app.fil
        self.np = app.np
        self.dat = app.dat

# třída pro zadání nového produkltu v hlavním okně nákupního lístku
class NewProduct(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(NewProduct, self).__init__(**kwargs)

        self.generated_class, self.base_class = uic.loadUiType("New_product.ui")
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")

        now = datetime.now()
        self.form.Product_date.setText(f"{now.day}.{now.month}.{now.year}")

        self.form.Button_Back.clicked.connect(lambda:self.np.widget.hide())  # tlačítko pro ukončení aplikace
        self.form.Button_Save_Back.clicked.connect(lambda:self.uloz_zpet())
        self.form.Button_Save_Next.clicked.connect(lambda:self.uloz_dalsi())

    # parametry se uloží do proměnných a některá okna se vymažou
    def uloz_dalsi(self):
        # podmínka - pokdu určitá okna nejsou vyplněna, vypíše se chybová hláška
        if len(self.form.Product_amount.text()) == 0 or len(self.form.Product_city.text()) == 0 or len(self.form.Product_name.text()) == 0 or len(self.form.Product_date.text()) == 0 or len(self.form.Product_discount.text()) == 0 or len(self.form.Product_price.text()) == 0 or len(self.form.Product_shop.text()) == 0 or len(self.form.Product_unit.text()) == 0:
            self.np.form.Message.setText("Nejsou vyplněny všechny povinné údaje, prosím doplňte.")
        else:
            self.mnozstvi = self.form.Product_amount.text()
            self.mesto = self.form.Product_city.text()
            self.nazev = self.form.Product_name.text()  
            self.datum = self.form.Product_date.text()
            self.sleva = self.form.Product_discount.text()
            self.cena = self.form.Product_price.text()
            self.obchod = self.form.Product_shop.text()
            self.jednotka = self.form.Product_unit.text()
            self.komentar = self.form.Product_comments.text()

            self.uzivatel = self.sl.ulozeny_uzivatel() # načte si zvoleného uživatele do proměnné
            self.dat.zapis(self.uzivatel, self.nazev, self.cena, self.datum, self.mnozstvi, self.jednotka, self.sleva, self.obchod, self.mesto, self.komentar)
            self.sl.nacteni()

            # vymažou se některé kolonky, některé zůstanou, aby bylo vypňování jednodušší
            self.form.Message.setText("")
            self.form.Product_amount.setText("") # vymaže pole pro zadání textu
            self.form.Product_comments.setText("") # vymaže pole pro zadání textu
            self.form.Product_discount.setText("") # vymaže pole pro zadání textu
            self.form.Product_name.setText("") # vymaže pole pro zadání textu
            self.form.Product_price.setText("") # vymaže pole pro zadání textu
            self.form.Product_unit.setText("") # vymaže pole pro zadání textu

    # parametry se uloží a tabulka zmizí
    def uloz_zpet(self):
        # podmínka - pokdu určitá okna nejsou vyplněna, vypíše se chybová hláška
        if len(self.form.Product_amount.text()) == 0 or len(self.form.Product_city.text()) == 0 or len(self.form.Product_name.text()) == 0 or len(self.form.Product_date.text()) == 0 or len(self.form.Product_discount.text()) == 0 or len(self.form.Product_price.text()) == 0 or len(self.form.Product_shop.text()) == 0 or len(self.form.Product_unit.text()) == 0:
            self.np.form.Message.setText("Nejsou vyplněny všechny povinné údaje, prosím doplňte.")
        else:
            self.mnozstvi = self.form.Product_amount.text()
            self.mesto = self.form.Product_city.text()
            self.nazev = self.form.Product_name.text()  
            self.datum = self.form.Product_date.text()
            self.sleva = self.form.Product_discount.text()
            self.cena = self.form.Product_price.text()
            self.obchod = self.form.Product_shop.text()
            self.jednotka = self.form.Product_unit.text()
            self.komentar_prazdny()

            self.uzivatel = self.sl.ulozeny_uzivatel() # načte si zvoleného uživatele do proměnné
            self.dat.zapis( self.uzivatel, self.nazev, self.cena, self.datum, self.mnozstvi, self.jednotka, self.sleva, self.obchod, self.mesto, self.komentar)
            self.sl.nacteni()

            # vymažou se některé kolonky, některé zůstanou, aby bylo vypňování jednodušší
            self.form.Message.setText("")
            self.form.Product_amount.setText("") # vymaže pole pro zadání textu
            self.form.Product_comments.setText("") # vymaže pole pro zadání textu
            self.form.Product_discount.setText("") # vymaže pole pro zadání textu
            self.form.Product_name.setText("") # vymaže pole pro zadání textu
            self.form.Product_price.setText("") # vymaže pole pro zadání textu
            self.form.Product_unit.setText("") # vymaže pole pro zadání textu
            self.form.Product_date.setText("") # vymaže pole pro zadání textu
            self.form.Product_city.setText("") # vymaže pole pro zadání textu
            self.form.Product_shop.setText("") # vymaže pole pro zadání textu

            self.widget.close() # ukončí okno po vyplnění

    # ošetření, aby komentář nebyl nikdy prázdný pro zápis do tabulky
    def komentar_prazdny(self):
        if len(self.form.Product_comments.text()) == 0:
            self.komentar = " "
        else:
            self.komentar = self.form.Product_comments.text()

    def setup(self):
        self.nof = app.nof
        self.vuf = app.vuf
        self.sl = app.sl
        self.fil = app.fil
        self.np = app.np

        self.dat = app.dat

# okno pro opětovné zeptání se, zda má být produkt smazán
class DeleteReally(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(DeleteReally, self).__init__(**kwargs)

        self.generated_class, self.base_class = uic.loadUiType("Delete_really.ui")
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")
    
        self.form.Button_Back.clicked.connect(lambda:self.widget.close())
        self.form.Button_Delete.clicked.connect(lambda:self.sl.smazat())

    def setup(self):
        self.sl = app.sl

# okno pro úpravu/změnu produktu
class ChangeProduct(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(ChangeProduct, self).__init__(**kwargs)

        self.generated_class, self.base_class = uic.loadUiType("Change_product.ui")
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")
    
        self.form.Button_Back.clicked.connect(lambda:self.widget.close())
        self.form.Button_Save_Change.clicked.connect(lambda: self.er.widget.show())

    # vypíše do kolonek informace o produktu, které se budou moct přepsat
    def vypis_produktu(self):
        self.form.Product_name.setText(self.sl.vypis_radek[0])
        self.form.Product_price.setText(self.sl.vypis_radek[1])
        self.form.Product_date.setText(self.sl.vypis_radek[2])
        self.form.Product_amount.setText(self.sl.vypis_radek[3])
        self.form.Product_unit.setText(self.sl.vypis_radek[4])
        self.form.Product_discount.setText(self.sl.vypis_radek[5])
        self.form.Product_shop.setText(self.sl.vypis_radek[6])
        self.form.Product_city.setText(self.sl.vypis_radek[7])
        self.form.Product_comments.setText(self.sl.vypis_radek[10])

    # metoda načte upravené hodnoty do proměnných
    def uprav(self,vypis_id):
        # podmínka - pokdu určitá okna nejsou vyplněna, vypíše se chybová hláška
        if len(self.form.Product_amount.text()) == 0 or len(self.form.Product_city.text()) == 0 or len(self.form.Product_name.text()) == 0 or len(self.form.Product_date.text()) == 0 or len(self.form.Product_discount.text()) == 0 or len(self.form.Product_price.text()) == 0 or len(self.form.Product_shop.text()) == 0 or len(self.form.Product_unit.text()) == 0:
            self.np.form.Message.setText("Nejsou vyplněny všechny povinné údaje, prosím doplňte.")
        else:
            self.mnozstvi = self.form.Product_amount.text()
            self.mesto = self.form.Product_city.text()
            self.nazev = self.form.Product_name.text()  
            self.datum = self.form.Product_date.text()
            self.sleva = self.form.Product_discount.text()
            self.cena = self.form.Product_price.text()
            self.obchod = self.form.Product_shop.text()
            self.jednotka = self.form.Product_unit.text()
            self.komentar_prazdny()

            self.widget.close() # ukončí okno po vyplnění
            self.er.widget.close() 

            self.uzivatel = self.sl.ulozeny_uzivatel() # načte si zvoleného uživatele do proměnné
            self.dat.uprav( vypis_id, self.nazev, self.cena, self.datum, self.mnozstvi, self.jednotka, self.sleva, self.obchod, self.mesto, self.komentar)
            self.sl.nacteni()

    # ošetření, aby komentář nebyl nikdy prázdný pro zápis do tabulky
    def komentar_prazdny(self):
        if len(self.form.Product_comments.text()) == 0:
            self.komentar = " "
        else:
            self.komentar = self.form.Product_comments.text()

    def setup(self):
        self.sl = app.sl
        self.dat = app.dat
        self.er = app.er

# okno pro opětovné zeptání se, zda má být produkt upraven
class EditReally(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(EditReally, self).__init__(**kwargs)

        self.generated_class, self.base_class = uic.loadUiType("Edit_really.ui")
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")
    
        self.form.Button_Back.clicked.connect(lambda:self.widget.close())
        self.form.Button_Edit.clicked.connect(lambda:self.cp.uprav(self.sl.vypis_id))

    def setup(self):
        self.cp = app.cp
        self.sl = app.sl

# okno pro opětovné zeptání se, zda má být uživatel smazán
class DeleteUserReally(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(DeleteUserReally, self).__init__(**kwargs)

        self.generated_class, self.base_class = uic.loadUiType("Delete_user_really.ui")
        self.widget = self.base_class()
        self.form = self.generated_class()
        self.form.setupUi(self.widget)
        self.setWindowTitle("Nákupní Lístek JV")
    
        self.form.Button_Back.clicked.connect(lambda:self.widget.close())
        self.form.Button_Delete.clicked.connect(lambda:self.vuf.odebrat_uzivatele())

    def setup(self):
        self.vuf = app.vuf

# třída pro logickou vrstvu aplikace
# na začátku vyvolá načtzení načtení uživatelů z případného (existujícího) souboru scv
# následně vypíše uživatele do tabulky widgetu
class App(QtWidgets.QApplication):

    def build(self):
        self.nof = NovaOsobaForm()
        self.vuf = VyberUzivateleForm()
        self.sl = ShoppingList()
        self.fil = Filter()
        self.np = NewProduct()
        self.dr = DeleteReally()
        self.cp = ChangeProduct()
        self.er = EditReally()
        self.dur = DeleteUserReally()

        self.dat = Database()

        # jednotlivá okna aplikace
        self.vuf.setup()
        self.nof.setup()
        self.sl.setup()
        self.fil.setup()
        self.np.setup()
        self.dr.setup()
        self.cp.setup()
        self.er.setup()
        self.dur.setup()      

        self.vuf.nacteni_uzivatelu() # načte uživatele ze souboru scv
        self.vuf.vypis_uzivatelu() # vypíše uživatele do tabulky widgetu
        sys.exit(app.exec())


if __name__ == "__main__":

    app = App([])
    app.build()

