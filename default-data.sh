#!/bin/bash

set -e

SAWTOOTH_HOST=localhost:8000
BIRD_CERT=birdfriendly-cca-2016-2019
ECO_CERT=ecocert-pe-2017-95151

CAC_FARM=cac-la-florida
CAC_HARVEST=cca-laflordia-2017Q3
CAC_SHIPMENT=ship-peru-hkg-nykli710-486645

MANLAO_FARM=manlao-river-coffee-naji
MANLAO_HARVEST=manlao-naji-2017Q4

ROAST_KEY=SH-20180507

http --check-status post ${SAWTOOTH_HOST}/api/codes/mint/ << EOFJSON
{
    "messages": [
        "AABABEB40C0418MPP0518DA2403989B",
        "343589B6140418MPP05183A64577813"
    ],
    "created_at": "2018-04-23T10:10:00Z",
    "company": 277
}
EOFJSON
sleep 1

http --check-status post ${SAWTOOTH_HOST}/api/codes/activate/ << EOFJSON
{
    "messages": [
        "AABABEB40C0418MPP0518DA2403989B",
        "343589B6140418MPP05183A64577813"
    ],
    "activated_at": "2018-05-11T04:04:00Z"
}
EOFJSON
sleep 1

http --check-status -v post ${SAWTOOTH_HOST}/api/certs/create/ << EOFJSON
{
	"key": "${ECO_CERT}",
	"name": "EcoCert (CAC La Florida)",
	"certifier_url": "http://certificat.ecocert.com/client.php?source=recherche&id=5E135A81-FA52-4260-B57B-2E18A3A49EF2",
	"url": "https://i.imgur.com/1Va2hAL.jpg",
	"valid_from": "2017-06-16",
	"valid_to": "2018-03-16",
	"file": {
		"url": "http://dl.scantrust.com.s3-website-eu-west-1.amazonaws.com/blockchain/assets/cambio/Eco%20Cert%20PE-2017-95151-Z-62066-2017.pdf",
		"name": "EcoCert, Jun 2017 - Mar 2018"
	},
	"instructions": "Please visit ecocert.com to further validate the attached certificate."
}
EOFJSON
sleep 1


http --check-status -v post ${SAWTOOTH_HOST}/api/certs/create/ << EOFJSON
{
	"key": "${BIRD_CERT}",
	"name": "Bird Friendly Certification",
	"certifier_url": "https://nationalzoo.si.edu/migratory-birds/certified-coffee-farms",
	"valid_from": "2017-11-10",
	"valid_to": "2019-11-09",
	"file": {
		"url": "http://dl.scantrust.com.s3-website-eu-west-1.amazonaws.com/blockchain/assets/cambio/Bird%20Friendly%20Certificate%20CAC%20La%20Florida.pdf",
		"name": "Bird Friendly Certification, Nov 2016 - Nov 2019"
	},
	"instructions": "Please visit nationalzoo.si.edu to further validate the attached certificate."
}
EOFJSON
sleep 1


http --check-status -v post ${SAWTOOTH_HOST}/api/farms/create/ << EOFJSON
{
	"key": "${CAC_FARM}",
	"name": "Cooperativa Agraria Cafetalera La Florida",
	"location": {
		"lat": -11.064929,
		"lng": -75.33724,
		"description": "Av. Perú 430, La Merced, Peru"
	},
	"address": [
		"Av. Perú N 430 - 432",
		"Pampa del Carmen",
		"Chanchamayo Chanchamayo, Peru"
	],
	"certifications": [
		"${ECO_CERT}",
		"${BIRD_CERT}"
	]
}
EOFJSON
sleep 1


http --check-status -v post ${SAWTOOTH_HOST}/api/farms/create/ << EOFJSON
{
	"key": "${MANLAO_FARM}",
	"name": "ManLao River Coffee (Naji)",
	"location": {
		"lat": 24.5386,
		"lng": 104.284,
		"description": "NaJi, Yunnan (云南省)"
	},
	"address": [
		"云南省纳吉口子"
	],
	"certifications": [
	]
}
EOFJSON
sleep 1



# harvest for la-florida
http --check-status -v post ${SAWTOOTH_HOST}/api/harvests/create/ << EOFJSON
{
	"key": "${CAC_HARVEST}",
	"country": "Peru",
	"year": 2017,
	"month": 8,
	"location": {
		"lat": -11.064929,
		"lng": -75.33724,
		"description": "Av. Perú 430, La Merced, Peru"
	},
	"farms": [
		"${CAC_FARM}"
	],
	"shipments": [
	]
}
EOFJSON
sleep 1

# harvest for ManLao
http --check-status -v post ${SAWTOOTH_HOST}/api/harvests/create/ << EOFJSON
{
	"key": "${MANLAO_HARVEST}",
	"country": "China",
	"year": 2017,
	"month": 12,
	"location": {
		"lat": 24.5386,
		"lng": 104.284,
		"description": "NaJi, Yunnan (云南省)"
	},
	"farms": [
		"${MANLAO_FARM}"
	],
	"shipments": [
	]
}
EOFJSON
sleep 1


http --check-status -v post ${SAWTOOTH_HOST}/api/shipments/create/ << EOFJSON
{
	"key": "${CAC_SHIPMENT}",
	"ship_name": "NYK LIBRA 710",
	"kg": 886,
	"source": {
		"lat": -12.053358,
		"lng": -77.144120,
		"description": "Callao, Peru"
	},
	"destination": {
		"lat": 22.333619,
		"lng": 114.127875,
		"description": "Hong Kong, China"
	},
	"shipped_at":  "2017-10-15",
	"recieved_at": "2017-11-30",
	"extra_info":[
		"Shanghai Customs: 118000002274937001"
	]
}
EOFJSON
sleep 1

http --check-status -v post ${SAWTOOTH_HOST}/api/harvests/${CAC_HARVEST}/add-shipment/ key=${CAC_SHIPMENT}

http --check-status -v post ${SAWTOOTH_HOST}/api/roasts/create/ << EOFJSON
{
	"key": "${ROAST_KEY}",
	"roasted_at": "2018-06-03T19:35:00Z",
	"location": {
		"lat": 31.229788,
		"lng": 121.450201,
		"description": "Shanghai, China"
	},
	"harvests": [
		"${MANLAO_HARVEST}",
		"${CAC_HARVEST}"
	]
}
EOFJSON
sleep 2

http -v get ${SAWTOOTH_HOST}/api/roasts/${ROAST_KEY}/