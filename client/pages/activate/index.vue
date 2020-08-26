<template>
  <div class="container">
    <p>
      Hier kan je order nummers invullen om alleen deze orders te zien in de
      zijbalk
    </p>
    <section class="p-1">
      <b-field label="Order Nummer">
        <b-input
          v-model="current_input"
          placeholder="Order Nummer"
          type="number"
        >
        </b-input>
      </b-field>
      <b-button @click="submitNumber">Submit</b-button>
      <b-button @click="removeAll">Verwijder alle</b-button>
    </section>
    <section class="p-2">
      <h1 class="title">Huidige actieve orders</h1>
      <ul>
        <li v-for="number in currentTrackedJobs">
          {{ number.order_number }}: {{ number.name }}
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { actionTypes } from '@/store'
export default {
  data() {
    return {
      current_input: 0
    }
  },
  computed: {
    ...mapState(['jobs']),
    currentTrackedJobs() {
      if (process.client) {
        const items = localStorage.getItem('activeJobs') ?? '[]'

        return JSON.parse(items)
      }
      return []
    }
  },
  mounted() {
    this[actionTypes.FETCH_ALL_JOBS]()
  },
  methods: {
    ...mapActions([actionTypes.FETCH_ALL_JOBS]),
    submitNumber() {
      if (process.client) {
        const currentstr = localStorage.getItem('activeJobs') ?? '[]'
        const current = JSON.parse(currentstr)

        const item = this.jobs.find(
          (el) => el.order_number === parseInt(this.current_input, 10)
        )

        current.push(item)

        localStorage.setItem('activeJobs', JSON.stringify(current))
        this._computedWatchers.currentTrackedJobs.run()
        this.$forceUpdate()
      }
    },
    removeAll() {
      if (process.client) {
        localStorage.removeItem('activeJobs')
        this._computedWatchers.currentTrackedJobs.run()
        this.$forceUpdate()
      }
    }
  }
}
</script>

<style scoped>
.p-2 {
  padding-top: 2rem;
}
.p-1 {
  padding-top: 1rem;
}
</style>
