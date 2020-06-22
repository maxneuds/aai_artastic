import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        card: { test: "testitest2" }
    },

    getters: {
        getCard(state) {
            return state.card;
        }
    },

    mutations: {
        addCard(state, card) {
            state.card = card;
        }
    }

})