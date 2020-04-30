<template>
  <div>
    <header>
      <b-navbar :mobile-burger="true" type="is-primary">
        <template slot="brand">
          <b-navbar-item :to="{ path: '/' }" tag="router-link">
            QR-toolkit scanner
          </b-navbar-item>
        </template>
        <template slot="end">
          <b-navbar-item :to="{ path: '/' }" tag="router-link">
            <b-icon icon="home" size="is-medium" />
          </b-navbar-item>
          <b-navbar-item :to="{ path: '/map' }" tag="router-link">
            <b-icon icon="map-marker" size="is-medium" />
          </b-navbar-item>
          <b-navbar-item :to="{ path: '/register' }" tag="router-link">
            <b-icon icon="plus-circle" size="is-medium" />
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
export default {}
</script>

<style></style>
