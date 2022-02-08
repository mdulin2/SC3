FROM python:3
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir /home/admin \
    && mkdir /home/anonymous \
    && echo 'root:root' | chpasswd
COPY key.txt key.txt
COPY notes /root/notes
COPY entrypoint.sh /entrypoint.sh
COPY http_server.py \
    ftp_server.py \
    /
CMD [ "/entrypoint.sh" ]
