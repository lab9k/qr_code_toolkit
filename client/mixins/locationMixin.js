export const LocationMixin = {
  created() {
    if (process.client) {
      console.log('requesting location')
      this.$watchLocation({ timeout: 5000 })
        .then(({ lat, lng }) => {
          this.location = [lat, lng]
        })
        .catch((message) => {
          this.$buefy.toast.open({
            duration: 5000,
            message: `Er ging iets mis: ${message}`,
            position: 'is-bottom',
            type: 'is-danger'
          })
        })
    }
  },
  data() {
    return {
      location: null,
      current_address: 'even geduld...'
    }
  },
  methods: {
    distanceBetween(latA, lonA, latB, lonB) {
      const R = 6371e3
      const φ1 = (latA * Math.PI) / 180
      const φ2 = (latB * Math.PI) / 180
      const Δφ = ((latB - latA) * Math.PI) / 180
      const Δλ = ((lonB - lonA) * Math.PI) / 180
      const a =
        Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
        Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ / 2) * Math.sin(Δλ / 2)
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
      return R * c
    }
  },
  watch: {
    async location(val) {
      if (!this.location) return 'calculating'
      const url = `https://nominatim.openstreetmap.org/?q=${this.location.join(
        ','
      )}&format=json&limit=1&country=Belgium`

      const [data] = await this.$axios.$get(url)

      this.current_address = data.display_name
    }
  }
}
