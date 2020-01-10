FROM python:3.6

ADD mail_sender.py /

# RUN pip install pystrich

CMD [ "python3", "./mail_sender.py" ]