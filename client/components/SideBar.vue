<template>
  <section>
    <b-sidebar
      :fullheight="fullheight"
      :fullwidth="fullwidth"
      :overlay="overlay"
      :right="right"
      :open.sync="open"
      type="is-light"
    >
      <div class="p-1">
        <p class="title is-5">Huidig adres</p>
        <p class="subtitle is-6">{{ current_address }}</p>
      </div>

      <div class="p-1">
        <div class="field">
          <b-switch v-model="onlyActiveJobsFilter">{{
            'Aleen actieve jobs'
          }}</b-switch>
        </div>
      </div>

      <div class="p-1">
        <div
          v-for="job in orderedJobs"
          :key="job.id"
          @click="goTo(job)"
          class="m-t-sm card"
        >
          <div class="card-content">
            <div class="media">
              <div class="media-content">
                <p class="title is-4">{{ job.name }}</p>
                <p class="subtitle is-6">{{ job.address }}</p>
              </div>
            </div>
            <div class="content">
              <span></span>
              <span></span>
              <span>{{ job.order_number }}</span>
            </div>
          </div>
        </div>
      </div>
    </b-sidebar>
  </section>
</template>

<script>
import { mapState } from 'vuex'
import { LocationMixin } from '@/mixins/locationMixin'

export default {
  name: 'SideBar',
  mixins: [LocationMixin],
  data() {
    return {
      overlay: true,
      fullheight: true,
      fullwidth: false,
      right: false,
      open: false,
      onlyActiveJobsFilter: false
    }
  },
  computed: {
    ...mapState(['jobs']),
    orderedJobs() {
      let j = this.jobs
      if (process.client && this.onlyActiveJobsFilter) {
        const activeJobs = JSON.parse(
          localStorage.getItem('activeJobs') || '[]'
        )
        j = j.filter(
          (e) =>
            activeJobs.findIndex((ac) => ac.order_number === e.order_number) >=
            0
        )
      }
      return [...j].sort(({ location: locationA }, { location: locationB }) => {
        if (this.location) {
          const [latA, lonA] = locationA.split(',')
          const [latB, lonB] = locationB.split(',')
          const [currLat, currLon] = this.location
          return (
            this.distanceBetween(currLat, currLon, latA, lonA) -
            this.distanceBetween(currLat, currLon, latB, lonB)
          )
        } else {
          return false
        }
      })
    }
  },
  methods: {
    toggle() {
      this.open = !this.open
    },
    goTo(job) {
      this.$router.push(
        { name: 'job-id', params: { id: job.id } },
        this.toggle.bind(this),
        this.toggle.bind(this)
      )
    }
  }
}
</script>

<style scoped>
.p-1 {
  padding: 1em;
}
</style>
