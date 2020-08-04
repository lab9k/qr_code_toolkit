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
  }
}
