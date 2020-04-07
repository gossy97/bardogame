
import pygame
from pygame.locals import *
import random
import copy

import pandas as pd
import ibm_db
import ibm_db_dbi
import sqlalchemy

player_name = "player_name"



dsn_driver = "IBM DB2 ODBC DRIVER"
dsn_database = "BLUDB"
dsn_hostname = "dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net"
dsn_port = "50000"
dsn_protocol = "TCPIP"
dsn_uid = "jrk61454"
dsn_pwd = "5@3tb6hk2kxdmfbw"

ibm_db_conn = ibm_db.connect("DATABASE=BLUDB;"
                                  "HOSTNAME=dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net;"
                                  "PORT=50000;"
                                  "PROTOCOL=TCPIP;"
                                  "UID=jrk61454;"
                                  "PWD=5@3tb6hk2kxdmfbw;",
                                  "", "")
conn = ibm_db_dbi.Connection(ibm_db_conn)
db2 = sqlalchemy.create_engine('ibm_db_sa://jrk61454'
                                    ':5@3tb6hk2kxdmfbw'
                                    '@dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net'
                                    ':50000'
                                    '/BLUDB')

LEFT = 1
RIGHT = 3

# Load Images
icon = pygame.image.load('resources/icon.png')
cBack = pygame.image.load('resources/cards/cardback.png')
diamondA = pygame.image.load('resources/cards/ad.png')
clubA = pygame.image.load('resources/cards/ac.png')
heartA = pygame.image.load('resources/cards/ah.png')
spadeA = pygame.image.load('resources/cards/as.png')
diamond2 = pygame.image.load('resources/cards/2d.png')
club2 = pygame.image.load('resources/cards/2c.png')
heart2 = pygame.image.load('resources/cards/2h.png')
spade2 = pygame.image.load('resources/cards/2s.png')
diamond3 = pygame.image.load('resources/cards/3d.png')
club3 = pygame.image.load('resources/cards/3c.png')
heart3 = pygame.image.load('resources/cards/3h.png')
spade3 = pygame.image.load('resources/cards/3s.png')
diamond4 = pygame.image.load('resources/cards/4d.png')
club4 = pygame.image.load('resources/cards/4c.png')
heart4 = pygame.image.load('resources/cards/4h.png')
spade4 = pygame.image.load('resources/cards/4s.png')
diamond5 = pygame.image.load('resources/cards/5d.png')
club5 = pygame.image.load('resources/cards/5c.png')
heart5 = pygame.image.load('resources/cards/5h.png')
spade5 = pygame.image.load('resources/cards/5s.png')
diamond6 = pygame.image.load('resources/cards/6d.png')
club6 = pygame.image.load('resources/cards/6c.png')
heart6 = pygame.image.load('resources/cards/6h.png')
spade6 = pygame.image.load('resources/cards/6s.png')
diamond7 = pygame.image.load('resources/cards/7d.png')
club7 = pygame.image.load('resources/cards/7c.png')
heart7 = pygame.image.load('resources/cards/7h.png')
spade7 = pygame.image.load('resources/cards/7s.png')
diamond8 = pygame.image.load('resources/cards/8d.png')
club8 = pygame.image.load('resources/cards/8c.png')
heart8 = pygame.image.load('resources/cards/8h.png')
spade8 = pygame.image.load('resources/cards/8s.png')
diamond9 = pygame.image.load('resources/cards/9d.png')
club9 = pygame.image.load('resources/cards/9c.png')
heart9 = pygame.image.load('resources/cards/9h.png')
spade9 = pygame.image.load('resources/cards/9s.png')
diamond10 = pygame.image.load('resources/cards/10d.png')
club10 = pygame.image.load('resources/cards/10c.png')
heart10 = pygame.image.load('resources/cards/10h.png')
spade10 = pygame.image.load('resources/cards/10s.png')
diamondJ = pygame.image.load('resources/cards/jd.png')
clubJ = pygame.image.load('resources/cards/jc.png')
heartJ = pygame.image.load('resources/cards/jh.png')
spadeJ = pygame.image.load('resources/cards/js.png')
diamondQ = pygame.image.load('resources/cards/qd.png')
clubQ = pygame.image.load('resources/cards/qc.png')
heartQ = pygame.image.load('resources/cards/qh.png')
spadeQ = pygame.image.load('resources/cards/qs.png')
diamondK = pygame.image.load('resources/cards/kd.png')
clubK = pygame.image.load('resources/cards/kc.png')
heartK = pygame.image.load('resources/cards/kh.png')
spadeK = pygame.image.load('resources/cards/ks.png')

