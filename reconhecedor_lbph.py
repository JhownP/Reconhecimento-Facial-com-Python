import cv2
import os

class ReconhecerLBPH:
    def __init__(self):

        detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
        reconhecedor = cv2.face.LBPHFaceRecognizer_create()
        reconhecedor.read("classificadorLBPH.yml")
        largura, altura = 220, 220
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL

        camera = cv2.VideoCapture(0)

        while (True):
            conectado, imagem = camera.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = detectorFace.detectMultiScale(imagemCinza,
                                                            scaleFactor=1.5,
                                                            minSize=(150,150))

            for (x, y, l, a) in facesDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                cv2.rectangle(imagem, (x,y), (x + l, y + a), (0, 0, 255), 2)
                id, confianca = reconhecedor.predict(imagemFace)

                # Envia o Valor do ID para a função em comparação com Nome
                nome = ReconhecerLBPH.getNome(self, id)

                cv2.putText(imagem, nome, (x,y + (a+30)), font, 2, (0, 0, 255), 2)
                cv2.putText(imagem, str('{:.2f}'.format(confianca)), (x,y + (a+70)), font, 2, (0, 0, 255), 2)

            cv2.imshow("Reconhecimento Facial em LBPH", imagem)
            if cv2.waitKey(1) == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()

    def getNome(self, idPrevisto):
        caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]

        for caminhoImagem in caminhos:
            idAtual = int(os.path.split(caminhoImagem)[1].split(".")[1])

            if (idPrevisto == idAtual):
                nome = os.path.split(caminhoImagem)[-1].split('.')[0]
            else:
                nome = "Nao Localizado"

        return nome