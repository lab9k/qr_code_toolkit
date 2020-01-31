<template>
  <section class="section">
    <h1 class="title">Scan je werkorder</h1>
    <client-only>
      <scanner />
    </client-only>
  </section>
</template>

<script>
export default {
  name: 'HomePage',
  components: {
    scanner: () => import('@/components/client-only/Scanner')
  }
}
</script>
