import ibm_db
import pandas as pd
import ibm_db_dbi
import sqlalchemy
from PIL import Image
from IPython.display import HTML, display

dsn_driver = "IBM DB2 ODBC DRIVER"
dsn_database = "BLUDB"
dsn_hostname = "dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net"
dsn_port = "50000"
dsn_protocol = "TCPIP"
dsn_uid = "jrk61454"
dsn_pwd = "5@3tb6hk2kxdmfbw"

class Bardogame:

    def __init__(self, player_name = "player_name", deck = "standard_52", color = "red"):
        self.player_name = player_name
        self.deck = deck
        self.color = color
        self.ibm_db_conn = ibm_db.connect("DATABASE=BLUDB;"
                                 "HOSTNAME=dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net;"
                                 "PORT=50000;"
                                 "PROTOCOL=TCPIP;"
                                 "UID=jrk61454;"
                                 "PWD=5@3tb6hk2kxdmfbw;",
                                 "", "")
        self.conn = ibm_db_dbi.Connection(self.ibm_db_conn)
        self.db2 = sqlalchemy.create_engine('ibm_db_sa://jrk61454'
                                   ':5@3tb6hk2kxdmfbw'
                                   '@dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net'
                                   ':50000'
                                   '/BLUDB')
        
    def get_deck(self):
        deck = pd.read_sql("SELECT cards FROM " + self.deck +" ORDER BY RAND()", self.conn)
        deck.to_sql('deck', con=self.db2, if_exists='replace')
        img = Image.open(self.color + "_back.png")
        display(img)

    def draw_card(self, num_cards):
        deck = pd.read_sql("SELECT cards FROM deck", self.conn)
        draw_card = pd.DataFrame(deck.iloc[:num_cards])
        deck = deck.drop(draw_card.index, axis=0)
        deck.to_sql('deck', con=self.db2, if_exists='replace')
        draw_card.to_sql(self.player_name + "_hand", con=self.db2, if_exists='append')
        str1 = "<table><tr>"
        str_in = "<td><img src='"
        str_fin = "'></td>"
        str3 = "</tr></table>"
        str2 = ""
        print("Your hand:")
        hand = pd.read_sql("SELECT cards FROM " + self.player_name + "_hand", self.conn)
        for i in range(len(hand.CARDS)):
            str2 += str_in + str(hand.loc[i,"CARDS"]) + ".png" + str_fin
        string1 = str1+str2+str3
        display(HTML(string1))
        str2 = ""
        print("On the table:")
        table = pd.read_sql("SELECT cards FROM TABLE", self.conn)
        for i in range(len(table.CARDS)):
            str2 += str_in + str(table.loc[i,"CARDS"]) + ".png" + str_fin
        string1 = str1+str2+str3
        display(HTML(string1))

    def play_card(self, card):
        hand = pd.read_sql("SELECT cards FROM " + self.player_name + "_hand", self.conn)
        play_card = hand.loc[hand['CARDS'] == card]
        hand = hand.drop(play_card.index, axis=0)
        hand.to_sql(self.player_name+ "_hand", con=self.db2, if_exists='replace')
        play_card.to_sql('TABLE', con=self.db2, if_exists='append')
        str1 = "<table><tr>"
        str_in = "<td><img src='"
        str_fin = "'></td>"
        str3 = "</tr></table>"
        str2 = ""
        print("Your hand:")
        hand = pd.read_sql("SELECT cards FROM " + self.player_name + "_hand", self.conn)
        for i in range(len(hand.CARDS)):
            str2 += str_in + str(hand.loc[i,"CARDS"]) + ".png" + str_fin
        string1 = str1+str2+str3
        display(HTML(string1))
        str2 = ""
        print("On the table:")
        table = pd.read_sql("SELECT cards FROM TABLE", self.conn)
        for i in range(len(table.CARDS)):
            str2 += str_in + str(table.loc[i,"CARDS"]) + ".png" + str_fin
        string2 = str1+str2+str3
        display(HTML(string2))


    def win_card(self, card):
        table = pd.read_sql("SELECT cards FROM TABLE", self.conn)
        win_card = table.loc[table['CARDS'] == card]
        table = table.drop(win_card.index, axis=0)
        table.to_sql('TABLE', con=self.db2, if_exists='replace')
        win_card.to_sql(self.player_name + '_pot', con=self.db2, if_exists='append')
        str1 = "<table><tr>"
        str_in = "<td><img src='"
        str_fin = "'></td>"
        str3 = "</tr></table>"
        str2 = ""
        print("Your hand:")
        hand = pd.read_sql("SELECT cards FROM " + self.player_name + "_hand", self.conn)
        for i in range(len(hand.CARDS)):
            str2 += str_in + str(hand.loc[i,"CARDS"]) + ".png" + str_fin
        string1 = str1+str2+str3
        display(HTML(string1))
        str2 = ""
        print("On the table:")
        table = pd.read_sql("SELECT cards FROM TABLE", self.conn)
        for i in range(len(table.CARDS)):
            str2 += str_in + str(table.loc[i,"CARDS"]) + ".png" + str_fin
        string2 = str1+str2+str3
        display(HTML(string2))

    def show(self):
        str1 = "<table><tr>"
        str_in = "<td><img src='"
        str_fin = "'></td>"
        str3 = "</tr></table>"
        str2 = ""
        print("Your hand:")
        hand = pd.read_sql("SELECT cards FROM " + self.player_name + "_hand", self.conn)
        for i in range(len(hand.CARDS)):
            str2 += str_in + str(hand.loc[i,"CARDS"]) + ".png" + str_fin
        string1 = str1+str2+str3
        display(HTML(string1))
        str2 = ""
        print("On the table:")
        table = pd.read_sql("SELECT cards FROM TABLE", self.conn)
        for i in range(len(table.CARDS)):
            str2 += str_in + str(table.loc[i,"CARDS"]) + ".png" + str_fin
        string2 = str1+str2+str3
        display(HTML(string2))

    def card_table(self, num_cards):
        deck = pd.read_sql("SELECT cards FROM deck", self.conn)
        draw_card = pd.DataFrame(deck.iloc[:num_cards])
        deck = deck.drop(draw_card.index, axis=0)
        deck.to_sql('deck', con=self.db2, if_exists='replace')
        draw_card.to_sql('TABLE', con=self.db2, if_exists='append')
        str1 = "<table><tr>"
        str_in = "<td><img src='"
        str_fin = "'></td>"
        str3 = "</tr></table>"
        str2 = ""
        print("On the table:")
        table = pd.read_sql("SELECT cards FROM TABLE", self.conn)
        for i in range(len(table.CARDS)):
            str2 += str_in + str(table.loc[i,"CARDS"]) + ".png" + str_fin
        string = str1+str2+str3
        display(HTML(string))

    def clear_hand(self):
        stmt = ibm_db.exec_immediate(self.ibm_db_conn, "DROP TABLE " + self.player_name + "_hand")

    def clear_table(self):
        stmt = ibm_db.exec_immediate(self.ibm_db_conn, "DROP TABLE TABLE")
        
    def show_pot(self):
        print("Your pot:")
        pot = pd.read_sql("SELECT cards FROM " + self.player_name + "_pot", self.conn)
        str1 = "<table><tr>"
        str_in = "<td><img src='"
        str_fin = "'></td>"
        str3 = "</tr></table>"
        str2 = ""
        for i in range(len(pot.CARDS)):
            str2 += str_in + str(pot.loc[i,"CARDS"]) + ".png" + str_fin
        string = str1+str2+str3
        display(HTML(string))

        
        
  