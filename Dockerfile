ENV priveleged

EXPOSE 4723/tcp
EXPOSE 4723/udp

VOLUME /dev/bus/usb:/dev/bus/usb

FROM python:3.12.8-bookworm

RUN curl -fsSL https://fnm.vercel.app/install | bash

ENV PATH="/root/.fnm:$PATH"

RUN fnm install --lts

RUN npm install -g appium

RUN appium &

RUN git clone https://github.com/HaiziIzzudin/Everyday-posting-automation.git

WORKDIR /Everyday-posting-automation

RUN pip install -r requirements.txt

CMD ["fastapi", "run"]
