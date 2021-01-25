# -*- coding: utf-8 -*-

from tkinter import *
import os
import os.path
import webbrowser
from tkinter import messagebox
import socket
from socket import error as SocketError

w1 = Tk()
w1.resizable(0,0)
w1.geometry('1250x550')
w1.iconphoto(False, PhotoImage(file='consolePy.png'))
w1.title('Web Hacking Studio')

score = 0

defis = ['0', '0', '0', '0', '0', '0', '0']

def affDefis():
    global defis
    w4 = Toplevel(w1, padx = 5)
    w4.title('Défis')
    w4.iconphoto(False, PhotoImage(file='help.png'))
    
    main = LabelFrame(w4, padx = 20)
    main.grid()
    Label(main, text='Javascript reading  : ').grid(row = 0, column = 0, sticky = 'w')
    Label(main, text=defis[0]).grid(row = 0, column = 1, sticky = 'w')
    Label(main, text='XSS attack : ').grid(row = 1, column = 0, sticky = 'w')
    Label(main, text=defis[1]).grid(row = 1, column = 1, sticky = 'w')
    Label(main, text='Base 64 decrypting : ').grid(row = 2, column = 0, sticky = 'w')
    Label(main, text=defis[2]).grid(row = 2, column = 1, sticky = 'w')
    Label(main, text='Javascript obfuscation : ').grid(row = 3, column = 0, sticky = 'w')
    Label(main, text=defis[3]).grid(row = 3, column = 1, sticky = 'w')
    Label(main, text='Javascript Mangled : ').grid(row = 4, column = 0, sticky = 'w')
    Label(main, text=defis[4]).grid(row = 4, column = 1, sticky = 'w')
    Label(main, text='Server Bruteforce : ').grid(row = 5, column = 0, sticky = 'w')
    Label(main, text=defis[5]).grid(row = 5, column = 1, sticky = 'w')
    Label(main, text='Javascript Analyze : ').grid(row = 6, column = 0, sticky = 'w')
    Label(main, text=defis[6]).grid(row = 6, column = 1, sticky = 'w')
    Button(w4, text='Quitter', command=w4.destroy).grid()
    
def getHelp():
    global n
    w2 = Toplevel(w1)
    w2.title('Aide')
    w2.iconphoto(False, PhotoImage(file='help.png'))
    c1 = Frame(w2)
    c1.grid(padx = 20, pady = 20)
    h1 = StringVar()
    p = StringVar()
    code = StringVar()
    h11 = Label(c1, font=('Consolas', 16), justify='center', textvariable=h1)
    h11.grid()
    p1 = Label(c1, font=('Consolas', 12), textvariable=p, height=4, justify='center')
    p1.grid()
    code1 = Label(c1, font='Consolas 13', textvariable=code, height=1, justify='center')
    code1.grid()
    Button(c1, text='FERMER', command=w2.destroy, padx = 10).grid(pady = 10)
    if(n == 1):
        h1.set('Aide pour la lecture Javascript')
        p.set('Sous Firefox, appuyez sur Ctrl+Maj+C afin d\'afficher le code source de la page.\nTrouvez le moyen d\'afficher le code source et lisez la condition Javascript permettant\nde vérifier si le mot de passe est bon ou pas.N\'hésitez pas à vous renseigner sur le\nJavascript !')
        code.set('Nécessite de connaitre un minimum le Javascript')
    elif(n == 2):
        h1.set('Aide pour l\'injection XSS')
        p.set('Renseignez-vous sur l\'injection XSS : Comment insérer une image dans une entrée\nde texte avec l\'affichage de la variable \'admin\' en cas d\'erreur ?')
        code.set('Nécessite de connaitre le HTML et le Javascript')
    elif(n == 3):
        h1.set('Aide pour la base 64')
        p.set('Savez-vous ce qu\'est une base 64 ? Le mot de passe ici est codé en base 64, à\nvous de trouver la commande Javascript pour les traduire directement ! N\'hésitez pas à\nutiliser Internet pour vous renseigner !')
        code.set('Nécessite uniquement la console et du Javascript')
    elif(n==4):
        h1.set('Aide pour la desobfuscation')
        p.set('Une obfuscation est un moyen de rendre un code illisible pour l\'homme afin\nde le protéger des personnes mal intentionnées. Il existe une balise\nJavascript qui permet de décrypter un code obfusqué de bas niveau.\nFaites vos recherches pour trouver cette commande !')
        code.set('Nécessite uniquement la console et du Javascript')
    elif(n==5):
        h1.set('Aide pour la désobfuscation en mangled')
        p.set('Sur JsFuck.com, il est possible d\'obfusquer du Javascript en Mangled. Mais\nil est également possible de le désobfusquer ! Faites des recherches\nsur Internet, de nombreux tutos existent.')
        code.set('Nécessite des connaissances un peu plus poussé en Javascript')
    elif(n==6):
        h1.set('Aide pour bruteforce du server Python')
        p.set('Il vous faut créer un programme en python vous permettant de tester toutes\nles combinaisons à trois chiffres possibles jusqu\'à trouver la bonne.\nUtilisez la librairie Socket, sur le port 8888, en localhost et\nattendez le message \'Welcome\'')
        code.set('Nécessite des connaissances poussées en Python avec la librairie Socket')
    elif(n==7):
        h1.set('Aide pour l\'analyse Javascript')
        p.set('Analyser le Javascript afin de découvrir le nom d\'utilisateur et le mot de passe défini par les deux fonctions \"setUsr()\" et \"setPass()\".\nN\'hésitez pas à vous renseigner sur les fonctions que vous ne connaissez pas.')
        code.set('Nécessite de connaitre un minimum le Javascript et d\'avoir réussi les défis précédents')
    else:
        h1.set('Aide générale')
        p.set('Ce logiciel vous permet d\'apprendre les bases de la sécurité web. N\'oubliez pas de sauvegarder régulièrement votre progression !') 
        code.set('Pour toute demande, ou conseil, allez dans le menu \'Tools > Infos\'')

