'''
Card images : https://github.com/SSC-SDE/Blackjack/tree/main/cards
'''

import os
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random
import time



'Card Class'
class Card:
    def __init__(self, rank, suit, val, adress):
        self.rank = rank
        self.suit = suit
        self.val = val
        self.adress = adress


'Canvas Parametres'
'----------------------------------------------------------------------------------------------------'
os.chdir('C:/Users/yasin/PycharmProjects/blackjack/cards')
root = tk.Tk()
myCanvas = tk.Canvas(root, bg="white", height=310, width=310)
root.title('Blackjack created by YasnTrk')
root.geometry("1200x800")

bg = Image.open('bg.png')
background = ImageTk.PhotoImage(bg)
bg_label = tk.Label(image=background)
bg_label.image = background
bg_label.pack(fill='both')


'Global Variables'
'--------------------------------------------------------'
global desk_img,player1_img,player2_img,annc
global player1, player2, deck, desk, player_point, player2_point
global player1_score, player2_score, desk_score
global played_tours
global loc_x, loc_y, desk_x, desk_y
global score_board, label2, announcer
global back_of_card,end_game
desk_img,player1_img,player2_img,annc = [],[],[],[]
player1 = []
player2 = []
desk = []
player1_score = 0
player2_score = 0
player1_point = 0
end_game = 0
player2_point = 0
desk_score = 0
played_tours = 0
loc_x = 900
loc_y = 500
desk_x = 500
desk_y = 200

'Commonly used parameters and values'
'--------------------------------------------------------------------'

SUITS = ["diamond", "spade", "heart", "club"]
VALUES = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10,
          'king': 10}

deck = [Card(key, suit, value, key + '_' + suit + '.png') for suit in SUITS for key, value in VALUES.items()]
back_of_card = 'back.png'

score_board = tk.Label(root, text='Player1: ' + str(player1_score) + '\n' + 'Player2: ' + str(player2_score))
score_board.place(x=0, y=0)

'----------------------------------------------------------------------------------------------------'


def give_card(card_name, card2):
    '''
    gives a random card to the first and second player and puts them on the table
    :param card_name: first is for the first player
    :param card2: second card is for the second player
    :return: nothing
    '''
    global loc_y, loc_x, player1_score, player1, player2_score, player2_point, desk_score,player2_img
    # Player1
    if player1_score <= 21:
        player1.append(card_name)
        image = Image.open(card_name.adress)
        card = ImageTk.PhotoImage(image)
        label = tk.Label(image=card)
        label.image = card
        player1_img.append(label)
        label.place(x=loc_x, y=loc_y)
        loc_x = loc_x + 50
        player1_score = player1_score + card_name.val
        print(player1_score,'Player 1 Skoru')

    if player2_score < 16:
        # Player2
        player2.append(card2)
        image = Image.open(card2.adress)
        card = ImageTk.PhotoImage(image)
        label = tk.Label(image=card)
        label.image = card
        player2_img.append(label)
        label.place(x=loc_x - 550, y=loc_y)

        player2_score = player2_score + card2.val
        print(player2_score, 'Player 2 Skoru')


def stand(card3):
    '''
    :param card3: A card from the random function card3.
    the table plays until it loses or wins
    '''
    global desk_score, desk, desk_y, desk_x,player2_score,player1_score,desk_score
    if desk_score < 16:
        # Desk
        desk.append(card3)
        image = Image.open(card3.adress)
        card = ImageTk.PhotoImage(image)
        label = tk.Label(image=card)
        label.image = card
        label.place(x=desk_x + 200, y=desk_y)
        desk_img.append(label)
        desk_score = desk_score + card3.val
        desk_x = desk_x + 100


def give_random():
    '''
    Takes and returns random values ​​from a list.
    '''
    card1 = random.choice(deck)
    deck.remove(card1)
    return card1


