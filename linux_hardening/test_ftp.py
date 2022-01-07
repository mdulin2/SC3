from ftplib import FTP

ftp = FTP()
ftp.set_debuglevel(1)
ftp.connect('127.0.0.1', 21)
ftp.login("root", "password")
ftp.cwd("notes")
ftp.retrbinary("RETR note.txt", open("_note.txt", 'wb').write)