def getRapport():
    webbrowser.open('info.txt')
def sendFeedback():
    import subprocess
    messagebox.showinfo('Feedback', 'Vous avez des suggestions ? Des idées ? Envoyez nous un mail à : web.hstdio@mail.fr (l\'adresse mail a été copiée dans votre presse-papier).')
    cmd = 'echo web.hstdio@mail.fr |clip'
    subprocess.check_call(cmd, shell=True)
    
def getMore():
    w3 = Toplevel(w1)
    w3.title('Infos')
    w3.geometry('400x370')
    w3.iconphoto(False, PhotoImage(file='help.png'))

    frMain = Frame(w3, padx=50)
    frMain.grid()

    Label(frMain, text='Web Hacking Studio', font='hack 20', pady=50).grid()
    Label(frMain, text='v1.6_Win10 (beta)', font='hack 14').grid()
    Label(frMain, text='CE Evan Koehler').grid()
    Label(frMain, text='Images (logo) : https://icones8.fr/ (Icones8)').grid()
    Label(frMain, text='Développé en Python, HTML, Javascript, CSS').grid()
    Label(frMain, text = 'Développé sous Visual Studio Code\n').grid()
    Button(frMain, text='Générer rapport de version', command = getRapport).grid()
    Button(frMain, text = 'Des suggestions ?', command = sendFeedback).grid()

def serverOpened():

    messagebox.showwarning('Server', 'Veuillez lancer le programme de bruteforce pour lancer la console server et cliquez sur OK pour continuer')

    w5 = Toplevel(w1)
    w5.title('Console Server')
    console = Text(w5, font='consolas 13', bg='#000000', fg='#FFFFFF')
    console.grid()

    hote = ''
    port = 8888

    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((hote, port))
    connexion_principale.listen(1)
    console.insert(END, "Le serveur écoute à présent sur le port {}".format(port))

    connexion_avec_client, infos_connexion = connexion_principale.accept()
    console.insert(END, '\nInfos client : ')
    console.insert(END, infos_connexion)

    msg_recu = b""
    while True:
        msg_recu = connexion_avec_client.recv(1024)
        if(msg_recu == b"702"):
            connexion_avec_client.send(b"Welcome")
            console.insert(END, '\nAccess granted')
            break
        else:
            connexion_avec_client.send(b"Wrong")
        
    console.insert(END, "\nFermeture de la connexion")
    connexion_avec_client.close()
    connexion_principale.close()

