<template>
  <div class="container">
    <client-only>
      <scanner :registering="true" @result="createItem" />
    </client-only>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { actionTypes } from '../../store'
export default {
  components: { scanner: () => import('@/components/client-only/Scanner') },
  methods: {
    async createItem(id) {
      const exists = await this[actionTypes.FETCH_ITEM](id)
      if (!exists) {
        this.$buefy.dialog.prompt({
          message: `Welk item is dit?`,
          inputAttrs: {
            placeholder: 'bv. Paaltje 10',
            maxlength: 255
          },
          trapFocus: true,
          onConfirm: (value) => {
            const data = { name: value, id }
            this[actionTypes.REGISTER_ITEM](data)
              .then(() =>
                this.$buefy.toast.open({
                  duration: 5000,
                  message: `Item is geregistreerd`,
                  position: 'is-bottom',
                  type: 'is-success'
                })
              )
              .catch(() =>
                this.$buefy.toast.open({
                  duration: 5000,
                  message: `Er ging iets mis bij het registreren`,
                  position: 'is-bottom',
                  type: 'is-danger'
                })
              )
          }
        })
      } else {
        this.$buefy.toast.open({
          duration: 5000,
          message: `Dit item (${exists.name}) is al geregistreerd`,
          position: 'is-bottom',
          type: 'is-warning'
        })
      }
    },
    ...mapActions([actionTypes.FETCH_ITEM, actionTypes.REGISTER_ITEM])
  }
}
</script>

<style scoped></style>
