FROM python:3.12.8-bookworm

RUN git clone https://github.com/HaiziIzzudin/Everyday-posting-automation.git

WORKDIR /Everyday-posting-automation

RUN pip install -r requirements.txt

CMD ["fastapi", "run"]