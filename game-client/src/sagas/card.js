import { all, call, delay, put, takeEvery, takeLatest } from 'redux-saga/effects';
import CardService from '../services/CardService';
import * as type from '../actionTypes';

const cardService = new CardService();

function* fetchCardsFlow(action) {
    try {
        console.log("EVER BEEN HERE");
        const response = yield call(cardService.find, action.data);
        console.log("response -> ", response);
        yield put({ type: type.FETCH_CARDS_SUCCESS, response });
    } catch(error) {
        yield put({ type: type.FETCH_CARDS_FAILURE, error });
    }
}

function* watchFetchCardsFlow() {
    yield takeLatest(type.FETCH_CARDS, fetchCardsFlow);
}

export default function* cardsSaga() {
    yield all([
        watchFetchCardsFlow(),
    ]);
};