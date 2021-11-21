import * as types from "./actionTypes";

const loadGame = () => {
    return {
        type: types.LOAD_GAME,
    };
};

const onInputValueUpdate = (value) => {
    return {
        type: types.ANSWER_INPUT_CHANGE,
        value
    }
};

const submitAnswer = (answer) => {
    return {
        type: types.SUBMIT_ANSWER,
        data: {},
        params: {answer: answer} 
    }
};

const appActions = {
    loadGame,
    submitAnswer,
    onInputValueUpdate
}

export default appActions;
