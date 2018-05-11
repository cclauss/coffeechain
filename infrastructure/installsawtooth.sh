#! /bin/bash

# Add Sawtooth Repo
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8AA7AF1F1091A5FD
sudo add-apt-repository 'deb http://repo.sawtooth.me/ubuntu/1.0/stable xenial universe'
sudo apt-get update

# Install the sawtooth packages
sudo apt-get install -y sawtooth

# Create key
sudo sawtooth keygen
sudo sawtooth keygen ubuntu

# Create Genesis block
sudo sawset genesis
sudo -u sawtooth sawadm genesis config-genesis.batch

# Create validator keypair
sudo sawadm keygen

# Create validator config file
sudo mv /etc/sawtooth/validator.toml.example /etc/sawtooth/validator.toml

# Set variables for validator config file
FILE_TO_CHANGE=/etc/sawtooth/validator.toml
NETWORK_OLD_VALUE=network:tcp://127.0.0.1:8800
NETWORK_NEW_VALUE=network:tcp://eth0:8800
GET_PRIVATE_IP="hostname --ip-address"
PRIVATE_IP=`eval $GET_PRIVATE_IP`
ENDPOINT_OLD_VALUE='endpoint = "tcp://127.0.0.1:8800"'
EPN1='endpoint = "tcp://'
EPN2=':8800"'
ENDPOINT_NEW_VALUE=${EPN1}${PRIVATE_IP}${EPN2}
PEERS_OLD_VALUE='"tcp://127.0.0.1:8801"'
PEERS_NEW_VALUE='"tcp://172.31.29.97:8800","tcp://172.31.25.33:8800"'



# Set network bind
sudo sed -i "s+${NETWORK_OLD_VALUE}+${NETWORK_NEW_VALUE}+g" $FILE_TO_CHANGE

# Set endpoint
sudo sed -i "s+${ENDPOINT_OLD_VALUE}+${ENDPOINT_NEW_VALUE}+g" $FILE_TO_CHANGE

# Set peers
sudo sed -i "s+${PEERS_OLD_VALUE}+${PEERS_NEW_VALUE}+g" $FILE_TO_CHANGE


# Start Sawtooth services
sudo systemctl restart sawtooth-xo-tp-python.service
sudo systemctl restart sawtooth-intkey-tp-python.service
sudo systemctl restart sawtooth-settings-tp.service
sudo systemctl restart sawtooth-poet-validator-registry-tp.service
sudo systemctl restart sawtooth-rest-api.service
sudo systemctl restart sawtooth-validator.service

# Enable Sawtooth services on startup
sudo systemctl enable  sawtooth-xo-tp-python.service
sudo systemctl enable  sawtooth-intkey-tp-python.service
sudo systemctl enable  sawtooth-settings-tp.service
sudo systemctl enable  sawtooth-poet-validator-registry-tp.service
sudo systemctl enable  sawtooth-rest-api.service
sudo systemctl enable  sawtooth-validator.service

# Install Nginx
sudo apt-get install -y nginx

# Install Nginx
sudo apt-get install -y nginx

# Configure port fowarding on port 80
sudo rm /etc/nginx/sites-enabled/default
sudo touch /etc/nginx/sites-enabled/sawtooth
sudo echo "server {server_name default;
    listen 80;
    location / {
        include proxy_params;
        proxy_pass http://localhost:8008;
    }
}">/etc/nginx/sites-enabled/sawtooth

# Test nginx config
cd /etc/nginx/sites-enabled/
sudo nginx -t

# restart Nginx
sudo nginx -s reload

exit 0