def launchTest():
    global n
    if(n==1):
        webbrowser.open('javascriptHack.html')
        #javascript.html : validate1
    elif(n==2):
        webbrowser.open('XSSAttack.html')
        #XSSAttack.html : Uw8NjMSkDjc
    elif(n==3):
        webbrowser.open('b64Hack.html')
        #b64Hack.html : b64PassValid
    elif(n==4):
        webbrowser.open('desobfuscation.html')
        #desobfuscation.html : obfPassEscape
    elif(n==5):
        webbrowser.open('native_code.html')
        #native_code.html : bfJsMangled
    elif(n==6):
        serverOpened()
        #client.py : 702
    elif(n==7):
        webbrowser.open('whatsUseful.html')
        #whatsUseful.html : {'usr1' : 'admin5'}
    else:
        messagebox.showerror('Error', 'Veuillez choisir un défi !')
def passtest():
    global n, password, score, defis
    
    pw = password.get()
    l = open('options.aes', 'w')
    score = int(score)
    password.config(text='')

    if(n==1 and pw=='validate1'):
        if('0' in defis[0]):
            score = score + 5
            d.set('Score : ' + str(score))
            defis = ['1', defis[1], defis[2], defis[3], defis[4], defis[5], defis[6]]
            messagebox.showinfo('Bravo', 'Vous avez réussi ce défi !', icon='info')
        else:
            messagebox.showinfo('Mais ?', 'Vous aviez déjà réussi ce défi...', icon='info')
    elif(n==2 and pw=='Uw8NjMSkDjc'):
        if('0' in defis[1]):
            score = score + 10
            d.set('Score : ' + str(score))
            defis = [defis[0], '1', defis[2], defis[3], defis[4], defis[5], defis[6]]
            messagebox.showinfo('Bravo', 'Vous avez réussi ce défi !', icon='info')
        else:
            messagebox.showinfo('Mais ?', 'Vous aviez déjà réussi ce défi...', icon='info')
    elif(n==3 and pw=='b64PassValid'):
        if('0' in defis[2]):
            score = score + 15
            d.set('Score : ' + str(score))
            defis = [defis[0], defis[1], '1', defis[3], defis[4], defis[5], defis[6]]
            messagebox.showinfo('Bravo', 'Vous avez réussi ce défi !', icon='info')
        else:
            messagebox.showinfo('Mais ?', 'Vous aviez déjà réussi ce défi...', icon='info') 
    elif(n==4 and pw=='obfPassEscape'):
        if('0' in defis[3]):
            score = score + 20
            d.set('Score : ' + str(score))
            defis = [defis[0], defis[1], defis[2], '1', defis[4], defis[5], defis[6]]
            messagebox.showwarning('Bravo','Vous avez réussi ce défi !', icon='info')
        else:
            messagebox.showinfo('Mais ?', 'Vous aviez déjà réussi ce défi...', icon='info')
    elif(n==5 and pw=='bfJsMangled'):
        if('0' in defis[4]):
            score = score + 35
            d.set('Score : ' + str(score))
            defis = [defis[0], defis[1], defis[2], defis[3], '1', defis[5], defis[6]]
            messagebox.showwarning('Bravo','Vous avez réussi ce défi !', icon='info')
        else:
            messagebox.showinfo('Mais ?', 'Vous aviez déjà réussi ce défi...', icon='info')
    elif(n==6 and pw=='702'):
        if('0' in defis[5]):
            score += 50
            d.set('Score : ' + str(score))
            defis = [defis[0], defis[1], defis[2], defis[3], defis[4], '1', defis[6]]
            messagebox.showwarning('Bravo','Vous avez réussi ce défi !', icon='info')
        else:
            messagebox.showinfo('Mais ?', 'Vous aviez déjà réussi ce défi...', icon='info')
    elif(n==7 and pw=='admin5'):
        if('0' in defis[6]):
            score += 30
            d.set('Score : ' + str(score))
            defis = [defis[0], defis[1], defis[2], defis[3], defis[4], defis[5], '1']
            messagebox.showwarning('Bravo','Vous avez réussi ce défi !', icon='info')
        else:
            messagebox.showinfo('Mais ?', 'Vous aviez déjà réussi ce défi...', icon='info')
    elif(n==0):
        messagebox.showwarning('Défi manquant', 'Choisissez d\'abord un défi')
    else:
        messagebox.showwarning('Wrong !', 'Mauvais mot de passe ! Réessayez l\'épreuve !')
    password.delete(0, 'end')
    l.write(str(score))