def desk_plays():
    '''
    this function is calculating  the winner
    the table plays until it loses or completes the rules
    At the end of the function, a text is written about who wins.
    '''
    global desk_img,desk_score,announcer,player1_point,player2_score,player1_score,player2_point,loc_x,loc_y,annc
    label2.destroy()
    card2 = desk[1]
    image = Image.open(card2.adress)
    card = ImageTk.PhotoImage(image)
    label = tk.Label(image=card)
    label.image = card
    label.place(x=desk_x + 100, y=desk_y) #Place Image into the Canvas
    while desk_score < 16: #Check desk score
        card3 = give_random()
        stand(card3)
        time.sleep(0.1)
    if player1_score < 12:
        for i in player1:
            if '1' == i.rank:
                player1_score = player1_score + 10
    if player2_score < 12:
        for i in player2:
            if '1' == i.rank:
                player2_score = player2_score + 10
    if desk_score < 12:
        for i in desk:
            if '1' == i.rank:
                desk_score = desk_score + 10

    '''
    Calculating the Winner with comparing scores 
    '''
    if player2_score <= 21 and desk_score > 21 or player2_score == 21 or (player1_score <= player2_score <= 21 and player2_score >= desk_score):
        player2_point += 1
        print('Player 2 Won')
        announcer = tk.Label(text = 'Player 2 Won',font= 100)
        announcer.place( x = loc_x-650, y = loc_y-200)
        annc.append(announcer)
    if (player1_score <= 21 and desk_score > 21 or player1_score == 21) or (player2_score <= player1_score <= 21 and player1_score >= desk_score):
        player1_point += 1
        announcer = tk.Label(text='Player 1 Won',font= 100)
        announcer.place(x=loc_x - 650, y=loc_y - 200)
        annc.append(announcer)
    if (desk_score == 21 and (player1_score != 21 and player2_score != 21)) or (21 >= desk_score > player1_score and desk_score > player2_score):
        announcer = tk.Label(text='Desk Won',font= 100)
        announcer.place(x=loc_x - 650, y=loc_y - 200)
        annc.append(announcer)
    if player2_score <= 21 and player1_score > 22 and desk_score > 22:
        announcer = tk.Label(text = 'Player 2 Won',font= 100)
        announcer.place( x = loc_x-650, y = loc_y-200)
        annc.append(announcer)
    if player1_score <= 21 and player2_score > 22 and desk_score > 22:
        announcer = tk.Label(text = 'Player 1 Won',font= 100)
        announcer.place( x = loc_x-650, y = loc_y-200)
        annc.append(announcer)
    if player1_score > 21 and player2_score > 21 and desk_score < 22:
        announcer = tk.Label(text = 'Desk Won',font= 100)
        announcer.place( x = loc_x-650, y = loc_y-200)
        annc.append(announcer)
    if player2_score <= player1_score <= 21 and player1_score >= desk_score:
        score_board.configure(text='Player2: ' + str(player2_point) + '\n' + 'Player1: ' + str(player1_point))
    else:
        score_board.configure(text = 'Player1: ' + str(player1_point) + '\n' + 'Player2: ' + str(player2_point))

def plot_card(): #Give Random Cards
    '''
    plot the cards I wrote it because the button needs an another function
    '''
    global label
    card = give_random() #Take Random card from Random function
    card2 = give_random()
    give_card(card, card2)


def players_starts():
    '''
    Choose random cards and give it to desk and put them into the Canvas for 2 players
    '''
    global player1_score, player2_score, player1, player2, loc_x, loc_y
    cardp_1 = random.choice(deck) #Player starter cards
    cardp_2 = random.choice(deck)
    player2.append(cardp_1) #Add them to the list
    player2.append(cardp_2)

    player2_score = cardp_1.val + cardp_2.val

    image = Image.open(cardp_1.adress) #Plot the cards
    card = ImageTk.PhotoImage(image)
    label = tk.Label(image=card)
    label.image = card
    label.place(x=loc_x - 600, y=loc_y)

    image = Image.open(cardp_2.adress)
    card = ImageTk.PhotoImage(image)
    label = tk.Label(image=card)
    label.image = card
    label.place(x=loc_x - 550, y=loc_y)


    '--------------------------------'
    card1_p2 = random.choice(deck) #Player 2 starter cards
    card2_p2 = random.choice(deck)
    player1.append(card1_p2)
    player1.append(card2_p2)
    player1_score = card1_p2.val + card2_p2.val

    image = Image.open(card1_p2.adress)  #Plot the cards
    card = ImageTk.PhotoImage(image)
    label = tk.Label(image=card)
    label.image = card
    label.place(x=loc_x - 100, y=loc_y)

    image = Image.open(card2_p2.adress)
    card = ImageTk.PhotoImage(image)
    label = tk.Label(image=card)
    label.image = card
    label.place(x=loc_x - 50, y=loc_y)
    print(player1_score, 'Başlangıç 1. Oyuncu Puanı')


