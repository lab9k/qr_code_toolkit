<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="card">
          <div class="card-image">
            <client-only>
              <figure>
                <img
                  :src="
                    `https://qrcodeservice.herokuapp.com/?query=${currentURL}`
                  "
                  alt="Placeholder image"
                />
              </figure>
            </client-only>
          </div>
          <div class="card-content">
            <item-info-card-content :item="item" />
          </div>
        </div>
      </div>
      <div class="column is-12">
        <h4 class="title is-4">Geschiedenis</h4>
      </div>
      <template v-if="isUpdated">
        <div class="column is-12">
          <b-collapse
            v-for="(historyItem, index) in history"
            :key="index"
            :open="isOpen[index] === true"
            @open="isOpen[index] = true"
            @close="isOpen[index] = false"
            class="card"
          >
            <div
              slot="trigger"
              slot-scope="props"
              class="card-header"
              role="button"
            >
              <p class="card-header-title">
                {{ dateDistanceToNow(historyItem.fields.last_update) }} ago
              </p>
              <a class="card-header-icon">
                <b-icon :icon="props.open ? 'menu-down' : 'menu-up'"> </b-icon>
              </a>
            </div>
            <div class="card-content">
              <item-info-card-content :item="historyItem.fields" />
            </div>
          </b-collapse>
        </div>
      </template>
      <template v-else>
        <div class="column is-12">
          <div class="card">
            <div class="card-content">
              <div class="content">
                <p>Dit item heeft nog geen updates gekregen.</p>
              </div>
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { formatDistance } from 'date-fns'
import { actionTypes, getterTypes } from '../../store'
import ItemInfoCardContent from '../../components/ItemInfoCardContent'
export default {
  name: 'ItemHistory',
  components: { ItemInfoCardContent },
  data() {
    return {
      isOpen: []
    }
  },
  computed: {
    ...mapGetters([getterTypes.ITEM_PER_ID]),
    item() {
      return this[getterTypes.ITEM_PER_ID](parseInt(this.$route.params.id, 10))
    },
    history() {
      return this.item.history.map((el) => el.serialized_data[0])
    },
    isUpdated() {
      return this.history.length > 0
    },
    currentURL() {
      if (process.client) {
        return window.location.href
      }
      return ''
    }
  },
  async serverPrefetch() {
    await this[actionTypes.FETCH_ALL_JOBS]()
  },
  methods: {
    ...mapActions([actionTypes.FETCH_ALL_JOBS]),
    dateDistanceToNow(dateStr) {
      return formatDistance(new Date(dateStr), new Date())
    }
  }
}
</script>

<style scoped></style>
