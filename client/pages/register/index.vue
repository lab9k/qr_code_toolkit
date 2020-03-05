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
      // TODO: check if item exists
      const exists = await this[actionTypes.FETCH_ITEM](id)
      // TODO: if not, create popup, asking for name, POST data to backend
      if (!exists) {
        this.$buefy.dialog.prompt({
          message: `What is the item name?`,
          inputAttrs: {
            placeholder: 'e.g. Paaltje 10',
            maxlength: 255
          },
          trapFocus: true,
          onConfirm: (value) => {
            const data = { name: value, id }
            this[actionTypes.REGISTER_ITEM](data)
              .then(() =>
                this.$buefy.toast.open('Item successfully registered!')
              )
              .catch(() => this.$buefy.toast.open('Something went wrong!'))
          }
        })
      } else {
        this.$buefy.toast.open(
          `This item (${exists.name}) is already registered`
        )
      }
    },
    ...mapActions([actionTypes.FETCH_ITEM, actionTypes.REGISTER_ITEM])
  }
}
</script>

<style scoped></style>
