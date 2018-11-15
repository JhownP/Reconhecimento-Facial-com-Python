import cv2
import os
import numpy as np
from numpy.core.multiarray import ndarray


class Treinamento:

    def __init__(self):

        eigenface = cv2.face.EigenFaceRecognizer_create()
        fisherface = cv2.face.FisherFaceRecognizer_create()
        lbph = cv2.face.LBPHFaceRecognizer_create()

        ids, faces = Treinamento.getImagemComId(self)
        # print(faces)

        print("Treinando....")

        print("\n\nIniciando Treinamento EigenFaces")
        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO EIGENFACES
        eigenface.train(faces, ids)
        eigenface.write('classificadorEigen.yml')
        print(eigenface)

        print("\n\nIniciando Treinamento FisherFaces")
        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO FISHERFACE
        fisherface.train(faces, ids)
        fisherface.write('classificadorFisher.yml')
        print(fisherface)

        print("\n\nIniciando Treinamento LBPH")
        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO LBPH
        lbph.train(faces, ids)
        lbph.write('classificadorLBPH.yml')
        print(lbph)

        print("\n\nTreinamento concluido com Sucesso!!!!")
        os.system('cls')
    def getImagemComId(self):
        caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
        faces = []
        ids = []

        for caminhoImagem in caminhos:
            imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)

            id = int(os.path.split(caminhoImagem)[-1].split('.')[1])

            print(caminhoImagem)

            ids.append(id)
            faces.append(imagemFace)

            # cv2.imshow("Face", imagemFace)
            # cv2.waitKey(10)
        return np.array(ids), faces