def setText(self):
    global n, frOn, launch
    launch.grid()
    frOn.grid()
    if(defChoose.curselection()[0] == 0):
        titre.set('JAVASCRIPT READING')
        description.set('Retrouvez le mot de passe administrateur grâce au javascript de la page.')
        aide.set('Trouvez un moyen d\'afficher le code source de la page via \'inspecter l\'élément\' : essayez F12 ou Ctrl+Maj+C')
        n = 1
    elif(defChoose.curselection()[0] == 2):
        titre.set('BASE 64 DECRYPTING')
        description.set('Décryptez le mot de passe administrateur en base 64.')
        aide.set('La base 64 est un encodage très basique accessible depuis toutes les machines. N\'hésitez pas à vous renseigner !')
        n = 3
    elif(defChoose.curselection()[0] == 1):
        titre.set('XSS ATTACK')
        description.set('Faites une attaque XSS pour obliger le site à vous montrer le mot de passe administrateur.')
        aide.set('Une attaque XSS consiste à insérer du code dans une entrée de texte d\'un site Internet. Renseignez-vous !')
        n = 2
    elif(defChoose.curselection()[0] == 3):
        titre.set('JAVASCRIPT OBFUSCATION')
        description.set('Trouvez le mot de passe administrateur en décryptant le javascript de la page')
        aide.set('Une Obfuscation consiste à rendre illisble du code Javascript pour l\'homme en laissant éxecutable pour la machine')
        n = 4
    elif(defChoose.curselection()[0] == 4):
        titre.set('JAVASCRIPT MANGLED')
        description.set('Le mot de passe est caché dans le Javascript de cette page. Trouvez un moyen de le décrypter.')
        aide.set('Pour cela, vous aurez besoin du site JsFuck.com (voir HTML du défi).\n')
        n = 5
    elif(defChoose.curselection()[0] == 5):
        titre.set('BRUTEFORCE PYTHON SERVER')
        description.set('Le server est protégé par un mot de passe à trois chiffres. Faites un bruteforce grâce à un programme Python.')
        aide.set('Pour cela, vous aurez besoin de la librairie Socket')
        n = 6
    elif(defChoose.curselection()[0] == 6):
        titre.set('JAVASCRIPT ANALYZING')
        description.set('Trouvez le nom d\'utilisateur et le mot de passe en lisant et en comprenant le javascript de la page.')
        aide.set('Pour cela, vous aurez besoin de comprendre le Javascript et d\'avoir réussi les défis précédents')
        n = 7
    else:
        titre.set('')
        description.set('')
        aide.set('')
def passtest2(self):
    passtest()
