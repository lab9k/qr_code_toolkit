$(document).ready(function () {
  MapApp.init();
});

const MapApp = {
  init() {
    this.initMap().then(map => this.fetchItems().then(items => this.addMarkers(map, items)));
  },
  initMap() {
    return new Promise((resolve) => {
      const map = L.map('map').setView([51.034809, 3.729268], 13);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);
      resolve(map);
    });
  },
  fetchItems() {
    return fetch('/api/item').then(res => res.json())
  },
  addMarkers(map, items) {
    items.forEach(item => {
      const pos = item.location.split(",").map(el => parseFloat(el));
      const marker = L.marker(pos).addTo(map);

      const lastUpdate = moment(item.last_update);

      marker.bindPopup(`<p><b>Naam:</b> ${item.name}</p>
                        <p><b>Laatste update:</b> ${lastUpdate.format('LL')}</p>`);
      return marker;
    });
  }
};