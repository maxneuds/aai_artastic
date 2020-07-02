<template>
  <div class="my-2">
    <v-btn color="blue-grey" fab small dark v-on:click="toggleFunction(text)">
      <v-icon v-if="!isSpeaking">mdi-voice</v-icon>
      <v-icon v-if="isSpeaking">mdi-pause-circle-outline</v-icon>
    </v-btn>
  </div>
</template>

<script>
var synth = window.speechSynthesis;

export default {
  props: ["text"],
  data: () => ({
    isSpeaking: false
  }),
  beforeDestroy: function() {
    synth.cancel();
  },
  methods: {
    toggleFunction: function(text) {
      if (!this.isSpeaking) {
        if (synth.paused) {
          this.isSpeaking = true;
          synth.resume();
        }
        this.read_text(text);
      } else {
        this.isSpeaking = false;
        synth.pause();
      }
    },
    read_text: function(text) {
      var voices = synth.getVoices();
      var msg = new SpeechSynthesisUtterance();
      msg.voice = voices.filter(function(voice) {
        return voice.lang == "en-US";
      })[0];
      msg.lang = "en-US";
      msg.volume = 1; // 0 to 1
      msg.rate = 0.7; // 0.1 to 10
      msg.pitch = 1; //0 to 2
      msg.text = text;
      this.isSpeaking = true;
      synth.speak(msg);
    }
  }
};
</script>

<style></style>
