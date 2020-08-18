<template>
  <div class="content">
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">Naam</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">{{ item.name }}</p>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">Job</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">{{ job.name }}</p>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">In Gebruik</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">{{ item.is_in_use }}</p>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">Is Vermist</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">{{ item.missing }}</p>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">Laatste Update</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">
          {{ dateDistanceToNow(item.last_update) }} geleden
        </p>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">Locatie</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">
          <b-button @click="showsMap = !showsMap">
            {{ showsMap ? 'Verberg Map' : 'Toon Map' }}
          </b-button>
        </p>
      </div>
    </div>
    <div v-if="showsMap" class="columns">
      <div class="column is-12">
        <single-point-map :location="item.location" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { formatDistance } from 'date-fns'
import { getterTypes } from '@/store'
import SinglePointMap from './SinglePointMap'
export default {
  name: 'ItemInfoCardContent',
  components: { SinglePointMap },
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      showsMap: false
    }
  },
  computed: {
    ...mapGetters([getterTypes.JOB_PER_ID]),
    job() {
      return this[getterTypes.JOB_PER_ID](this.item.job)
    }
  },
  methods: {
    dateDistanceToNow(dateStr) {
      return formatDistance(new Date(dateStr), new Date())
    }
  }
}
</script>

<style scoped></style>
