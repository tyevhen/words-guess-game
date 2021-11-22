import * as types from '../actionTypes';

const initialState = {
    game: undefined,
    inputValue: '',
    inputHighlightStyle: 'default'
};

export default function card(state = initialState, action) {
    switch (action.type) {
        case types.LOAD_GAME_SUCCESS:
            return { ...state, game: action.response.data };
        case types.ANSWER_INPUT_CHANGE:
            return { ...state, inputValue: action.value };
        case types.SUBMIT_ANSWER_SUCCESS:
            return { ...state, game: action.response.data, inputValue: '' };
        case types.ANSWER_CORRECT:
            return { ...state, inputHighlightStyle: 'correct' };    
        case types.ANSWER_WRONG:
            return { ...state, inputHighlightStyle: 'wrong' };    
        case types.ANSWER_HELP:
            return { ...state, inputHighlightStyle: 'help', inputValue: action.answer }; 
        case types.RESET_STYLE:
            return { ...state, inputHighlightStyle: initialState.inputHighlightStyle };   
    default:
        return state
    }
}
