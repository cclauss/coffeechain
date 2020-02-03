<template>
  <div class="blockchain flex flex-vertical flex-space-between">

    <div class="flex-1">
      <div v-if="cambioBlockchainData.harvests" class="map-container">
        <l-map :zoom="0" :center="[47.413220, -1.219482]" :bounds="bounds" :options="mapOptions">
          <l-tilelayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"></l-tilelayer>
          <l-poly v-for="(line, index) in farmLines" :key="index" :lat-lngs="line.points"></l-poly>

          <v-polyline-decorator :options="options">
            <l-poly v-for="(line, index) in harvestLines" :key="index" :lat-lngs="line.points"></l-poly>
          </v-polyline-decorator>

          <v-polyline-decorator :options="options">
            <l-poly v-for="(line, index) in roastLines" :key="index" :lat-lngs="line.points"></l-poly>
          </v-polyline-decorator>

          <v-polyline-decorator v-if="userPosition.lat" :options="options">
            <l-poly v-for="(line, index) in scanLines" :key="index" :lat-lngs="line.points"></l-poly>
          </v-polyline-decorator>

          <l-marker v-for="marker in markers" :key="marker.id" :lat-lng="marker.position">
            <l-popup :content="marker.popup" />
          </l-marker>
        </l-map>
      </div>

      <div v-if="cambioBlockchainData.harvests" class="product-journey-ctn">
        <div class="section-title">
          Product Journey Overview
        </div>
        <div class="overview-ctn">
          <div class="overview-section">
            <div class="title">
              Your Scan
            </div>
            <div class="Grid -between text">
              <div class="Cell Grid">
                <div class="Cell">
                  This item has been scanned {{code.scan_count}} times
                </div>
              </div>
              <div class="Cell">{{formatDate()}}</div>
            </div>
          </div>
          <div class="overview-arrow">
            <div class="icon" v-html="icons.arrow"></div>
          </div>

          <div class="overview-section">
            <div class="title">
              Roast
            </div>
            <div class="Grid -between text">
              <div class="Cell Grid">
                <div class="icon" v-html="icons.location"></div>
                {{this.cambioBlockchainData.location.description}}
              </div>
              <div class="Cell">{{formatDate(this.cambioBlockchainData.roasted_at, false)}}</div>
            </div>
          </div>
          <div class="overview-arrow">
            <div class="icon" v-html="icons.arrow"></div>
          </div>

          <div class="overview-section">
            <div class="title">
              Harvest
            </div>
            <div class="Grid -between text">
              <div class="Cell Grid">
                <div class="icon" v-html="icons.location"></div>
                <span :key="`harvest-${index}`" v-for="(harvest, index) in cambioBlockchainData.harvests">
                  {{harvest.country}}
                  <span v-if="index != cambioBlockchainData.harvests.length - 1">& &nbsp;</span>
                </span>
              </div>
            </div>
          </div>

        </div>
      </div>

      <div v-if="cambioBlockchainData.harvests" :key="`harvest-details-${harvestIndex}`" v-for="(harvest, harvestIndex) in this.cambioBlockchainData.harvests" class="harvest-ctn">
        <div class="section-title">
          Harvest Details - {{harvest.country}} - {{harvest.year}}/{{harvest.month}}
        </div>
        <div class="address-ctn text">
          <div class="Cell Grid">
            <div class="icon" v-html="icons.building"></div>
            <div class="Cell">
              {{harvest.location.description}}
            </div>
          </div>
        </div>

        <div :key="`shipment-${shipmentIndex}`" v-for="(shipment, shipmentIndex) in harvest.shipments" class="shipments-ctn">
          <div class="line-title Grid">
            <div class="">Shipments</div>
            <div class="line Cell -fill"></div>
          </div>

          <div class="Grid -between text location">
            <div class="Cell Grid">
              <div class="icon" v-html="icons.location"></div>
              <div>To: {{shipment.destination.description}}</div>
            </div>
            <div class="Cell">{{formatDate(shipment.recieved_at, true)}}</div>
          </div>

          <div class="shipment-infos Grid -middle">
            <div class="Cell icon-column">
              <div class="icon" v-html="icons.dots"></div>
              <div class="icon plane" v-html="icons.plane"></div>
              <div class="icon" v-html="icons.dots"></div>
            </div>
            <div class="Cell infos -fill">
              <div :key="`infos-${infoIndex}`" v-for="(info, infoIndex) in shipment.extra_info" class="text">{{info}}</div>
              <div class="text">Ship Name: {{shipment.ship_name}}</div>
              <div class="text">Package Weight: {{shipment.kg}} kg</div>
            </div>
          </div>

          <div class="Grid -between text location">
            <div class="Cell Grid">
              <div class="icon" v-html="icons.location"></div>
              <div>From: {{shipment.source.description}}</div>
            </div>
            <div class="Cell">{{formatDate(shipment.shipped_at, true)}}</div>
          </div>

        </div>

        <div class="farms-ctn">
          <div class="line-title Grid">
            <div class="">Certified Farms</div>
            <div class="line Cell -fill"></div>
          </div>

          <div :key="`farm-${farmIndex}`" v-for="(farm, farmIndex) in harvest.farms" class="farm">
              <div class="farm-title">
                {{farm.name}}
              </div>
              <div class="farm-address Grid">
                <div class="">
                  <div class="icon" v-html="icons.location"></div>
                </div>
                <div class="Cell -fill text">
                  <div :key="`addressline-${addressIndex}`" v-for="(addressLine, addressIndex) in farm.address" class="">
                    {{addressLine}}
                  </div>
                </div>
              </div>
              <div class="farm-certifications">
                <!-- <div class="Grid">
                  <div class="icon" v-html="icons.certificate"></div>
                  <div class="Cell -fill text">
                    Certifications: Ecocert, jun 2017 - mar 2018...
                  </div>
                  <div class="more-btn">
                    more
                  </div>
                </div> -->
                <div :key="`certificate-${certificateIndex}`" v-for="(certificate, certificateIndex) in farm.certifications" class="certificate Grid">
                  <div class="icon cert-icon" v-html="icons.certificate"></div>
                  <div class="Cell -fill">
                    <div class="Grid link">
                      <a :href="certificate.file.url">{{certificate.name}}</a>
                      <div class="icon -middle" v-html="icons.pdf"></div>
                    </div>
                    <div class="">
                      <div class="text">
                        Valid from {{formatDate(certificate.date_from, true)}} to {{formatDate(certificate.date_to, true)}}
                      </div>
                      <div class="hash-ctn">
                        MD5 Hash:<br>
                        {{certificate.file.md5_hash}}
                      </div>
                      <div class="Grid link">
                        <a :href="certificate.certifier_url">Certifier Website</a>
                        <div class="icon" v-html="icons.out"></div>
                      </div>
                      <div class="text">
                        {{certificate.instructions}}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
          </div>
        </div>
      </div>
      <!-- <div v-show="blockchainInfos.code" v-for="(val, key) in blockchainInfos.code.metadata.scm_data" class="blockchain-field">
        <div class="label roboto-medium">{{key}}</div>
        <div class="value roboto">{{val}}</div>
      </div> -->
    </div>
    <app-footer></app-footer>
  </div>
