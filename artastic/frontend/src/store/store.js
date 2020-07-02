import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        chips: [],
        searchParam: {},
        card: {},
        searchWordLabels: []
    },

    getters: {
        getSearchParam(state){
            return state.searchParam;
        },
        getChips(state){
            return state.chips;
        },
        getCard(state) {
            return state.card;
        },
        getSearchWordLabels(state) {
            return state.searchWordLabels;
        }
    },

    mutations: {
        setSearchParam(state, param){
            state.searchParam = param;
        },
        addChip(state, chip){
            if (!state.chips.includes(chip)) {
                state.chips.push(chip);
            }
        },
        setChips(state, array){
            state.chips = array;
        },
        addCard(state, card) {
            state.card = card;
        },
        addSearchWordLabels(state, labels) {
            state.searchWordLabels = labels;
        }
    }

})