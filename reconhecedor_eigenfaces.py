# encoding: utf-8
import cv2
import os

class ReconhecerEigenFaces:
    def __init__(self):

        detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
        reconhecedor = cv2.face.EigenFaceRecognizer_create()
        reconhecedor.read("classificadorEigen.yml")
        largura, altura = 220, 220
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL

        camera = cv2.VideoCapture(0)

        # VERIFICADOR DE FACES AONDE IREMOS LISTAR E CHAMAR O MÉTODO DE RECONHECIMENTO DE NOMES
        while (True):
            conectado, imagem = camera.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = detectorFace.detectMultiScale(imagemCinza,
                                                            scaleFactor=1.5,
                                                            minSize=(50,50))

            for (x, y, l, a) in facesDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                cv2.rectangle(imagem, (x,y), (x + l, y + a), (255, 0, 0), 2)
                id, confianca = reconhecedor.predict(imagemFace)

                # Envia o Valor do ID para a função em comparação com Nome
                nome = ReconhecerEigenFaces.getNome(self, id, confianca)

                cv2.putText(imagem, nome, (x, y + (a + 30)), font, 2, (255, 0, 0), 2)
                cv2.putText(imagem, str('{:.2f}'.format(confianca)), (x, y + (a + 70)), font, 2, (255, 0, 0), 2)

            cv2.imshow("Reconhecimento Facial em EigenFaces", imagem)
            if cv2.waitKey(1) == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()

    # MÉTODO QUE INFORMA O NOME RECONHECIDO
    def getNome(self, idPrevisto, confianca):
        caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]

        for caminhoImagem in caminhos:
            idAtual = int(os.path.split(caminhoImagem)[1].split(".")[1])

            if (confianca <= 7000):
                if (idPrevisto == idAtual):
                    nome = os.path.split(caminhoImagem)[-1].split('.')[0]
            else:
                nome = "Nao Localizado"

        return nome