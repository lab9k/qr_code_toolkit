<template>
  <div>
    <header>
      <b-navbar :mobile-burger="true" type="is-primary">
        <template slot="brand">
          <b-navbar-item :to="{ path: '/' }" tag="router-link">
            QR-toolkit scanner
          </b-navbar-item>
          <b-navbar-item @click="toggleSideBar()">
            <b-icon icon="menu" />
            <span>Snelle job selectie</span>
          </b-navbar-item>
        </template>
        <template slot="end">
          <b-navbar-item :to="{ path: '/' }" tag="router-link">
            <b-icon icon="home" />
            <span>Alle jobs</span>
          </b-navbar-item>
          <b-navbar-item :to="{ path: '/map' }" tag="router-link">
            <b-icon icon="map-marker" />
            <span>Map</span>
          </b-navbar-item>
          <b-navbar-item :to="{ path: '/register' }" tag="router-link">
            <b-icon icon="plus-circle" />
            <span>Registreer</span>
          </b-navbar-item>
        </template>
      </b-navbar>
    </header>
    <side-bar ref="sidebar"></side-bar>
    <main class="main-content">
      <nuxt />
    </main>
  </div>
</template>

<script>
import SideBar from '../components/SideBar'
export default {
  components: { SideBar },
  data() {
    return {
      open: false
    }
  },
  methods: {
    toggleSideBar() {
      this.$refs.sidebar.toggle()
    }
  }
}
</script>

<style></style>
