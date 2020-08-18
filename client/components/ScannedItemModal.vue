<template>
  <b-modal :active.sync="isModalVisible" scroll="keep">
    <div class="card">
      <div class="card-content">
        <div class="content">
          {{ item.name }}
        </div>
      </div>
      <footer class="card-footer">
        <a @click="confirm(true)" class="card-footer-item has-text-success">
          Bevestig
        </a>
        <a @click="confirm(false)" class="card-footer-item has-text-danger">
          Annuleer
        </a>
      </footer>
    </div>
  </b-modal>
</template>

<script>
export default {
  name: 'ScannedItemModal',
  props: {
    isModalVisible: {
      required: true,
      type: Boolean
    },
    item: {
      required: true,
      type: Object,
      default: () => ({ name: '' })
    }
  },
  methods: {
    confirm(valid) {
      this.$emit('confirm', valid)
    }
  }
}
</script>

<style scoped></style>
