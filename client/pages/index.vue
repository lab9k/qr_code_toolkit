<template>
  <section class="section">
    <h1 class="title">Scan je werkorder</h1>
    <div
      style="border: 1px solid grey; height: 320px; background-color: black;"
    ></div>
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
