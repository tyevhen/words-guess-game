import * as types from '../actionTypes';

const initialState = {
    cards: [],
};

export default function card(state = initialState, action) {
    console.log("ACTION", action);
    switch (action.type) {
        case types.FETCH_CARDS_SUCCESS:
            return { ...state, cards: action.response.data };
    default:
        return state
    }
}
