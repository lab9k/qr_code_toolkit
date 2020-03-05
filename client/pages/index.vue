<template>
  <section class="section"></section>
</template>

<script>
export default {
  name: 'HomePage',
  middleware({ redirect }) {
    return redirect('/job')
  }
}
</script>
