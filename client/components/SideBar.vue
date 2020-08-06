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
        <b-menu>
          <b-menu-list label="Location">
            <b-menu-item
              :label="location ? `${location[0]} , ${location[1]}` : ''"
              icon="world"
            ></b-menu-item>
          </b-menu-list>
        </b-menu>
      </div>

      <div class="p-1">
        <div
          v-for="job in orderedJobs"
          :key="job.id"
          @click="goTo(job)"
          class="m-t-sm card"
        >
          <div class="card-content">
            <div class="content">
              <span>{{ job.name }}</span>
              <span>{{ job.address }}</span>
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
      open: false
    }
  },
  computed: {
    ...mapState(['jobs']),
    orderedJobs() {
      return [...this.jobs].sort(
        ({ location: locationA }, { location: locationB }) => {
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
        }
      )
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
