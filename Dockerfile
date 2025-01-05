FROM python:3.12.8-bookworm



# install android platform-tools
RUN apt update && apt upgrade -y && apt install wget -y
RUN wget https://github.com/AndroidIDEOfficial/platform-tools/releases/download/v34.0.4/platform-tools-34.0.4-aarch64.tar.xz
RUN tar -xvf platform-tools-34.0.4-aarch64.tar.xz
RUN /platform-tools/adb devices
RUN echo 'export ANDROID_HOME="/platform-tools"' >> ~/.bashrc






# install nodejs & npm
RUN mkdir /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 22.12.0
RUN curl https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH



# install appium via npm
RUN npm install -g appium
RUN appium &


# download and run project
RUN git clone https://github.com/HaiziIzzudin/Everyday-posting-automation.git

WORKDIR /Everyday-posting-automation

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "run"]




# during deployment, please set these:
# --privileged
# -p 8100:8000
# VOLUME /dev/bus/usb:/dev/bus/usb
# VOLUME ~/.android:/root/.android