from quitanda_funcoes import *

#frutas = ["Laranja", "Melancia", "Morango"]
frutas = {"Laranja" : 1.50,
          "Melancia" : 7.30,
          "Morango" : 0.75}

cedulas = [20, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]


compra = menu(frutas,"BEM VINDO A QUINTANDA!")

fim_venda = final_venda(compra, cedulas)