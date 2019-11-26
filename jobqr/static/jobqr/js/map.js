$(document).ready(function () {
  MapApp.init();
});


const commonIconOptions = {
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
};
const ICONS = {
  GREEN: new L.Icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    ...commonIconOptions
  }),
  BLUE: new L.Icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
    ...commonIconOptions
  }),
  RED: new L.Icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    ...commonIconOptions
  }),
  ORANGE: new L.Icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png',
    ...commonIconOptions
  })
};

const MapApp = {
  init() {
    this.map = null;
    this.items = [];
    this.initMap().then(map => this.fetchItems().then(items => this.addMarkers(map, items)));
  },
  initMap() {
    return new Promise((resolve) => {
      const map = L.map('map').setView([51.034809, 3.729268], 13);
      MapApp.map = map;
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);
      resolve(map);
    });
  },
  fetchItems() {
    let url = '/api/device';
    if (window.location.pathname.includes('missing')) {
      url += '/?missing=1'
    }
    console.log('using url' + url);
    return fetch(url).then(res => res.json()).then(items => {
      this.items = items;
      return items;
    })
  },
  addMarkers(map, items, icon = ICONS.BLUE) {
    items.forEach(item => {
      const pos = item.location.split(",").map(el => parseFloat(el));
      if (pos.length === 2) {
        const marker = L.marker(pos, {icon}).addTo(map);

        const lastUpdate = moment(item.last_update);

        const template = `<p><b>Naam:</b> ${item.name}</p>
                        <p><b>Laatste update:</b> ${lastUpdate.format('LL')}</p>`;
        const historyButton = `<p><a href="/device/${item.pk}/history">Go to history</a></p>`;
        marker.bindPopup(template + historyButton);
      }
    });
  }
};


