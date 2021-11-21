import { all, call, delay, put, takeEvery, takeLatest } from 'redux-saga/effects';
import GameService from '../services/GameService';
import * as types from '../actionTypes';

const gameService = new GameService();

function* loadGameFlow(action) {
    try {
        const response = yield call(gameService.find, action.data);
        yield put({ type: types.LOAD_GAME_SUCCESS, response });
    } catch(error) {
        yield put({ type: types.LOAD_GAME_FAILURE, error });
    }
}

function* watchLoadGameFlow() {
    yield takeLatest(types.LOAD_GAME, loadGameFlow);
}


function* submitAnswerFlow(action) {
    try {
        const response = yield call(gameService.create, action.data, action.params);
        if (response.data.is_valid) {
            yield put({ type: types.ANSWER_CORRECT });
        } else if (response.data.is_valid === null) {
            yield put({ type: types.ANSWER_HELP });
        } else if (!response.data.is_valid) {
            yield put({ type: types.ANSWER_WRONG });
        }
        yield delay(2000);
        yield put({ type: types.RESET_STYLE });
        yield put({ type: types.SUBMIT_ANSWER_SUCCESS, response });
    } catch(error) {
        yield put({ type: types.SUBMIT_ANSWER_FAILURE, error });
    }
}

function* watchSubmitAnswerFlow() {
    yield takeLatest(types.SUBMIT_ANSWER, submitAnswerFlow);
}

export default function* cardsSaga() {
    yield all([
        watchLoadGameFlow(),
        watchSubmitAnswerFlow()
    ]);
};