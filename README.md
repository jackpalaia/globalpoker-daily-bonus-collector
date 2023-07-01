# About 
This is an automation script that automatically collects the daily bonus from globalpoker.com. The script runs on an AWS EC2 instance, and runs once per day at 9am EST. The script uses Selenium to automate the whole navigation and sign in process.

# Usage
## Linux/WSL2

1. Install Google Chrome: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps#install-google-chrome-for-linux

2. Install Chromdriver

Find the correct version of Chromdriver that supports the version of Chrome you just downloaded, via this page: https://chromedriver.chromium.org/downloads. Then install it with
```
wget https://chromedriver.storage.googleapis.com/{YOUR_CORRECT_VERSION_HERE, something like 114.0.5735.90}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

3. Set up an AWS EC2 instance. Create a new one or use one your already have running. This was tested on an Ubuntu instance so try to go with that. Make sure to stay within the free tier if you're not trying to spend any money. Make sure to save the .pem file so that you can SSH into the machine and transfer files over to it using SCP.

4. Clone this repo

```
git clone git@github.com:jackpalaia/globalpoker-daily-bonus-collector.git
cd globalpoker-daily-bonus-collector
```

5. Copy the .pem file from the EC2 instance into the `globalpoker-daily-bonus-collector` directory.

6. Transfer files over to the EC2 instance

```
scp -i key-pair.pem main.py driver.py scheduler.py utils.py requirements.txt ubuntu@{EC2_ADDRESS}:~/.
```

7. SSH into the EC2 instance

```
ssh -i key-pair.pem ubuntu@{EC2_ADDRESS}
```

8. Create a `.env` file with variables "GOOGLE_EMAIL" and "GOOGLE_PASSWORD" with the values of the Google account that you would like to sign into globalpoker with.

9. Install Python and all required packages

```
sudo apt update
sudo apt install python3-pip
pip install -r requirements.txt
```

10. Run `main.py` in the background using `nohup`

```
nohup python3 main.py &
```

And that's it!
