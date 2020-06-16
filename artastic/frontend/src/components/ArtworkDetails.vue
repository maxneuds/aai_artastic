<template>
  <div class="pt-5">
    <div v-if="artwork && artwork.results">
      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">Property</th>
              <th class="text-left">Value</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(prop, index) in artwork.results.bindings" :key="index">
              <td>{{ prop.property.value }}</td>
              <td>{{ prop.value.value }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </div>
    <p v-if="!artwork">No artwork bro</p>
  </div>
</template>

<script>
export default {
  props: ["artwork"]
};
</script>

<style scoped>
</style>