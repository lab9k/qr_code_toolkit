<template>
  <div class="container">
    <div class="columns is-multiline">
      <div
        v-for="historyItem in history"
        :key="historyItem.id"
        class="column is-12"
      >
        {{ JSON.stringify(historyItem) }}
        <div class="card">
          <div class="card-content">
            <div class="content">
              <p>{{ historyItem.last_update }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { actionTypes, getterTypes } from '../../store'
export default {
  name: 'ItemHistory',
  computed: {
    ...mapGetters([getterTypes.ITEM_PER_ID]),
    item() {
      return this[getterTypes.ITEM_PER_ID](parseInt(this.$route.params.id, 10))
    },
    history() {
      const itemHistory = this.item?.history?.map(
        (el) => el.serialized_data[0].fields
      )
      return itemHistory
    }
  },
  mounted() {
    this[actionTypes.FETCH_ALL_JOBS]()
  },
  methods: {
    ...mapActions([actionTypes.FETCH_ALL_JOBS])
  }
}
</script>

<style scoped></style>
