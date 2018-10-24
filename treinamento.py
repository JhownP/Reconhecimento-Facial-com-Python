import cv2
import os
import numpy as np

class Treinamento:

    def __init__(self, mensagem):
        print(mensagem)

        eigenface = cv2.face.EigenFaceRecognizer_create()
        fisherface = cv2.face.FisherFaceRecognizer_create()
        lbph = cv2.face.LBPHFaceRecognizer_create()

        def getImagemComId():
            caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
            faces = []
            nomes = []

            for caminhoImagem in caminhos:
                imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
                nome = int(os.path.split(caminhoImagem)[-1].split('.')[1])
                nomes.append(nome)
                faces.append(imagemFace)

                # cv2.imshow("Face", imagemFace)
                # cv2.waitKey(10)
            return np.array(nomes), faces

        nomes, faces = getImagemComId()
        # print(faces)

        print("Treinando....")

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO EIGENFACES
        eigenface.train(faces, nomes)
        eigenface.write('classificadorEigen.yml')

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO FISHERFACE
        fisherface.train(faces, nomes)
        fisherface.write('classificadorFisher.yml')

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO LBPH
        lbph.train(faces, nomes)
        lbph.write('classificadorLBPH.yml')

        mensagem = "Treinamento concluido com Sucesso!!!!"
        print(mensagem)
        return mensagem
