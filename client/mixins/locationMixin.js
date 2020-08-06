export const LocationMixin = {
  created() {
    if (process.client) {
      this.$watchLocation().then(({ lat, lng }) => {
        this.location = [lat, lng]
      })
    }
  },
  data() {
    return {
      location: null
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
  }
}
