<template>
  <div>
    <header>
      <b-navbar :mobile-burger="false" type="is-primary">
        <template slot="brand">
          <b-navbar-item :to="{ path: '/' }" tag="router-link">
            QR-toolkit scanner
          </b-navbar-item>
          <b-navbar-item :to="{ path: '/' }" class="m-l-auto" tag="router-link">
            <b-icon icon="home" size="is-medium" />
          </b-navbar-item>
        </template>
      </b-navbar>
    </header>
    <main class="main-content">
      <nuxt />
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          title: 'Home',
          icon: 'home',
          to: { name: 'index' }
        },
        {
          title: 'Inspire',
          icon: 'lightbulb',
          to: { name: 'inspire' }
        }
      ]
    }
  }
}
</script>

<style>
.navbar-brand {
  flex-grow: 1;
}

.navbar-menu {
  display: none;
}
</style>
