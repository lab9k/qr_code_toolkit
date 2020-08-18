<template>
  <div class="container is-fluid">
    <section>
      <div class="container">
        <div class="py-2">
          <p class="title is-5">{{ job.name }}</p>
          <p class="subtitle is-6">{{ job.address }}</p>
        </div>
      </div>
    </section>
    <section>
      <div class="container">
        <b-table :data="isEmpty ? [] : job.current_items" :mobile-cards="true">
          <template slot-scope="props">
            <b-table-column field="id" label="ID" width="40" numeric>
              {{ props.row.id }}
            </b-table-column>

            <b-table-column field="name" label="Naam">
              {{ props.row.name }}
            </b-table-column>

            <b-table-column field="last_update" label="Laatste Update">
              {{ props.row.last_update }}
            </b-table-column>

            <b-table-column field="missing" label="Vermist">
              {{ props.row.missing ? 'Ja' : 'Nee' }}
            </b-table-column>

            <b-table-column field="report_missing" label="vermist/gevonden">
              <b-button @click="reportMissing(props.row)">
                Report {{ props.row.missing ? 'Gevonden' : 'Vermist' }}
              </b-button>
            </b-table-column>
          </template>
          <template slot="empty">
            <section class="section">
              <div class="content has-text-grey has-text-centered">
                <p>
                  <b-icon icon="emoticon-sad" size="is-large"> </b-icon>
                </p>
                <p>Er zijn geen items gevonden voor deze job.</p>
              </div>
            </section>
          </template>
        </b-table>
      </div>
    </section>
    <section>
      <div class="container">
        <b-button @click="startScanning" class="is-info is-outlined is-medium">
          {{ scanning ? 'Stop Scanning' : 'Scan' }}
        </b-button>
        <b-button @click="addPictures" class="is-info is-outlined is-medium">
          {{ addingPics ? 'Sluit foto menu' : 'Open foto menu' }}
        </b-button>
      </div>
    </section>
    <section v-if="scanning">
      <client-only>
        <scanner @result="addItem" />
      </client-only>
    </section>
    <section v-if="addingPics">
      <div class="container">
        <form @submit="submitPictures">
          <b-field label="Voeg een foto toe">
            <b-input type="file" accept="image/*" name="file"></b-input>
          </b-field>
          <b-field label="Schrijf een beschrijving van de foto">
            <b-input type="text" name="remark"></b-input>
          </b-field>
          <b-field class="is-grouped">
            <div class="control">
              <button class="button is-link">Toevoegen</button>
            </div>
            <div class="control">
              <button class="button is-link is-light">Annuleer</button>
            </div>
          </b-field>
        </form>
        <div class="columns is-multiline is-centered">
          <div
            v-for="image in job.images"
            :key="image.id"
            class="column is-three-quarters-mobile is-two-thirds-tablet is-half-desktop is-one-third-widescreen is-one-quarter-fullhd"
          >
            <div class="card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img :src="image.stored_image" alt="Placeholder image" />
                </figure>
              </div>
              <div class="card-content">
                <div class="content">
                  <p>{{ image.remark }}</p>
                  <time datetime="2016-1-1">{{ image.created_at }}</time>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
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
      scanning: false,
      addingPics: false,
      location: null,
      requestsWithoutLocation: []
    }
  },
  computed: {
    ...mapGetters([getterTypes.JOB_PER_ID]),
    job() {
      return (
        this[getterTypes.JOB_PER_ID](parseInt(this.$route.params.id, 10)) || {
          images: [],
          current_items: [],
          title: ''
        }
      )
    },
    isEmpty() {
      return this.job ? this.job.current_items.length <= 0 : true
    },
    postUrl() {
      const base = this.$axios.defaults.baseURL
      return `${base}/job/${this.$route.params.id}/add-image/`
    }
  },
  watch: {
    location: {
      handler(val, oldVal) {
        if (this.requestsWithoutLocation.length > 0) {
          this.requestsWithoutLocation.forEach(({ job, item }) => {
            this.$buefy.snackbar.open({
              message: `item wijzigen: ${item.name}`,
              type: 'is-warning'
            })
            this[actionTypes.TRACK_ITEM]({
              job,
              item: { ...item, location: val }
            })
          })
          this.requestsWithoutLocation = []
          this[actionTypes.FETCH_ALL_JOBS]()
        }
      },
      immediate: false
    }
  },
  mounted() {
    this[actionTypes.FETCH_ALL_JOBS]()
    this.$watchLocation().then(({ lat, lng }) => {
      this.location = `${lat},${lng}`
    })
  },
  methods: {
    ...mapActions([
      actionTypes.FETCH_ALL_JOBS,
      actionTypes.TRACK_ITEM,
      actionTypes.UPDATE_ITEM
    ]),
    reportMissing(item) {
      const report = { ...item, missing: !item.missing }
      this[actionTypes.UPDATE_ITEM](report)
    },
    addItem(item) {
      if (process.client) {
        console.log('App is confirmed to be in CLIENT mode')

        if (!this.location) {
          this.$buefy.snackbar.open({
            message:
              'Locatie van dit toestel is nog niet gekend. Het item word geupdated wanner de locatie beschikbaar is',
            type: 'is-info'
          })
          this.requestsWithoutLocation.push({
            job: this.job,
            item: { ...item }
          })
          return
        }
        this.$buefy.snackbar.open({
          message: 'Locatie is beschikbaar. Item word nu geupdated',
          type: 'is-info'
        })
        this[actionTypes.TRACK_ITEM]({
          job: this.job,
          item: { ...item, location: this.location }
        }).then((res) => {
          this[actionTypes.FETCH_ALL_JOBS]()
        })
      }
    },
    startScanning() {
      if (this.addingPics) {
        this.addingPics = false
      }
      this.scanning = !this.scanning
    },
    addPictures() {
      if (this.scanning) {
        this.scanning = false
      }
      this.addingPics = !this.addingPics
    },
    async submitPictures(e) {
      e.preventDefault()
      const postData = new FormData()
      console.log(e.target)
      postData.append('file', e.target[0].files[0])
      postData.append('remark', e.target[1].value)
      await this.$axios.post(this.postUrl, postData)
      this[actionTypes.FETCH_ALL_JOBS]()
      return false
    }
  }
}
</script>

<style scoped>
.py-2 {
  padding-bottom: 0.5rem;
  padding-top: 0.5rem;
}
</style>
