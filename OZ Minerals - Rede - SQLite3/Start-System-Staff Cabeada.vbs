Set shell = CreateObject("WScript.Shell")
shell.CurrentDirectory = "C:\Nova pasta\OZ Minerals - Rede"
shell.Run "cmd /c python manage.py runserver 10.106.20.55:9393", 1, True
