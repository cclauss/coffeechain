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


# Name of the Cooperative:墨江那拉壳热带农业开发有限公司
# Name of the Farm:那拉壳有机咖啡庄园
# Address of Farm?Location:云南省普洱市墨江县新抚镇界牌村挖落组挖落河
# Harvest date:2017年12月 -2018年3月
# Certificate descriptions:有机销售证明
# Certificates :attached this email
# validity of certificates:2018.02.02-2019.3.31
# web URL where the certificates can be viewed online:www.ecocert.com

# Name of the Cooperative:墨江那拉壳热带农业开发有限公司    
# English: MOJIANG ''NA LA KE'' TROPICAL AGRICULTURE DEVELOPMENT CO., LTD..   
# PinYing:MO JIANG NA LA KE RE DAI NONG YE KAI FA YOU XIAN GONG SI


# Name of the Farm:那拉壳有机咖啡庄园 
# English: ''NA LA KE'' Organic Coffee Farm    
# PinYing: NA LA KE YOU JI KA FEI ZHUANG YUAN 


# Address of Farm?Location: 云南省新抚镇界牌村挖落组挖落河 
# English: XinFu Town, Waluo River, Waluo Team, Jiepai Village - XINFU TOWN - CHINA  
# PinYing: YUN NAN SHENG XIN FU ZHEN JIE PAI CUN WA LUO ZU WA LUO HE 