def save():
    global defis, score
    if(os.path.isfile('levels.aes')):
        d = messagebox.askyesno(title = 'Sure ?', message = 'Vous avez déjà une sauvegarde. Souhaitez-vous l\'écraser ?')
        if(d == True):
            p = open('levels.aes', 'r+')
            p.write('{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(defis[0], defis[1], defis[2], defis[3], defis[4], defis[5], defis[6]))
            p = open('options.aes', 'r+')
            p.write(str(score))
            messagebox.showinfo('Saved', 'Votre progression a été sauvegardée.')
def chargeSaved():
    global defis, score
    try:
        p = open('levels.aes', 'r+')
        p1 = p.readline()
        p2 = p.readline()
        p3 = p.readline()
        p4 = p.readline()
        p5 = p.readline()
        p6 = p.readline()
        p7 = p.readline()
        defis = [p1, p2, p3, p4, p5, p6, p7]
        p = open('options.aes', 'r+')
        score = p.readline()
        d.set('Score : ' + str(score))
        messagebox.showinfo('Succès', 'Votre sauvegarde a été chargée.')
    except FileNotFoundError:
        messagebox.showinfo('Erreur', 'Aucune sauvegarde n\'a été trouvée.')

n = 0

frRight = Frame(w1, width = 1140, height = 450)
frRight.grid_propagate(1)
frRight.grid(row = 0, column = 1)
frLeft = Frame(w1)
frLeft.grid(row = 0, column = 0)

defChoose = Listbox(frLeft, font='hack 12', selectmode='single', height=20, width=25, fg="#FFFFFF", bg="#121212")
defChoose.insert(1, 'Javascript Reading')
defChoose.insert(2, 'XSS Attack')
defChoose.insert(3, 'Base 64 Decrypting')
defChoose.insert(4, 'Javascript Obfuscation')
defChoose.insert(5, 'Javascript Mangled')
defChoose.insert(6, 'Bruteforce server')
defChoose.insert(7, 'Javascript Analyzing')

defChoose.grid(row=0)

d = StringVar()
scoreAff = Label(frLeft, textvariable=d, font='hack 15')
d.set('Score : ' + str(score))
scoreAff.grid(row=1)

titre = StringVar()
title = Label(frRight, textvariable=titre, font='hack 20 bold', anchor='n', pady=10)
titre.set('Bienvenue !')
title.grid(row=0, column=0)
description = StringVar()
descr = Label(frRight, textvariable=description, font='hack', anchor='center', pady=20, padx=15)
description.set('Choisissez une défi dans la liste à gauche pour commencer')
descr.grid(row=1, column=0)
aide = StringVar()
help = Label(frRight, textvariable=aide, font='hack', anchor='center', pady=15, padx=5)
aide.set('Terminez tous les défis pour gagner !\n')
help.grid(row=2, column=0)

imageLaunch = PhotoImage(file = 'launchButton.png')
imageLaunch = imageLaunch.subsample(3, 3)
launch = Button(frRight, image = imageLaunch, pady=15, command=launchTest, fg="#FFFFFF", width = 300, height = 100)
launch['border'] = '0'
launch.grid()
launch.grid_forget()

frOn = Frame(frRight, pady=30)
frOn.grid()
formFrame = Frame(frOn, padx = 10, pady = 10)
formFrame.grid()
passFrame = LabelFrame(formFrame, font = 'consolas 13', text = ' MOT DE PASSE ')
passFrame.grid()
password = Entry(passFrame, bg="#121212", fg="#FFFFFF", width=50, justify='center', font='hack 15')
password.bind('<Return>', passtest2)
password.grid_configure(pady = 10)
password.grid()
imageSend = PhotoImage(file = 'sendButton.png')
imageSend = imageSend.subsample(3, 3)
send = Button(formFrame, image = imageSend, command=passtest, font='hack 12 bold')
send['border'] = '0'
send.grid(row = 0, column = 1)
frOn.grid_forget()

defChoose.bind('<<ListboxSelect>>', setText)

menu = Menu(w1)

menu1 = Menu(menu, tearoff=0)
menu.add_cascade(label='Home', menu=menu1)
menu1.add_command(label='Défis réussis', command=affDefis)
menu1.add_command(label = 'Sauvegarder', command = save)
menu1.add_command(label = 'Charger', command = chargeSaved)
menu1.add_command(label='Quit', command=w1.quit)
menu2 = Menu(menu, tearoff=0)
menu2.add_command(label='Aide', command=getHelp)
menu2.add_command(label='Infos', command=getMore)
menu.add_cascade(label='Tools', menu=menu2)
w1.config(menu=menu)

w1.mainloop()

# Objectifs :
#
# All done

# Difficultés :
#
# Développement d'un HTML vulnérable au XSS pour le 2ème défi
# Tentative de Dark mode mais c'était affreux (textes détourés) ==> Abandon
# Notation du score (problème de varType)
# Obfusquer suffisement mais pas trop le javascript du 4e défi
# Programmer le défi 6 (client et server)
# Programmer l'execution du défi 6 (qui ne peut être fait depuis le navigateur) ==> Incrusté directement dans le code du launcher
# Faire fonctionner le défi 6 au niveau server et client (différents messages d'erreur)
# Apprendre à faire des trucs beaux en CSS (c'est pas évident, hein, jpensais pas)

# Défi 5 : 
# window.prompt_ = window.prompt
# window.prompt = function(a, b){ debugger; return window.prompt_(a, b);}
#
# function(a, b){
#    debugger;
#    return window.prompt_(a, b);
# }

