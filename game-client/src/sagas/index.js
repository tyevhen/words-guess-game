import { put, call, all } from "redux-saga/effects";
import cardsSaga from './card';


export default function* rootSaga() {
    yield(
        all([
            cardsSaga()
        ])
    )
}