# Set Icon
pygame.display.set_icon(icon)

# Global Constants
black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)

cards = [ [0,diamondA], [1, clubA] , [2, heartA] , [3, spadeA] ,\
[4,diamond2], [5,club2], [6,heart2], [7,spade2], \
[8,diamond3], [9,club3], [10,heart3], [11,spade3], \
[12,diamond4], [13,club4], [14,heart4], [15,spade4], \
[16,diamond5], [17,club5], [18,heart5], [19,spade5], \
[20,diamond6], [21,club6], [22,heart6], [23,spade6], \
[24,diamond7], [25,club7], [26,heart7], [27,spade7], \
[28,diamond8], [29,club8], [30,heart8], [31,spade8], \
[32,diamond9], [33,club9], [34,heart9], [35,spade9], \
[36,diamond10], [37,club10], [38,heart10], [39,spade10], \
[40,diamondJ], [41,clubJ], [42,heartJ], [43,spadeJ], \
[44,diamondQ], [45,clubQ], [46,heartQ], [47,spadeQ], \
[48,diamondK], [49,clubK], [50,heartK], [51,spadeK] ]


def genCard(cList, xList):
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    return card

def initGame(cList, uList, dList):
    '''Liste da usare: carte, user, dealer'''
    #card1, cA = genCard(cList, uList)
    #card2, cA = genCard(cList, dList)
    #card3, cA = genCard(cList, uList)

