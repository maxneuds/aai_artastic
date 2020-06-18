<template>
  <mark class="custom" @click="$emit('generateChip', text)">
    <slot></slot>
  </mark>
</template>

<script>
export default {
  props: {
    index: Number, // From TextHighlight
    text: String // From TextHighlight, equals to `this.$slots.default[0].text`
  }
};
</script>

<style>
</style>