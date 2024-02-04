import pickle
import os

adresse = fr'{os.getcwd()}\messages'


def ligne(nombre_d_alignement=1, caractere="-"):
    return caractere * nombre_d_alignement



def load_file():
    try:
        mails = pickle.load(open(f'{adresse}/mails', 'rb'))
    except FileNotFoundError:
        mails = []

    return mails

def save_file(mails):
    pickle.dump(mails, open(f'{adresse}/mails', 'bw'))


def read_mails(user):
    my_mails = []
    mails = load_file()
    for mail in mails:
        if mail['to'] == user and not mail['read']:
            my_mails.append(mail)
            mail['read'] = True
    save_file(mails)
    return my_mails

def check_mails(user):
    mails = load_file()
    for mail in mails:
        if mail['to'] == user and not mail['read']:
            print("You have new mail!")
            break


def write_mail(frum, to, body):
    mails = load_file()
    mails.append({'from': frum, 'to': to, 'body': body, 'read': False})
    save_file(mails)


def ascii_art(alignement = 0):
    print(f"""{ligne(' ', alignement)} _      _____ _     ____  ____  _      _____  
{ligne(' ', alignement)}/ \  /|/  __// \   /   _\/  _ \/ \__/|/  __/  
{ligne(' ', alignement)}| |  |||  \  | |   |  /  | / \|| |\/|||  \    
{ligne(' ', alignement)}| |/\|||  /_ | |_/\|  \_ | \_/|| |  |||  /_   
{ligne(' ', alignement)}\_/  \|\____\\____/\____/\____/\_/  \|\____\  
{ligne(' ', alignement)}                                              
{ligne(' ', alignement)}                 _  _                         
{ligne(' ', alignement)}                / \/ \  /|                    
{ligne(' ', alignement)}                | || |\ ||                    
{ligne(' ', alignement)}                | || | \||                    
{ligne(' ', alignement)}                \_/\_/  \|                    
{ligne(' ', alignement)}                                              
{ligne(' ', alignement)} _      _____ ____  ____  ____  _____ _____   
{ligne(' ', alignement)}/ \__/|/  __// ___\/ ___\/  _ \/  __//  __/   
{ligne(' ', alignement)}| |\/|||  \  |    \|    \| / \|| |  _|  \     
{ligne(' ', alignement)}| |  |||  /_ \___ |\___ || |-||| |_//|  /_    
{ligne(' ', alignement)}\_/  \|\____\\\\____/\____/\_/ \|\____\\\\____\\
\n\n\n""")

tryagain = True
ascii_art(40)

while tryagain:
    user = input("Quel est votre nom\n>>> ")
    if not user.strip():
        print("Erreur : Vous n'avez rien rempli")

    else:
        user = user.strip().title()
        tryagain = False


print(f"Salut {user} !")

tryAgain = True
while tryAgain:
    check_mails(user)
    print("1 : écrire un message à ...\n2 : lire vos messages\n3 : exit [-->]")
    choix = input(">>> ")
    if choix == '1':
        destinataire = input(f"À qui voulez-vous écrire ? [NAME] : ")
        ecrit = input(f"Que voulez-vous écrire à {destinataire.lower().title()} ? : ")
        write_mail(user, destinataire.strip().title(), ecrit)
    elif choix == '2':
        my_mails = read_mails(user)
        for my_mail in my_mails:
            print(f"{ligne(20, caractere=' ')}De: {my_mail['from']} - {my_mail['body']}")
    elif choix == '3':
        n = input(f"Vous voulez quitter ? [Y/n] \n>>> ")
        if n == 'Y':
            exit(1000000000)
    elif choix == 'ZZ':
        print(load_file())





