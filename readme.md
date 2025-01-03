1. Please follow quickstart guide for installing Appium and UiAutomator2 https://appium.io/docs/en/latest/quickstart/

### How to download and update env for 

1. Connect to your linux local server using Filezilla, using SSH credentials file.
2. Download https://github.com/AndroidIDEOfficial/platform-tools/releases
3. Xfer the file to server using Filezilla.
4. Open your terminal, SSH to your server, and run `tar -xf file.xz`
5. `nano .bashrc`
6. Add this line to your .bashrc file:
```
export ANDROID_HOME="$HOME/appium"
export JAVA_HOME="$HOME/appium/jdk-9.0.4"
```
7. restart shell `bash -s`


# make sure npm has been installed
appium