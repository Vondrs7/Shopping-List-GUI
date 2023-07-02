import sqlite3
from sqlite3 import Error as SQLError


class Database():

    def setup(self):

        # soupis typů sloupečků v databázi a jejich typy
        self.table = (
            "BEGIN TRANSACTION",
            """
            -- New Table for new User
            CREATE TABLE IF NOT EXISTS Data (
            item_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name   TEXT (100) NOT NULL,
            item_price  TEXT (10) NOT NULL,
            date        TEXT (10) NOT NULL,
            amount      TEXT (10) NOT NULL,
            unit        TEXT (10) NOT NULL,
            discount    TEXT (10) NOT NULL,
            shop_name   TEXT (100) NOT NULL,      
            shop_city   TEXT (100) NOT NULL,
            user        TEXT (100) NOT NULL,
            comments    TEXT (1000)
            );
            """,
            "COMMIT TRANSACTION;")
         
    # metoda pro zápis nového produktu do databáze       
    def zapis(self, uzivatel, nazev, cena, datum, mnozstvi, jednotka, sleva, obchod, mesto, komentar):
        conn = None
        lists = "lists.db" 
        conn = self.pripojeni(lists)
        data_in = "INSERT INTO Data (item_name, item_price, date, amount, unit, discount, shop_name, shop_city, user, comments) VALUES (?,?,?,?,?,?,?,?,?,?)" 

        try:
            cur = conn.cursor()
            cur.execute(data_in,(nazev, cena, datum, mnozstvi, jednotka, sleva, obchod, mesto, uzivatel, komentar))
            conn.commit()
        except SQLError as e:
            print(e)
    
    # metoda pro čtení dat z tabulky
    def vypis(self,uzivatel):
        conn = None
        lists = "lists.db" 
        conn = self.pripojeni(lists)   
        cur = conn.cursor()

        cur.execute('SELECT item_name, item_price, date, amount, unit, discount, shop_name, shop_city, user, item_id, comments FROM Data WHERE user = (?)',(uzivatel,))
        return cur.fetchall()

    # metoda pro výpis konkrétního nákupu vybraného v tabulce předvýběru
    def vypis_datum_predvyber(self, uzivatel):
        conn = None
        lists = "lists.db" 
        conn = self.pripojeni(lists)   
        cur = conn.cursor()

        cur.execute('SELECT date, shop_name, shop_city, item_id FROM Data WHERE user = (?)',(uzivatel,))
        return cur.fetchall()
    
    # metoda pro výpis konkrétního nákupu vybraného v tabulce podle data, města a obchodu
    def vypis_datum_vyber(self, uzivatel, datum, obchod, mesto):
        conn = None
        lists = "lists.db" 
        conn = self.pripojeni(lists)   
        cur = conn.cursor()

        cur.execute('SELECT item_name, item_price, date, amount, unit, discount, shop_name, shop_city, user, item_id, comments FROM Data WHERE user = (?) AND date = (?) AND shop_name = (?) AND shop_city = (?)',(uzivatel, datum, obchod, mesto))
        return cur.fetchall()
    
    # metoda pro filtrování dat z tabulky
    def filtr(self, uzivatel, nazev, cena, datum, mnozstvi, jednotka, sleva, obchod, mesto, komentar):
        conn = None
        lists = "lists.db" 
        conn = self.pripojeni(lists)   
        
        try:
            cur = conn.cursor()
            cur.execute('SELECT item_name, item_price, date, amount, unit, discount, shop_name, shop_city, user, item_id, comments FROM Data WHERE user LIKE (?) AND item_name LIKE (?) AND item_price LIKE (?) AND date LIKE (?) AND amount LIKE (?) AND unit LIKE (?) AND discount LIKE (?) AND shop_name LIKE (?) AND shop_city LIKE (?) AND comments LIKE (?)',(uzivatel, nazev, cena, datum, mnozstvi, jednotka, sleva, obchod, mesto, komentar,))
            return cur.fetchall()
        except SQLError as e:
            self.chyba = e
            print(e)
    
    # metoda pro smazání vybraného řádku
    def smazat(self, vypis_id):
        conn = None
        lists = "lists.db" 
        conn = self.pripojeni(lists)   
        cur = conn.cursor()

        cur.execute("DELETE FROM Data WHERE item_id = (?)",(vypis_id))
        conn.commit()

    # metoda pro úpravu vybraného řádku
    def uprav(self, vypis_id, nazev, cena, datum, mnozstvi, jednotka, sleva, obchod, mesto, komentar):
        conn = None
        lists = "lists.db" 
        conn = self.pripojeni(lists)
        data_in = "UPDATE Data SET item_name = (?), item_price = (?), date = (?), amount = (?), unit = (?), discount = (?), shop_name = (?), shop_city = (?), comments = (?) WHERE item_id = (?)" 

        try:
            cur = conn.cursor()
            cur.execute(data_in,(nazev, cena, datum, mnozstvi, jednotka, sleva, obchod, mesto, komentar, vypis_id))
            conn.commit()
        except SQLError as e:
            print(e)

    # metoda pro připojení k databázi
    def pripojeni(self, lists_file):       
        conn = None      
        try:
            conn = sqlite3.connect(lists_file)
            return conn       
        except SQLError as e:
            print(e)
        return conn
    
    # metoda pro vytvoření tabulky
    def vytvorit_tab(self, conn, table):
        try:
            cur = conn.cursor()
            cur.execute(table)
        except SQLError as e:
            print(e)

    # hlavní metoda pro funkci třídy s tabulkou
    def main(self):
        self.setup()      
        lists = "lists.db" # vytvoří nový soubor ve složce
        conn = self.pripojeni(lists) # vytvoří připojení k databázi
        if conn is not None:
            for x in self.table:
                self.vytvorit_tab(conn, x)
            conn.close() # ukončí spojení
        else:
            print("Chyba! Nelze vytvořit spojení s databází.\n" + SQLError)
    
if __name__ == '__main__':
    db = Database() 
    db.main()
