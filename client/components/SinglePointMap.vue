<template>
  <div class="container">
    <client-only>
      <l-map :zoom="13" :center="loc">
        <l-control-layers />
        <l-lwms-tile-layer
          v-for="layer in layers"
          :key="layer.name"
          :layers="layer.layers"
          :visible="layer.visible"
          :name="layer.name"
          :format="layer.format"
          base-url="https://geo.gent.be/geoserver/ows"
        ></l-lwms-tile-layer>
        <l-marker :lat-lng="loc"></l-marker>
      </l-map>
    </client-only>
  </div>
</template>

<script>
export default {
  name: 'SinglePointMap',
  props: {
    location: {
      type: String,
      required: true
    }
  },
  computed: {
    loc() {
      return this.location.split(',')
    },
    layers() {
      return [
        {
          name: 'Stadsplan Gent',
          visible: true,
          format: 'image/png',
          layers: 'SG-E-Stadsplan:Stadsplan',
          transparent: true,
          attribution: 'Stad Gent'
        }
      ]
    }
  }
}
</script>

<style scoped lang="scss">
.container {
  width: 100%;
  height: 200px;
}
</style>