def main():
    # Local Variable
    deck = []
    hand = []
    hand_rect = []
    table = []
    table_rect = []
    pot = []
    pot_rect = []

    #initGame(deck, hand, table)

    #Initialize Game
    pygame.init()
    screen = pygame.display.set_mode((640*2, 480*2))
    pygame.display.set_caption('Bardogame')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Pesca', 1, black)
    restartTxt = font.render('Restart', 1, black)

    #Fill Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 150, 15))
    hitB = pygame.draw.rect(background, gray, (10, 445, 75, 25))
    restartB = pygame.draw.rect(background, gray, (800, 700, 75, 25))
    list1 = [[0], [1],[2],[3],[4],[50]]
    df1 = pd.DataFrame(list1)
    df1 = df1.rename(columns={0: "ID"})
    df1.to_sql('deck', con=db2, if_exists='replace')
    my_list = [[]]
    df = pd.DataFrame(my_list)
    df = df.rename(columns={0: "ID"})
    df.to_sql('hand_' + player_name, con=db2, if_exists='replace')
    df.to_sql('gametable', con=db2, if_exists='replace')
    df.to_sql('pot_' + player_name, con=db2, if_exists='replace')

    #Event Loop
    while True:
        listcazzo = []
        df = pd.read_sql("SELECT * FROM deck", conn)
        listcazzo = df.values.tolist()
        deck = []
        for i in range(len(listcazzo)):
            x = listcazzo[i][0]
            deck.append(cards[x])
        listcazzo = []

        df = pd.read_sql("SELECT * FROM hand_" + player_name, conn)
        listcazzo = df.values.tolist()
        listcazzo[:] = (value for value in listcazzo if value != [0])
        for i in range(len(listcazzo)):
            x = listcazzo[i][0]
            hand.append(cards[x])
        listcazzo = []

        df = pd.read_sql("SELECT * FROM pot_" + player_name, conn)
        listcazzo = df.values.tolist()
        listcazzo[:] = (value for value in listcazzo if value != [0])
        for i in range(len(listcazzo)):
            x = listcazzo[i][0]
            pot.append(cards[x])
        listcazzo = []

        df = pd.read_sql("SELECT * FROM gametable", conn)
        listcazzo = df.values.tolist()
        listcazzo[:] = (value for value in listcazzo if value != [0])
        for i in range(len(listcazzo)):
            x = listcazzo[i][0]
            table.append(cards[x])
        listcazzo = []


        gameover = False
        #background needs to be redisplayed because it gets updated
        #winTxt = font.render('Wins: %i' % winNum, 1, black)
        #puntitxt = font.render('Punti: %i' % punti, 1, black)

        #checks for mouse clicks on buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and hitB.collidepoint(pygame.mouse.get_pos()):
                card = genCard(deck, hand)

            elif event.type == pygame.MOUSEBUTTONDOWN and cBack.get_rect().collidepoint(pygame.mouse.get_pos()):
                card = genCard(deck, table)

            elif event.type == pygame.MOUSEBUTTONDOWN and restartB.collidepoint(pygame.mouse.get_pos()):
                #restarts the game, updating scores
                print("hai schiacciato restart")
                gameover = False
                hand = []
                table = []
                deck = copy.copy(cards)
                initGame(deck, hand, table)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                print("left")
                for rect in hand_rect:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        ccc = hand.pop(hand_rect.index(rect))
                        table.append(ccc)

                for rect in table_rect:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        ccc = table.pop(table_rect.index(rect))
                        hand.append(ccc)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:

                print("right")
                for rect in table_rect:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        ccc = table.pop(table_rect.index(rect))
                        pot.append(ccc)



        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (39, 448))
        screen.blit(restartTxt, (800, 700))

        #screen.blit(winTxt, (565, 423))
        #screen.blit(loseTxt, (565, 448))

        screen.blit(cBack, (10, 10))

        #displays table's cards
        table_rect.clear()
        for i in range(len(table)):
            x = 120 +  i* 110
            screen.blit(table[i][1], (110 + x, 10))
            table_rect.append(table[i][1].get_rect(topleft=(110 + x, 10)))


        #displays player's cards
        hand_rect.clear()
        for i in range(len(hand)):
            x = 10 +  i* 110
            screen.blit(hand[i][1], (x, 295))
            hand_rect.append(hand[i][1].get_rect(topleft=(x, 295)))

        # displays player's pot
        pot_rect.clear()
        for i in range(len(pot)):
            x = 10 + i * 30
            screen.blit(pot[i][1], (x, 295 + 285))
            pot_rect.append(pot[i][1].get_rect(topleft=(x, 295)))

        df = pd.DataFrame(deck)
        df = df.rename(columns={0: "ID"})
        df = df[df.ID != 0]
        df = df.drop(columns=1)
        df.to_sql('deck', con=db2, if_exists='replace')

        df = pd.DataFrame(hand)
        df = df[df.ID != 0]
        df = df.rename(columns={0: "ID"})
        try:
            df = df.drop(columns=1)
        except Exception:
            pass
        print(df)

        try:
            df.to_sql('hand_' + player_name, con=db2, if_exists='replace')
        except Exception:
            pass

        df = pd.DataFrame(table)
        df = df.rename(columns={0: "ID"})
        df = df[df.ID != 0]
        try:
            df = df.drop(columns=1)
        except Exception:
            pass
        try:
            df.to_sql('gametable', con=db2, if_exists='replace')
        except Exception:
            pass
        df = pd.DataFrame(pot)
        df = df.rename(columns={0: "ID"})
        df = df[df.ID != 0]
        try:
            df = df.drop(columns=1)
        except Exception:
            pass
        try:
            df.to_sql('pot_' + player_name, con=db2, if_exists='replace')
        except Exception:
            pass
        pygame.display.update()
            

if __name__ == '__main__':
    main()
