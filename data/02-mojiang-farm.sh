#!/bin/bash
set -e

source vars.sh 

MOJIANG_ECOCERT=mojiang-ecocert-2018
MOJIANG_FARM=mojiang-coop
MOJIANG_HARVEST=mojiang-2017

http --check-status -v post ${SAWTOOTH_HOST}/api/certs/create/ << EOFJSON
{
	"key": "${MOJIANG_ECOCERT}",
	"name": "EcoCert (Mo Jiang - 2018/19)",
	"certifier_url": "http://certificat.ecocert.com/client.php?source=recherche&id=1813C8AE-06FF-4B04-8C4B-2A886CF2D4B4",
	"url": "",
	"valid_from": "2018-02-02",
	"valid_to": "2019-03-31",
	"file": {
		"url": "http://dl.scantrust.com.s3-website-eu-west-1.amazonaws.com/blockchain/assets/cambio/ecocert-2018-feb-2019-mar.pdf",
		"name": "EcoCert, Feb 2018 - Mar 2019"
	},
	"instructions": "Please visit ecocert.com to further validate the attached certificate."
}
EOFJSON
sleep 1


http --check-status -v post ${SAWTOOTH_HOST}/api/farms/create/ << EOFJSON
{
	"key": "${MOJIANG_FARM}",
	"name": "Mojiang 'Na La Ke' Tropical Agriculture Development Co., LTD.",
	"location": {
		"lat": 23.62441,
		"lng": 101.2844868,
		"description": "Xinfu Town, Yunnan"
	},
	"address": [
		"Xinfuxiang, Mojiang, Pu'er, Yunnan, China",
		"云南省新抚镇界牌村挖落组挖落河"
	],
	"certifications": [
		"${MOJIANG_ECOCERT}"
	]
}
EOFJSON
sleep 1

http --check-status -v post ${SAWTOOTH_HOST}/api/harvests/create/ << EOFJSON
{
	"key": "${MOJIANG_HARVEST}",
	"country": "China",
	"year": 2017,
	"month": 12,
	"location": {
		"lat": 23.62441,
		"lng": 101.2844868,
		"description": "Xinfu Town, Yunnan"
	},
	"farms": [
		"${MOJIANG_FARM}"
	],
	"shipments": [
	]
}
EOFJSON
sleep 1

http --check-status -v post ${SAWTOOTH_HOST}/api/roasts/create/ << EOFJSON
{
	"key": "SH-20180916",
	"roasted_at": "2018-07-03T04:00:00Z",
	"location": {
		"lat": 31.229788,
		"lng": 121.450201,
		"description": "Shanghai, China"
	},
	"harvests": [
		"${MOJIANG_HARVEST}"
	]
}
EOFJSON
sleep 1
