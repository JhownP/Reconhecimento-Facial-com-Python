# encoding: utf-8
from tkinter import *

import os
import captura
import treinamento
import reconhecedor_lbph
import reconhecedor_eigenfaces
import reconhecedor_fisherfaces
import popup

class Application:
    def __init__(self, master=None):

        frm_width = root.winfo_rootx() - root.winfo_x()
        win_width = 500 + 2 * frm_width
        win_height = 380 + frm_width
        x = root.winfo_screenwidth() // 2 - win_width // 2
        y = root.winfo_screenheight() // 2 - win_height // 2
        root.geometry('500x380+{}+{}'.format(x, y))
        root.title("APS - Sistema de Reconhecimento Facial")
        root['bg'] = '#353b48'

        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 80
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer["bg"] = '#353b48'
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 80
        self.segundoContainer["bg"] = '#353b48'
        self.segundoContainer.pack()

        self.segundoContainerId = Frame(master)
        self.segundoContainerId["padx"] = 80
        self.segundoContainerId["pady"] = 10
        self.segundoContainerId["bg"] = '#353b48'
        self.segundoContainerId.pack()

        self.terceiroContainer = Frame(master)
        self.segundoContainer["padx"] = 80
        self.terceiroContainer["pady"] = 15
        self.terceiroContainer["bg"] = '#353b48'
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 80
        self.quartoContainer["pady"] = 15
        self.quartoContainer["bg"] = '#353b48'
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 120
        self.quintoContainer["bg"] = '#353b48'
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 10
        self.sextoContainer["bg"] = '#353b48'
        self.sextoContainer.pack()

        # PRIMEIRO CONTAINER
        self.titulo = Label(self.primeiroContainer, text="APS - Sistema de Reconhecimento Facial")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo["bg"] = '#353b48'
        self.titulo["fg"] = '#f5f6fa'
        self.titulo.pack()

        # SEGUNDO CONTAINER
        # Solicitando Nome do Usuario
        self.aprendendo = Label(self.segundoContainer, text="Aprendizado Supervisionado - IA")
        self.aprendendo["font"] = ("Arial", "10", "italic")
        self.aprendendo["bg"] = '#353b48'
        self.aprendendo["fg"] = '#f5f6fa'
        self.aprendendo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel["bg"] = '#353b48'
        self.nomeLabel["fg"] = '#f5f6fa'
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.idLabel = Label(self.segundoContainerId, text="ID     ", font=self.fontePadrao)
        self.idLabel["bg"] = '#353b48'
        self.idLabel["fg"] = '#f5f6fa'
        self.idLabel.pack(side=LEFT)

        self.id = Entry(self.segundoContainerId)
        self.id["width"] = 30
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        # TERCEIRO CONTAINER
        # Botão de Abrir o Capturador de Fotos
        self.capturarImagem = Button(self.terceiroContainer)
        self.capturarImagem["text"] = "Capturar Imagens"
        self.capturarImagem["font"] = ("Calibri", "8")
        self.capturarImagem["width"] = 23
        self.capturarImagem["command"] = self.capturaImagem
        self.capturarImagem.pack(side=LEFT)

        self.capturarImagem = Button(self.terceiroContainer)
        self.capturarImagem["text"] = "Treinar Algoritmos"
        self.capturarImagem["font"] = ("Calibri", "8")
        self.capturarImagem["width"] = 23
        self.capturarImagem["command"] = self.treinamento
        self.capturarImagem.pack(side=LEFT)


        # Quarto Container
        self.aprendendo = Label(self.quartoContainer, text="Scripts de Reconhecimento - IA")
        self.aprendendo["font"] = ("Arial", "10", "italic")
        self.aprendendo["bg"] = '#353b48'
        self.aprendendo["fg"] = '#f5f6fa'
        self.aprendendo.pack()

        self.eigenfaces = Button(self.quartoContainer)
        self.eigenfaces["text"] = "EigenFaces"
        self.eigenfaces["font"] = ("Calibri", "8")
        self.eigenfaces["width"] = 15
        self.eigenfaces["command"] = self.reconhecerEigen
        self.eigenfaces.pack(side=LEFT)

        self.fisherfaces = Button(self.quartoContainer)
        self.fisherfaces["text"] = "FisherFaces"
        self.fisherfaces["font"] = ("Calibri", "8")
        self.fisherfaces["width"] = 15
        self.fisherfaces["command"] = self.reconhecerFisher
        self.fisherfaces.pack(side=LEFT)

        self.lbph = Button(self.quartoContainer)
        self.lbph["text"] = "Script LBPH"
        self.lbph["font"] = ("Calibri", "8")
        self.lbph["width"] = 15
        self.lbph["command"] = self.reconhecerLBPH
        self.lbph.pack(side=LEFT)

        self.certificado = Label(self.quintoContainer, text="70%                   50%                    30%")
        self.certificado["font"] = ("Arial", "10", "bold")
        self.certificado["bg"] = '#353b48'
        self.certificado["fg"] = '#f5f6fa'
        self.certificado.pack(side=LEFT)

        self.obs = Label(self.sextoContainer, text="Obs: Chance de Erro do Scripts\n 70% Chance de Erro com EigenFaces\n 50% Chance de Erro com FisherFaces\n 30% Chance de Erro com LBPH")
        self.obs["font"] = ("Arial", "7", "italic")
        self.obs["bg"] = '#353b48'
        self.obs["fg"] = '#f5f6fa'
        self.obs.pack(side=LEFT)

    # Método verificar senha
    def capturaImagem(self):
        nome = self.nome.get()
        id = self.id.get()
        if nome != "":
            os.system('cls')
            print("Iniciando a Captura de Imagens")
            captura.Captura(nome, id)
        else:
            os.system('cls')
            print("Falha ao Capturar Imagens Informe o Nome e o ID")
            self.popUp()

    def treinamento(self):
        mensagem = "Iniciando Treinamento"
        treinamento.Treinamento()

    def reconhecerEigen(self):
        reconhecedor_eigenfaces.ReconhecerEigenFaces()

    def reconhecerFisher(self):
        reconhecedor_fisherfaces.ReconhecerFisherFaces()

    def reconhecerLBPH(self):
        reconhecedor_lbph.ReconhecerLBPH()

    def popUp(self):

        semNome = Tk()
        semNome.title("Erro 404 - Nome Não Encontrado")

        frm_width = semNome.winfo_rootx() - semNome.winfo_x()
        win_width = 500 + 2 * frm_width
        win_height = 120 + frm_width
        x = semNome.winfo_screenwidth() // 2 - win_width // 2
        y = semNome.winfo_screenheight() // 2 - win_height // 2

        semNome.geometry('500x120+{}+{}'.format(x, y))
        semNome['bg'] = '#353b48'

        popup.Popup(semNome)
        semNome.mainloop()

root = Tk()
Application(root)
root.mainloop()