<template>
  <div class="my-2">
    <v-btn color="blue-grey" fab small dark v-on:click="read_text(text)">
      <v-icon>mdi-voice</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  props: ["text"],
  methods: {
    read_text: function(text) {
      var synth = window.speechSynthesis;
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
      synth.speak(msg);
    }
  }
};
</script>

<style></style>
