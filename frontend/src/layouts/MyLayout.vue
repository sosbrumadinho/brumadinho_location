<template>
  <q-layout view="lHh Lpr lFf">
    <q-layout-header>
      <q-toolbar
        color="red-7"
        :inverted="$q.theme === 'ios'"
      >
        <q-toolbar-title>
          Location Tool
          <div slot="subtitle">Report</div>
        </q-toolbar-title>
        <q-btn
          flat
          dense
          round
          @click="rightDrawerOpen = !rightDrawerOpen"
          aria-label="Menu"
        >
          <q-icon name="settings" />
        </q-btn>
      </q-toolbar>
    </q-layout-header>

    <q-layout-drawer
    side='right'
      v-model="rightDrawerOpen"
      :content-class="$q.theme === 'mat' ? 'bg-grey-2' : null"
    >
      <q-list
        no-border
        link
        inset-delimiter
      >
        <q-list-header>Menu Principal</q-list-header>
        <q-item>
          <q-toggle @change="togglePersonIcons" v-model="personIcons" color="red-7" icon="person" label="Ícones de pessoas" />
        </q-item>
        <q-item>
          <q-toggle @change="toggleAnimalIcons" v-model="animalIcons" color="red-7" icon="pets" label="Ícones de animais" />
        </q-item>
        <q-item>
          <q-toggle @change="toggleSearchIcons" v-model="searchIcons" color="red-7" icon="search" label="Ícones de buscas" />
        </q-item>
        <q-item>
          <q-toggle v-model="heatmapLayer" color="red-7" icon="layers" label="Mapa de calor" />
        </q-item>
        <q-item>
        <q-option-group
          color="red-7"
          type="radio"
          v-model="currentLayer"
          :options="layers"
        />
        </q-item>
      </q-list>
    </q-layout-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name: 'MyLayout',
  data () {
    return {
      rightDrawerOpen: false,
      heatmapLayer: true,
      searchIcons: false,
      personIcons: true,
      animalIcons: true,
      satelliteLayer: false,
      topologyLayer: false,
      currentLayer: 'map',
      layers: [
        {label: 'Mapa', value: 'map'},
        {label: 'Satélite', value: 'satellite'},
        {label: 'Topologia', value: 'topology'}
      ]
    }
  },
  watch: {
    heatmapLayer: function (val) {
      this.$root.$emit('enable-Heatmap', val)
    },
    searchIcons: function (val) {
      this.$root.$emit('enable-searchIcons', val)
    },
    personIcons: function (val) {
      this.$root.$emit('enable-personIcons', val)
    },
    animalIcons: function (val) {
      this.$root.$emit('enable-animalIcons', val)
    },
    currentLayer: function (val) {
      this.$root.$emit('enable-layer', val)
    }
  },
  methods: {
    toggleHeatmap () {
      console.log('teste')
      this.$root.$emit('enable-Heatmap', 'true')
    },
    toggleSearchIcons () {
      this.$root.$emit('enable-searchIcons', this.searchIcons)
    },
    togglePersonIcons () {
      this.$root.$emit('enable-personIcons', this.personIcons)
    },
    toggleAnimalIcons () {
      this.$root.$emit('enable-animalIcons', this.animalIcons)
    },
    toggleSatellite () {
      this.$root.$emit('enable-satellite', this.satelliteLayer)
    },
    toggleTopology () {
      this.$root.$emit('enable-topology', this.topologyLayer)
    }
  },
  mounted () {
  }
}
</script>

<style>
</style>
