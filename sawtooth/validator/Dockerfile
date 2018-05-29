FROM hyperledger/sawtooth-validator:1.0

#the SAWTOOTH_HOME environment variable tells the validator where to store all configuration files and data
#respectively:
#   conf_dir    = SAWTOOTH_HOME/etc/
#   key_dir     = SAWTOOTH_HOME/keys/
#   data_dir    = SAWTOOTH_HOME/data/
#   log_dir     = SAWTOOTH_HOME/logs/
#   policy_dir  = SAWTOOTH_HOME/policy/
ENV SAWTOOTH_HOME configs

RUN mkdir -p ${SAWTOOTH_HOME}/etc/ && \
    mkdir ${SAWTOOTH_HOME}/keys/ && \
    mkdir ${SAWTOOTH_HOME}/data/ && \
    mkdir ${SAWTOOTH_HOME}/logs/ && \
    mkdir ${SAWTOOTH_HOME}/policy

COPY ./*.sh ./
COPY ./*.toml ${SAWTOOTH_HOME}/etc/

RUN chmod +x start_genesis_node.sh
RUN chmod +x start_node.sh
RUN chmod +x keypairtest.sh



RUN \
    # Update repositories
    apt-get update \
    # Install curl
&&  apt-get install -y curl \
    # Download filebeat package
&&  curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.2.4-amd64.deb \
    # Install filebeat
&&  dpkg -i filebeat-6.2.4-amd64.deb \
    # Rename standard filebeat config
&&  mv /etc/filebeat/filebeat.yml /etc/filebeat/filebeat.yml.example
# Copy certificate to certificate dir
COPY ./logstash-beats.crt /etc/pki/tls/certs/
COPY ./filebeat.yml /etc/filebeat/


RUN apt-get install -y nodejs-legacy && \

    apt install -y npm && \
    
    npm install -y zmq-zap && \

    npm install -y zeromq


RUN chmod go-w /etc/filebeat/filebeat.yml
