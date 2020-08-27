<template>
  <div class="container">
    <section>
      <b-tabs v-model="activeTabs" position="is-centered" class="block">
        <b-tab-item label="Handmatig" icon="pencil">
          <section class="p-1">
            <p>
              Hier kan je order nummers invullen om alleen deze orders te zien
              in de zijbalk
            </p>
            <b-field label="Order Nummer">
              <b-input
                v-model="current_input"
                placeholder="Order Nummer"
                type="number"
              >
              </b-input>
            </b-field>
            <b-button @click="submitNumber(current_input)">Submit</b-button>
          </section>
        </b-tab-item>
        <b-tab-item label="Automatisch" icon="video">
          <client-only>
            <scanner
              v-if="activeTabs === 1"
              :registering="true"
              @result="submitNumber"
            />
          </client-only>
        </b-tab-item>
      </b-tabs>
    </section>

    <section class="p-2">
      <h1 class="title">Huidige actieve orders</h1>
      <b-button @click="removeAll">Verwijder alle</b-button>
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
  components: { scanner: () => import('@/components/client-only/Scanner.vue') },
  data() {
    return {
      current_input: 0,
      activeTabs: 0
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
    submitNumber(current_order_number) {
      if (process.client) {
        const currentstr = localStorage.getItem('activeJobs') ?? '[]'
        const current = JSON.parse(currentstr)

        const item = this.jobs.find(
          (el) => el.order_number === parseInt(current_order_number, 10)
        )
        if (!item) {
          this.$buefy.toast.open({
            duration: 5000,
            message: `Deze job is niet gekend!`,
            position: 'is-top',
            type: 'is-danger'
          })
          return
        }

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
