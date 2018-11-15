from tkinter import *

class Popup:
    
    
    # ESTÁ CLASSE MONTA SOMENTE A TELA DE AVISO SEM INTERAÇÃO ALGUMA
    def __init__(self, error=None):

        self.mensagem = "Campo do Nome ou Id Não foi Preenchido"
        self.mensagemDois = "Preencha Para Capturar Imagens"

        self.primeiroContainerError = Frame(error)
        self.primeiroContainerError["bg"] = '#353b48'
        self.primeiroContainerError["pady"] = 20
        self.primeiroContainerError.pack()

        self.segundoContainerError = Frame(error)
        self.segundoContainerError["bg"] = '#353b48'
        self.segundoContainerError.pack()

        self.titulo = Label(self.primeiroContainerError, text=self.mensagem)
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo["bg"] = '#353b48'
        self.titulo["fg"] = '#f5f6fa'
        self.titulo.pack()

        self.argumento = Label(self.segundoContainerError, text=self.mensagem)
        self.argumento["font"] = ("Arial", "10", "italic")
        self.argumento["bg"] = '#353b48'
        self.argumento["fg"] = '#f5f6fa'
        self.argumento.pack()
