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
            # print(caminhos)
            faces = []
            ids = []

            for caminhoImagem in caminhos:
                imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
                nome = os.path.split(caminhoImagem)[-1].split('.')[1]
                print(id)
                nomes.append(id)
                faces.append(imagemFace)

                # cv2.imshow("Face", imagemFace)
                # cv2.waitKey(10)
            return np.array(ids), faces

        ids, faces = getImagemComId()
        # print(faces)

        print("Treinando....")

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO EIGENFACES
        eigenface.train(faces, ids)
        eigenface.write('classificadorEigen.yml')

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO FISHERFACE
        fisherface.train(faces, ids)
        fisherface.write('classificadorFisher.yml')

        # MOMENTO QUE PASSA AS INFORMAÇÕES PARA O TREINAMENTO DO LBPH
        lbph.train(faces, ids)
        lbph.write('classificadorLBPH.yml')

        mensagem = "Treinamento concluido com Sucesso!!!!"
        print(mensagem)
        return mensagem
