#!/usr/bin/env python3
# coding: utf-8
from threading import Thread

from self import self

from projetoRobo.SA.mensagens_auditor import MsgSStoSA
from projetoRobo.SS.InterfaceGrafica import *
from projetoRobo.SS.PosicionamentoSS import *
from projetoRobo.SS.Switch import *
#from projetoRobo.SS.clienteSR import *
from projetoRobo.SS.ReceptorSA import *
from projetoRobo.SS.ComunicacaoSR import *


teste = True

##a = 1 #Autonomo
#a = 2 #Manual
a = 0

posAtual = PosicionamentoSS(0, 0, 1)
posProx = PosicionamentoSS(0, 0, 1)

# pos1 = [2,2]
# pos2 = [1,1]
# pos3 = [3,3]

estado = True

#lista2 = [pos1, pos2, pos3]
#lista2 = [pos1, pos2]
lista2 = []

@Pyro4.expose
@Pyro4.oneway
class PrincipalSS(threading.Thread):
    def configInicial(self):
        print("Obtendo MAC Address...")
        print("MAC: ",ClienteSR.getEndMAC(self))

        corLED = input("Informe a cor do LED: ")
        print("Cor escolhida: ", ClienteSR.setCorLed(self, corLED))


    def modoJogo(self,mdj):
        if mdj == 1:
            threadSA = Switch('g2')
            threadSA.start()


    def getListaCacas(self):
        global lista2
        if len(lista2) != 0:
            return lista2
        else:
            return 1

    def setListaCacas(self,lista):
        global lista2
        print('Lista set', lista)
        lista2 = lista

    def removeCaca(self, x,y):
        global lista2
        if len(lista2) == 0:
            print("LISTA VAZIA NO SS")
        else:
            self.i = 0
            for n in lista2:
                if (lista2[self.i][0] == x and lista2[self.i][1] == y):
                    #print("Posição a ser removida", lista2[self.i])
                    lista2.pop(self.i)
                    #print("LISTA ATUALIZADA NO SS: ", lista2)
                self.i = self.i + 1

    def validaCaca(self):
        global posAtual
        print("solicitando validação da caça")
        # msg = {"_dir": "ss", "_robo": 'g2'}
        #compartilhados.sw_msg({'_dir': 'ss', '_robo': 'g2','cmd': SS_to_SA.ValidaCaca, 'x': posAtual.getEixoX(), 'y': posAtual.getEixoY()})
        opt = input("Minha caça é válida?\n"
                    "1) Válida\n"
                    "2) Não válida\n"
                    "Opção: ")
        if opt == '1':
            print("Caça validada")
            return True
        else:
            print("Essa caça não é sua")
            return True

    def atualizaPosicaoSS(self, x, y, ori, id):
        global posAtual
        global posProx

        if id == 1:
            posAtual.setEixoX(x)
            posAtual.setEixoY(y)
            posAtual.setOrientacao(ori)
            print("PosAtual:  ", posAtual.paraString())
        else:
            posProx.setEixoX(x)
            posProx.setEixoY(y)
            posProx.setOrientacao(ori)
            print("posProx:  ", posProx.paraString())

    def setEstadoDoJogo(self, estd):
        global estado
        estado = estd

    def getEstadoDoJogo(self):
        global estado
        return estado

    def run(self):
        PrincipalSS.configInicial(self)

    def setModoJogo(self,mdj):
        global a
        a = mdj

if __name__ == '__main__':
    PrincipalSS.modoJogo(self,1)
