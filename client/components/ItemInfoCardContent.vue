import { formatDistance } from "date-fns"
<template>
  <div class="content">
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">Name</h6>
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
        <h6 class="title is-6 is-marginless">Location</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">{{ item.location }}</p>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">In Use</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">{{ item.is_in_use }}</p>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">Is Missing</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">{{ item.missing }}</p>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2 is-paddingless">
        <h6 class="title is-6 is-marginless">Last Update</h6>
      </div>
      <div class="column is-10 is-paddingless">
        <p class="is-marginless">
          {{ dateDistanceToNow(item.last_update) }} ago
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { formatDistance } from 'date-fns'
import { getterTypes } from '../store'
export default {
  name: 'ItemInfoCardContent',
  props: {
    item: {
      type: Object,
      required: true
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
