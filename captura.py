import cv2
import numpy as np

class Captura:

    def __init__(self, nome, id):

        # DEFININDO VARIAVEIS QUE ESTÃO SENDO USADAS COMO CONSTANTES E TAMBEM COMO LABELS
        classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
        classificadorOlho = cv2.CascadeClassifier("haarcascade-eye.xml")
        camera = cv2.VideoCapture(0)
        amostra = 1
        numeroAmostras = 25
        largura, altura = 220, 220
        print("Capturando as Faces...")

        # REPETINDO A ABERTURA DA CAMERA PARA QUE SEMPRE FIQUE ABERTO
        while (True):
            conectado, imagem = camera.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                             scaleFactor=1.5,
                                                            minSize=(150,150))

            for (x, y, l, a) in facesDetectadas:
                cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
                regiao = imagem[y:y + a, x:x + l]

                # CONVERTE A IMAGEM PARA CINZA E JÁ VAI DETECTANDO OS OLHOS
                regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
                olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

                for (ox, oy, ol, oa) in olhosDetectados:
                    cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

                    if cv2.waitKey(1) & 0xFF == ord('q'):

                        # Linha Ao qual define o valor da Iluminação dos olhos e da face
                        if np.average(imagemCinza) > 110: # VALOR QUE DEFINE A LUMINOSIDADE
                            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                            cv2.imwrite("fotos/" + nome + "." + id + "." + str(amostra) + ".jpg", imagemFace)
                            print("[Foto " + str(amostra) + " Capturada com Sucesso!!]")
                            amostra += 1

            cv2.imshow("Capturando Faces de " + nome + " Com ID " + id, imagem)
            cv2.waitKey(1)
            if (amostra >= numeroAmostras + 1):
                break

        print("Faces capturadas com sucesso!!!")
        camera.release()
        cv2.destroyAllWindows()