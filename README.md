# QR 코드
## 디코딩
pyzbar라이브러리를 써서 바코드를 읽어주는 기능을 알려줬다

## 웹브라우저와 연결
webbrowser 라이브러리를 써서 qr코드를 웹캠에 인식했을 떄 웹브라우저로 연결하는 방식을 구현해보았다.

# filebrowser
git없이 나의 코드를 팀원이나 다른 사람에게 공유할 때 사용한다.

## 설치 방법
해당 사이트에 접속 -> 시작하기 -> 설치 -> 윈도우
iwr -useb https://raw.githubusercontent.com/filebrowser/get/master/get.ps1 | iex 
해당 내용 복사후
Powershell에 관리자권한으로 들어가서 설치한다.

## 사용 방법
PowerShell에 들어가서 C:\Users\405\projects\opencv_tutorial 해당 위치에 들어간 후 filebrower를 입력하면 IP주소와 비밀번호를 알려준다
해당 IP주소에 들어가서 ID는 admin을 입력후 해당 비밀번호를 입력하여 사용하면 된다.

# Aruco Maker
Aruco marker는 Rafael Muñoz와 Sergio Garrido가 개발한 정사각형 패턴이며, 로봇비전, 증강현실, 자동화 공정등에 널리 사용되고 있다.

## 캘리브레이션 사진촬영
캘리브레이션 사진촬영을 하여 사진의 보정을 실행한다.

## 거리에 따른 경고 메시지 출력
거리에 따라 가까워지면 경고 메시지를 출력하는 기능을 시행해본다.