<template>
  <div id="map-wrap" class="container">
    <client-only>
      <l-map :zoom="13" :center="[51.0538286, 3.7250121]">
        <l-tile-layer
          url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
        ></l-tile-layer>
        <l-marker
          v-for="item in items"
          :key="item.id"
          :lat-lng="item.location.split(',')"
        >
          <l-popup>
            <div class="container popup">
              <h3>{{ item.name }}</h3>
              <div class="columns">
                <div class="column is-half">
                  <b-button
                    :to="{ path: `/history/${item.item_id}` }"
                    type="is-info is-light is-small"
                    tag="router-link"
                  >
                    History
                  </b-button>
                </div>
              </div>
            </div>
          </l-popup>
        </l-marker>
      </l-map>
    </client-only>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getterTypes, actionTypes } from '../../store'
export default {
  name: 'MapView',
  computed: {
    ...mapGetters({ items: getterTypes.ALL_KNOWN_ITEMS })
  },
  mounted() {
    this.$store.dispatch(actionTypes.FETCH_ALL_JOBS)
  }
}
</script>

<style lang="scss" scoped>
#map-wrap {
  width: 100%;
  height: 90vh;
  .popup {
    width: 300px;
  }
}
</style>
