<template>
  <div>
    <qrcode-stream @decode="onDecode" @init="onInit">
      <div v-if="loading" class="loading-indicator">
        Loading...
      </div>
      <div v-if="error" class="error-indicator has-text-danger">
        {{ error }}
      </div>
    </qrcode-stream>
    <scanned-item-modal
      :is-modal-visible="modalVisible"
      :item="item"
      @confirm="confirm"
      v-if="!registering"
    />
  </div>
</template>

<script>
import { QrcodeStream } from 'vue-qrcode-reader'
import { mapActions } from 'vuex'
import { actionTypes } from '../../store'
import ScannedItemModal from '../ScannedItemModal'

export default {
  name: 'Scanner',
  components: {
    ScannedItemModal,
    QrcodeStream
  },
  props: {
    registering: {
      required: false,
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      result: null,
      error: null,
      loading: false,
      modalVisible: false,
      item: { name: '' }
    }
  },
  methods: {
    onDecode(result) {
      this.result = result
      const id = parseInt(result.match(/\/([0-9]+)\//)[1], 10)
      if (this.registering === true) {
        this.$emit('result', id)
      } else {
        this.$store.dispatch(actionTypes.FETCH_ITEM, id).then((item) => {
          this.item = item
          this.modalVisible = true
        })
      }
    },
    async onInit(promise) {
      this.loading = true
      try {
        await promise
      } catch (error) {
        if (error.name === 'NotAllowedError') {
          this.error = 'ERROR: you need to grant camera access permisson'
        } else if (error.name === 'NotFoundError') {
          this.error = 'ERROR: no camera on this device'
        } else if (error.name === 'NotSupportedError') {
          this.error = 'ERROR: secure context required (HTTPS, localhost)'
        } else if (error.name === 'NotReadableError') {
          this.error = 'ERROR: is the camera already in use?'
        } else if (error.name === 'OverconstrainedError') {
          this.error = 'ERROR: installed cameras are not suitable'
        } else if (error.name === 'StreamApiNotSupportedError') {
          this.error = 'ERROR: Stream API is not supported in this browser'
        }
      } finally {
        this.loading = false
      }
    },
    confirm(valid) {
      this.modalVisible = false
      if (valid) {
        this.$emit('result', this.item)
      }
    },
    ...mapActions([actionTypes.FETCH_ITEM])
  }
}
</script>
<style>
.loading-indicator,
.error-indicator {
  font-weight: bold;
  font-size: 2rem;
  text-align: center;
}
</style>
