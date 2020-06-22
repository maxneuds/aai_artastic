import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        card: {},
        searchWordLabels: []
    },

    getters: {
        getCard(state) {
            return state.card;
        },
        getSearchWordLabels(state) {
            return state.searchWordLabels;
        }
    },

    mutations: {
        addCard(state, card) {
            state.card = card;
        },
        addSearchWordLabels(state, labels) {
            state.searchWordLabels = labels;
        }
    }

})