def desk_starts():
    '''
    Choose random cards and give it to desk and put them into the Canvas
    '''
    global desk_score, desk, label2
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    desk.append(card1)
    desk.append(card2)
    desk_score = card1.val + card2.val
    '-----------------------------------------'
    image = Image.open(card1.adress)
    card = ImageTk.PhotoImage(image)
    label = tk.Label(image=card)
    label.image = card
    label.place(x=desk_x, y=desk_y)
    '----------------------------------------'
    image2 = Image.open(back_of_card)
    card2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(image=card2)
    label2.image = card2
    label2.place(x=desk_x + 100, y=desk_y)


def score(): #Calculate Score
    '''
    Calculate the Score
    :return:
    '''
    global player_point, player2_point, player1_score, desk_score,player2_score
    if player1_score == 21 or desk_score > 21:
        player_point += 1
    if player2_score == 21 or desk_score > 21:
        player2_point += 1

def restart(): ######################### Delete Everything
    '''
    Restart everything
    :return:
    '''
    global player1, player2, deck, desk, player_point, player2_point,desk_img,player1_img,player2_img,annc
    global player1_score, player2_score, desk_score
    global played_tours
    global loc_x, loc_y, desk_x, desk_y
    global score_board, label2, announcer
    global back_of_card, end_game
    player1 = []
    player2 = []
    desk = []
    player1_score = 0
    player2_score = 0
    end_game = 0
    desk_score = 0
    played_tours = 0
    loc_x = 900
    loc_y = 500
    desk_x = 500
    desk_y = 200
    try:
        for i in annc:
            i.destroy()
    except:
        pass
    for crd1 in desk_img:
        crd1.destroy()
    for crd2 in player2_img:
        crd2.destroy()
    for crd3 in player1_img:
        crd3.destroy()
    main()

'Buttons'
'----------------------------------------------------------------------------------------------------'

btn = tk.Button(root, text='Hit', command=plot_card,height= 2, width= 5) #Take Card
btn.place(x=600, y=700)

btn2 = tk.Button(root, text='Stand', command=desk_plays,height= 2, width= 5) #Wait for Desk to Play
btn2.place(x=650, y=700)

btn3 = tk.Button(root, text='Play again', command=restart, height= 2, width= 7) #Play again
btn3.place(x=625, y=650)

player2_label = tk.Label(root, text='Player 2', font=22) #Player 2 Label
player2_label.place(x=loc_x - 580, y=loc_y - 50)

player1_label = tk.Label(root, text='Player 1', font=22)  #Player 1 Label
player1_label.place(x=loc_x - 65, y=loc_y - 50)

player1_label = tk.Label(root, text='Desk', font=60) #Desk Label
player1_label.place(x=desk_x+100, y=desk_y-50)


'----------------------------------------------------------------------------------------------------'

for i in range(0,200,25): #To Create Fake Decks
    image1 = Image.open(back_of_card)
    back = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=back)
    label1.image = back
    label1.place(x=1000-i, y=75) #Coordinats

    image2 = Image.open(back_of_card)
    back2 = ImageTk.PhotoImage(image1)

def main():
    '''
    Main Function
    :return:
    '''
    while True:
        desk_starts()
        players_starts()
        root.mainloop()

if __name__ == '__main__':
    while True:
        main()



