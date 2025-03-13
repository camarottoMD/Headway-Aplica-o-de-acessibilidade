import cv2
import mediapipe as mp
import numpy as np
import pyautogui 

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
mp_drawing_styles = mp.solutions.drawing_styles

camera = cv2.VideoCapture(0)

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

calibrated = False
calibration_points = []
screen_points = []

winName = 'Janela de Teste para o SOPT'
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
janela_largura, janela_altura = pyautogui.size() 

pontos_janela = [
        (int(janela_largura * 0.1), int(janela_altura * 0.1)),
        (int(janela_largura * 0.9), int(janela_altura * 0.1)),
        (int(janela_largura * 0.9), int(janela_altura * 0.9)),
        (int(janela_largura * 0.1), int(janela_altura * 0.9)),
        (int(janela_largura * 0.5), int(janela_altura * 0.5))
    ]

pontos_olho = []

while True:
        sucesso, imagem = camera.read()
        if not sucesso:
                break

        imagem = cv2.resize(imagem, (janela_largura, janela_altura))

        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        resultados = face_mesh.process(imagem_rgb)

        imagem_calibracao = imagem.copy()
        cv2.circle(imagem_calibracao, pontos_janela[0], 10, (0, 0, 255), -1)
        cv2.putText(imagem_calibracao, f"Olhe para o ponto 1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow(winName, imagem_calibracao)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            if resultados.multi_face_landmarks:
                pontos_olho.append([x_iris_d, y_iris_d])
                pontos_olho.append([x_iris_e, y_iris_e])
                    
            cv2.destroyAllWindows()
            break

        if resultados.multi_face_landmarks:
                face_landmarks = resultados.multi_face_landmarks[0]

                indices_iris_direita = [473, 474, 475, 476, 477]
                x_iris_d = sum(face_landmarks.landmark[ind].x for ind in indices_iris_direita) / len(indices_iris_direita)
                y_iris_d = sum(face_landmarks.landmark[ind].y for ind in indices_iris_direita) / len(indices_iris_direita)

                indices_iris_esquerda = [468, 469, 470, 471, 472]
                x_iris_e = sum(face_landmarks.landmark[ind].x for ind in indices_iris_esquerda) / len(indices_iris_esquerda)
                y_iris_e = sum(face_landmarks.landmark[ind].y for ind in indices_iris_esquerda) / len(indices_iris_esquerda)

                x_draw_d = int(x_iris_d * janela_largura)
                y_draw_d = int(y_iris_d * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_d, y_draw_d), 5, (0, 255, 0), -1)
                coordenadaPontoDireita1 = x_draw_d, y_draw_d
                
                
                x_draw_e= int(x_iris_e * janela_largura)
                y_draw_e = int(y_iris_e * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_e, y_draw_e), 5, (0, 255, 0), -1)
                coordenadasPontoEsquerda1 = x_draw_e, y_draw_e

        print(f"Ponto 1 capturado.")


cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
        sucesso, imagem = camera.read()
        if not sucesso:
                break

        imagem = cv2.resize(imagem, (janela_largura, janela_altura))

        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        resultados = face_mesh.process(imagem_rgb)

        imagem_calibracao = imagem.copy()
        cv2.circle(imagem_calibracao, pontos_janela[1], 10, (0, 0, 255), -1)
        cv2.putText(imagem_calibracao, f"Olhe para o ponto 2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow(winName, imagem_calibracao)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            if resultados.multi_face_landmarks:
                pontos_olho.append([x_iris_d, y_iris_d])
                pontos_olho.append([x_iris_e, y_iris_e])
                    
            cv2.destroyAllWindows()
            break

        if resultados.multi_face_landmarks:
                face_landmarks = resultados.multi_face_landmarks[0]

                indices_iris_direita = [473, 474, 475, 476, 477]
                x_iris_d = sum(face_landmarks.landmark[ind].x for ind in indices_iris_direita) / len(indices_iris_direita)
                y_iris_d = sum(face_landmarks.landmark[ind].y for ind in indices_iris_direita) / len(indices_iris_direita)

                indices_iris_esquerda = [468, 469, 470, 471, 472]
                x_iris_e = sum(face_landmarks.landmark[ind].x for ind in indices_iris_esquerda) / len(indices_iris_esquerda)
                y_iris_e = sum(face_landmarks.landmark[ind].y for ind in indices_iris_esquerda) / len(indices_iris_esquerda)

                x_draw_d = int(x_iris_d * janela_largura)
                y_draw_d = int(y_iris_d * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_d, y_draw_d), 5, (0, 255, 0), -1)
                coordenadaPontoDireita2 = x_draw_d, y_draw_d
                
                
                x_draw_e= int(x_iris_e * janela_largura)
                y_draw_e = int(y_iris_e * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_e, y_draw_e), 5, (0, 255, 0), -1)
                coordenadasPontoEsquerda2 = x_draw_e, y_draw_e        
        print(f"Ponto 2 capturado.")


cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
while True:
        sucesso, imagem = camera.read()
        if not sucesso:
                break

        imagem = cv2.resize(imagem, (janela_largura, janela_altura))

        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        resultados = face_mesh.process(imagem_rgb)

        imagem_calibracao = imagem.copy()
        cv2.circle(imagem_calibracao, pontos_janela[2], 10, (0, 0, 255), -1)
        cv2.putText(imagem_calibracao, f"Olhe para o ponto 3", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow(winName, imagem_calibracao)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            if resultados.multi_face_landmarks:
                pontos_olho.append([x_iris_d, y_iris_d])
                pontos_olho.append([x_iris_e, y_iris_e])
                    
            cv2.destroyAllWindows()
            break

        if resultados.multi_face_landmarks:
                face_landmarks = resultados.multi_face_landmarks[0]

                indices_iris_direita = [473, 474, 475, 476, 477]
                x_iris_d = sum(face_landmarks.landmark[ind].x for ind in indices_iris_direita) / len(indices_iris_direita)
                y_iris_d = sum(face_landmarks.landmark[ind].y for ind in indices_iris_direita) / len(indices_iris_direita)

                indices_iris_esquerda = [468, 469, 470, 471, 472]
                x_iris_e = sum(face_landmarks.landmark[ind].x for ind in indices_iris_esquerda) / len(indices_iris_esquerda)
                y_iris_e = sum(face_landmarks.landmark[ind].y for ind in indices_iris_esquerda) / len(indices_iris_esquerda)

                x_draw_d = int(x_iris_d * janela_largura)
                y_draw_d = int(y_iris_d * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_d, y_draw_d), 5, (0, 255, 0), -1)
                coordenadaPontoDireita3 = x_draw_d, y_draw_d
                
                
                x_draw_e= int(x_iris_e * janela_largura)
                y_draw_e = int(y_iris_e * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_e, y_draw_e), 5, (0, 255, 0), -1)
                coordenadasPontoEsquerda3 = x_draw_e, y_draw_e

        print(f"Ponto 3 capturado.")

        
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
while True:
        sucesso, imagem = camera.read()
        if not sucesso:
                break

        imagem = cv2.resize(imagem, (janela_largura, janela_altura))

        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        resultados = face_mesh.process(imagem_rgb)

        imagem_calibracao = imagem.copy()
        cv2.circle(imagem_calibracao, pontos_janela[3], 10, (0, 0, 255), -1)
        cv2.putText(imagem_calibracao, f"Olhe para o ponto 4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow(winName, imagem_calibracao)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            if resultados.multi_face_landmarks:
                pontos_olho.append([x_iris_d, y_iris_d])
                pontos_olho.append([x_iris_e, y_iris_e])
                    
            cv2.destroyAllWindows()
            break

        if resultados.multi_face_landmarks:
                face_landmarks = resultados.multi_face_landmarks[0]

                indices_iris_direita = [473, 474, 475, 476, 477]
                x_iris_d = sum(face_landmarks.landmark[ind].x for ind in indices_iris_direita) / len(indices_iris_direita)
                y_iris_d = sum(face_landmarks.landmark[ind].y for ind in indices_iris_direita) / len(indices_iris_direita)

                indices_iris_esquerda = [468, 469, 470, 471, 472]
                x_iris_e = sum(face_landmarks.landmark[ind].x for ind in indices_iris_esquerda) / len(indices_iris_esquerda)
                y_iris_e = sum(face_landmarks.landmark[ind].y for ind in indices_iris_esquerda) / len(indices_iris_esquerda)

                x_draw_d = int(x_iris_d * janela_largura)
                y_draw_d = int(y_iris_d * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_d, y_draw_d), 5, (0, 255, 0), -1)
                coordenadaPontoDireita4 = x_draw_d, y_draw_d
                
                
                x_draw_e= int(x_iris_e * janela_largura)
                y_draw_e = int(y_iris_e * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_e, y_draw_e), 5, (0, 255, 0), -1)
                coordenadasPontoEsquerda4 = x_draw_e, y_draw_e
        print(f"Ponto 4 capturado.")


cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
while True:
        sucesso, imagem = camera.read()
        if not sucesso:
                break

        imagem = cv2.resize(imagem, (janela_largura, janela_altura))

        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        resultados = face_mesh.process(imagem_rgb)

        imagem_calibracao = imagem.copy()
        cv2.circle(imagem_calibracao, pontos_janela[4], 10, (0, 0, 255), -1)
        cv2.putText(imagem_calibracao, f"Olhe para o ponto 5", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow(winName, imagem_calibracao)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            if resultados.multi_face_landmarks:
                pontos_olho.append([x_iris_d, y_iris_d])
                pontos_olho.append([x_iris_e, y_iris_e])
                    
            cv2.destroyAllWindows()
            break

        if resultados.multi_face_landmarks:
                face_landmarks = resultados.multi_face_landmarks[0]

                indices_iris_direita = [473, 474, 475, 476, 477]
                x_iris_d = sum(face_landmarks.landmark[ind].x for ind in indices_iris_direita) / len(indices_iris_direita)
                y_iris_d = sum(face_landmarks.landmark[ind].y for ind in indices_iris_direita) / len(indices_iris_direita)

                indices_iris_esquerda = [468, 469, 470, 471, 472]
                x_iris_e = sum(face_landmarks.landmark[ind].x for ind in indices_iris_esquerda) / len(indices_iris_esquerda)
                y_iris_e = sum(face_landmarks.landmark[ind].y for ind in indices_iris_esquerda) / len(indices_iris_esquerda)

                x_draw_d = int(x_iris_d * janela_largura)
                y_draw_d = int(y_iris_d * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_d, y_draw_d), 5, (0, 255, 0), -1)
                coordenadaPontoDireita5 = x_draw_d, y_draw_d
                
                
                x_draw_e= int(x_iris_e * janela_largura)
                y_draw_e = int(y_iris_e * janela_altura)
                cv2.circle(imagem_calibracao, (x_draw_e, y_draw_e), 5, (0, 255, 0), -1)
                coordenadasPontoEsquerda5 = x_draw_e, y_draw_e
        print(f"Ponto 5 capturado.")


while True:
    sucesso, imagem = camera.read()
    if not sucesso:
        break

    imagem = cv2.resize(imagem, (janela_largura, janela_altura))

    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    resultados = face_mesh.process(imagem_rgb)

    if resultados.multi_face_landmarks:
        face_landmarks = resultados.multi_face_landmarks[0]

        indices_iris_direita = [473, 474, 475, 476, 477]
        x_iris_d = sum(face_landmarks.landmark[ind].x for ind in indices_iris_direita) / len(indices_iris_direita)
        y_iris_d = sum(face_landmarks.landmark[ind].y for ind in indices_iris_direita) / len(indices_iris_direita)

        indices_iris_esquerda = [468, 469, 470, 471, 472]
        x_iris_e = sum(face_landmarks.landmark[ind].x for ind in indices_iris_esquerda) / len(indices_iris_esquerda)
        y_iris_e = sum(face_landmarks.landmark[ind].y for ind in indices_iris_esquerda) / len(indices_iris_esquerda)

        x_draw_d = int(x_iris_d * janela_largura)
        y_draw_d = int(y_iris_d * janela_altura)
        cv2.circle(imagem, (x_draw_d, y_draw_d), 5, (0, 255, 0), -1)
        coordenadasDireitaAtuais = x_draw_d, y_draw_d
        
        x_draw_e = int(x_iris_e * janela_largura)
        y_draw_e = int(y_iris_e * janela_altura)
        cv2.circle(imagem, (x_draw_e, y_draw_e), 5, (0, 255, 0), -1)
        coordenadasEsquerdaAtuais = x_draw_e, y_draw_e


        if np.allclose(coordenadasDireitaAtuais, coordenadaPontoDireita1, atol=5):
          print(pontos_janela[0])
          pyautogui.moveTo(pontos_janela[0])
          print("Calibração concluída com sucesso.")
        elif np.allclose(coordenadasDireitaAtuais, coordenadaPontoDireita2, atol=5):
          print(pontos_janela[1])
          pyautogui.moveTo(pontos_janela[1])
          print("Calibração concluída com sucesso.")
        elif np.allclose(coordenadasDireitaAtuais, coordenadaPontoDireita3, atol=5):
          print(pontos_janela[2])
          pyautogui.moveTo(pontos_janela[2])
          print("Calibração concluída com sucesso.")
        elif np.allclose(coordenadasDireitaAtuais, coordenadaPontoDireita4, atol=5):
          print(pontos_janela[3])
          pyautogui.moveTo(pontos_janela[3])
          print("Calibração concluída com sucesso.")
        elif np.allclose(coordenadasDireitaAtuais, coordenadaPontoDireita5, atol=5):
          print(pontos_janela[4])
          pyautogui.moveTo(pontos_janela[4])
          print("Calibração concluída com sucesso.")


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
