import * as types from "./actionTypes";

const getCards = () => {
    return {
        type: types.FETCH_CARDS,
    };
};

const appActions = {
    getCards
}

export default appActions;
