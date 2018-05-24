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
