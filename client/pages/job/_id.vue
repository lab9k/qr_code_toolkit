<template>
  <div class="container is-fluid">
    <section>
      <div class="container">
        <b-table :data="isEmpty ? [] : job.current_items" :mobile-cards="true">
          <template slot-scope="props">
            <b-table-column field="id" label="ID" width="40" numeric>
              {{ props.row.id }}
            </b-table-column>

            <b-table-column field="name" label="Name">
              {{ props.row.name }}
            </b-table-column>

            <b-table-column field="last_update" label="Last Update">
              {{ props.row.last_update }}
            </b-table-column>

            <b-table-column field="missing" label="Missing">
              {{ props.row.missing }}
            </b-table-column>

            <b-table-column field="report_missing" label="Missing/Found">
              <b-button @click="reportMissing(props.row)">
                Report {{ props.row.missing ? 'Found' : 'Missing' }}
              </b-button>
            </b-table-column>
          </template>
          <template slot="empty">
            <section class="section">
              <div class="content has-text-grey has-text-centered">
                <p>
                  <b-icon icon="emoticon-sad" size="is-large"> </b-icon>
                </p>
                <p>No items tracked at the moment</p>
              </div>
            </section>
          </template>
        </b-table>
      </div>
    </section>
    <section>
      <div class="container">
        <b-button @click="scanning = !scanning">Scan</b-button>
      </div>
    </section>
    <section v-if="scanning">
      <client-only>
        <scanner @result="addItem" />
      </client-only>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { actionTypes, getterTypes } from '../../store'

export default {
  name: 'JobDetail',
  components: {
    scanner: () => import('@/components/client-only/Scanner')
  },
  data() {
    return {
      scanning: false
    }
  },
  computed: {
    ...mapGetters([getterTypes.JOB_PER_ID]),
    job() {
      return this[getterTypes.JOB_PER_ID](parseInt(this.$route.params.id, 10))
    },
    isEmpty() {
      return this.job ? this.job.current_items.length <= 0 : true
    }
  },
  mounted() {
    this[actionTypes.FETCH_ALL_JOBS]()
  },
  methods: {
    ...mapActions([actionTypes.FETCH_ALL_JOBS, actionTypes.TRACK_ITEM]),
    reportMissing(item) {
      console.log(item)
    },
    addItem(ev) {
      const isAlreadyTrackedInJob = this.job.current_items.find(
        (el) => el.url === ev
      )
      if (!isAlreadyTrackedInJob) {
        const id = ev.substr(ev.length - 2, 1)
        console.log(id)
        this[actionTypes.TRACK_ITEM]({ job: this.job, id }).then((res) =>
          this[actionTypes.FETCH_ALL_JOBS]()
        )
      }
    }
  }
}
</script>

<style scoped></style>