</template>

<script>

import Vue2Leaflet from 'vue2-leaflet'
import Vue2LeafletPolylineDecorator from 'vue2-leaflet-polylinedecorator'

import 'leaflet/dist/leaflet.css'

import Footer from '@/components/ui/Footer'
import { mapGetters } from 'vuex'

// hacks for icon pics
import L from 'leaflet'
delete L.Icon.Default.prototype._getIconUrl

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
})
// end hack

export default {
  name: 'blockchain-cambio',
  components: {
    'l-map': Vue2Leaflet.LMap,
    'l-tilelayer': Vue2Leaflet.LTileLayer,
    'l-poly': Vue2Leaflet.LPolyline,
    'l-marker': Vue2Leaflet.LMarker,
    'l-popup': Vue2Leaflet.LPopup,
    'v-polyline-decorator': Vue2LeafletPolylineDecorator,
    'app-footer': Footer
  },
  data () {
    return {
      blob: {},
      options: {
        color: 'red',
        patterns: [
          {offset: '100%', repeat: 0, symbol: L.Symbol.arrowHead({pixelSize: 12, polygon: false, pathOptions: {stroke: true}})}
        ]
      },
      farmLines: [],
      harvestLines: [],
      roastLines: [],
      scanLines: [],
      markers: [],
      purchasing: false,
      line: {
        points: []
      },
      mapOptions: {
        zoomControl: false,
        dragging: true,
        scrollWheelZoom: true
      },
      // eslint-disable-next-line
      bounds: new L.latLngBounds(),
      icons: {
        arrow: require('@/assets/icons/arrow.svg'),
        building: require('@/assets/icons/building.svg'),
        certificate: require('@/assets/icons/certificate.svg'),
        dots: require('@/assets/icons/vertical-dots.svg'),
        location: require('@/assets/icons/location.svg'),
        out: require('@/assets/icons/out-link.svg'),
        pdf: require('@/assets/icons/pdf.svg'),
        plane: require('@/assets/icons/plane.svg')
      },
      positionInterval: {}
    }
  },
  computed: {
    ...mapGetters(['getSmartLabelTab', 'code', 'cambioBlockchainData', 'userPosition'])
  },
  methods: {

    formatDate (string, short) {
      let date
      if (!string) {
        date = new Date()
      } else {
        date = new Date(Date.parse(string.replace(/-/g, '/').replace(/[a-z]+/gi, ' ')))
      }
      let minutes = date.getMinutes() <= 9 ? '0' + date.getMinutes() : date.getMinutes()
      let days = date.getDate() <= 9 ? '0' + date.getDate() : date.getDate()
      let months = date.getMonth() + 1 <= 9 ? '0' + (date.getMonth() + 1) : date.getMonth()
      if (short) {
        return `${date.getFullYear()}-${months}-${days}`
      } else {
        return `${date.getFullYear()}-${months}-${days} ${date.getHours()}:${minutes}`
      }
    },

    calcBounds (lines) {
      let array = this.roastLines.concat(this.farmLines.concat(this.harvestLines))

      let boundLine = []
      array.forEach((line) => {
        boundLine = boundLine.concat(line.points)
      })
      // eslint-disable-next-line
      this.bounds = new L.latLngBounds(boundLine)
    },

    buildScanLine () {
      if (this.userPosition && this.userPosition.lat && this.userPosition.lng) {
        let line = {points: []}
        line.points.push({lat: this.cambioBlockchainData.location.lat, lng: this.cambioBlockchainData.location.lng})
        line.points.push({lat: this.userPosition.lat, lng: this.userPosition.lng})
        this.scanLines.push(line)
        this.addMarker({position: {lat: this.userPosition.lat, lng: this.userPosition.lng}, id: 'user', popup: `Your location`})
      }
    },

    buildFarmPolylines (harvest) {
      this.addMarker({position: {lat: harvest.location.lat, lng: harvest.location.lng}, id: harvest.key, popup: `Harvest ${harvest.year}/${harvest.month}`})
      harvest.farms.forEach((farm) => {
        let line = {points: []}
        line.points.push({lat: harvest.location.lat, lng: harvest.location.lng})
        line.points.push({lat: farm.location.lat, lng: farm.location.lng})
        this.farmLines.push(line)
      })
    },

    addMarker (options) {
      this.markers.push(options)
    },

    buildHarvestLines (harvest) {
      let line = {points: []}
      line.points.push({lat: harvest.location.lat, lng: harvest.location.lng})
      if (harvest.shipments.length) {
        line.points.push({lat: harvest.shipments[0].source.lat, lng: harvest.shipments[0].source.lng})
        line.points.push({lat: harvest.shipments[0].destination.lat, lng: harvest.shipments[0].destination.lng})
        this.addMarker({position: {lat: harvest.shipments[0].source.lat, lng: harvest.shipments[0].source.lng}, id: harvest.shipments[0].key + '-source', popup: `Shipment leaves ${harvest.shipments[0].source.description}`})
        this.addMarker({position: {lat: harvest.shipments[0].destination.lat, lng: harvest.shipments[0].destination.lng}, id: harvest.shipments[0].key + '-destination', popup: `Shipment arrives in ${harvest.shipments[0].destination.description}`})
      }
      this.harvestLines.push(line)
    },

    buildRoastLines (roast) {
      roast.harvests.forEach((harvest) => {
        let line = {points: []}
        if (harvest.shipments.length) {
          line.points.push({lat: harvest.shipments[0].destination.lat, lng: harvest.shipments[0].destination.lng})
          line.points.push({lat: roast.location.lat, lng: roast.location.lng})
        } else {
          line.points.push({lat: harvest.location.lat, lng: harvest.location.lng})
          line.points.push({lat: roast.location.lat, lng: roast.location.lng})
        }

        this.roastLines.push(line)
      })
      this.addMarker({position: {lat: roast.location.lat, lng: roast.location.lng}, id: roast.key, popup: `Roasted in ${roast.location.description}`})
    }
  },

  created () {
    // Load data, then build stuff
    // this.buildTraceLine();
    this.cambioBlockchainData.harvests.forEach((harvest) => {
      this.buildFarmPolylines(harvest)
      this.buildHarvestLines(harvest)
    })
    this.buildRoastLines(this.cambioBlockchainData)

    this.positionInterval = setInterval(() => {
      if (this.userPosition && this.userPosition.lat && this.userPosition.lng) {
        clearInterval(this.positionInterval)
        this.buildScanLine()
        this.calcBounds()
      }
    }, 500)
  },

  mounted () {
    setTimeout(() => { window.dispatchEvent(new Event('resize')) }, 250)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.map-container{
  width: 100%;
  height: 200px;
}

.map{
  padding: 5px 0px;
}

.icon{
  width: calc(14px + 1vw);
}

.harvest-ctn{
  margin-top: 15px;
}

.section-title{
  color: #21409a;
  font-size: calc(18px + 1vw);
  background: #f1f1f1;
  padding: 8px 14px;
  font-family: 'Roboto';
}

.overview-ctn{
  padding: 16px 14px 0px 14px;
}

.overview-arrow{
  padding: 8px 0px;
}

.overview-arrow .icon{
  width: calc(8px + 1vw);
  padding-left: 2px;
}

.overview-section .title{
  font-size: calc(11px + 1vw);
  color: black;
  font-family: 'Roboto';
  font-weight: bold;
  padding-bottom: 5px;
}

.address-ctn{
  padding-left: 14px;
  padding-top: 11px;
}

.text{
  font-family: 'Roboto';
  font-size: calc(9px + 1vw);
  color: #444;
}

.icon{
  padding-right: 5px;
}

.line-title{
  font-family: 'Roboto';
  font-weight: bold;
  font-size: calc(13px + 1vw);
  color: black;
  padding-left: 14px;
  padding-bottom: 8px;
  padding-top: 14px;
}

.line-title .line {
  height: 1px;
  background: black;
  position: relative;
  margin-top: 12px;
  margin-left: 5px;
}

.shipments-ctn .location{
  padding: 0px 14px;
}

.shipment-infos{
  padding: 5px 14px;
}

.shipment-infos .infos{
  border: 1px solid #979797;
  border-radius: 4px;
  padding: 5px;
}

.plane{
  padding-top: 5px;
  padding-bottom: 5px;
}

.link a{
  font-family: 'Roboto';
  font-size: calc(12px + 1vw);
  color: #21409a;
  text-decoration: underline;
}

.link .icon{
  margin-left: 7px;
}

.farm-title{
  font-family: 'Roboto';
  padding: 5px;
  margin-left: 16px;
  margin-bottom: 8px;
  font-size: calc(14px + 1vw);
  color: black;
  display: inline-block;
  background: #f4f5fa;
}

.farm-address, .farm-certifications{
  padding-left: 14px;
}

.certificate{
  margin: 15px 0px;
}

.certificate .cert-icon{
  padding-top: 4px;
}

.hash-ctn{
  font-family: monospace;
  background: #f4f4f4;
  padding: 5px 8px;
  margin: 5px 0px;
  font-size: calc(12px + 1vw);
  word-wrap: break-word;
}

.blockchain >>> .icon path{
  fill: #666666;
}

.blockchain >>> .link .icon path{
  fill: #21409a;
}

</style>
