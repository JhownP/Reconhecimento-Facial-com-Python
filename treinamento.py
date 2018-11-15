import cv2
import os
import numpy as np
from numpy.core.multiarray import ndarray


class Treinamento:

    def __init__(self):

        # Definindo os Reconhecimento em suas variaveis
        eigenface = cv2.face.EigenFaceRecognizer_create()
        fisherface = cv2.face.FisherFaceRecognizer_create()
        lbph = cv2.face.LBPHFaceRecognizer_create()

        ids, faces = Treinamento.getImagemComId(self)
        # print(faces)

        print("Treinando....")

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO EIGENFACES
        print("\n\nIniciando Treinamento EigenFaces")
        eigenface.train(faces, ids)
        eigenface.write('classificadorEigen.yml')
        print(eigenface)

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO FISHERFACE
        print("\n\nIniciando Treinamento FisherFaces")
        fisherface.train(faces, ids)
        fisherface.write('classificadorFisher.yml')
        print(fisherface)

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO LBPH
        print("\n\nIniciando Treinamento LBPH")
        lbph.train(faces, ids)
        lbph.write('classificadorLBPH.yml')
        print(lbph)

        print("\n\nTreinamento concluido com Sucesso!!!!")
        os.system('cls')

    # CLASSE QUE LÊ TODOS OS IDS CADASTRADOS DAS IMAGENS PARA FAZER O TREINAMENTO
    def getImagemComId(self):
        caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
        faces = []
        ids = []

        # FOR DE INTERAÇÃO DE ARRAY DE IMAGENS PEGANDO TODOS OS IDS
        for caminhoImagem in caminhos:
            imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)

            id = int(os.path.split(caminhoImagem)[-1].split('.')[1])

            # print(id)

            ids.append(id)
            faces.append(imagemFace)

            # cv2.imshow("Face", imagemFace)
            # cv2.waitKey(10)
        # ADICIONANDO TODAS AS IMAGENS EM UM ARRAY E JÁ MOSTRANDO AS FACES
        return np.array(ids), faces
