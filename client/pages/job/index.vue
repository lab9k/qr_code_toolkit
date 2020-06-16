<template>
  <div class="container">
    <section>
      <b-field label="Filter">
        <b-input v-model="filterQuery"></b-input>
      </b-field>
    </section>
    <section>
      <div class="columns">
        <div v-for="job in filteredJobs" :key="job.id" class="column is-3">
          <div class="card">
            <div class="card-image">
              <figure class="image is-square">
                <img :src="getQrUrl(job)" alt="Placeholder image" />
              </figure>
            </div>
            <div class="card-content">
              <div class="content">
                <span>{{ job.name }}</span>
              </div>
            </div>
            <footer class="card-footer">
              <!-- <a :href="job.url" target="_blank" class="card-footer-item">
                Api link
              </a>-->
              <nuxt-link :to="`/job/${job.id}`" class="card-footer-item">
                Detail page
              </nuxt-link>
            </footer>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import { mapActions, mapState } from 'vuex'
import { actionTypes } from '../../store/index'

export default {
  data() {
    return {
      filterQuery: ''
    }
  },
  computed: {
    ...mapState(['jobs']),
    filteredJobs() {
      return this.jobs.filter((job) => {
        return (
          job.name.toLowerCase().includes(this.filterQuery.toLowerCase()) ||
          `${job.order_number}`.includes(this.filterQuery.toLowerCase())
        )
      })
    }
  },
  mounted() {
    this[actionTypes.FETCH_ALL_JOBS]()
  },
  methods: {
    getQrUrl(job) {
      if (process.client) {
        const currentURL = window.location.origin
        const joburl = currentURL + `/job/${job.id}`
        return `https://qrcodeservice.herokuapp.com/?query=${joburl}`
      }
      return ''
    },
    shouldBeVisible() {},
    ...mapActions([actionTypes.FETCH_ALL_JOBS])
  }
}
</script>
