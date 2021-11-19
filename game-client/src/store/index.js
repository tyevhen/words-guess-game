import { createStore, applyMiddleware } from "redux";
import createSagaMiddleware from "redux-saga";
import rootReducer from "../reducers/index";
import rootSaga from "../sagas/index";

const saga = createSagaMiddleware();
const store = createStore(rootReducer, applyMiddleware(saga));

saga.run(rootSaga);

const unsubscribe = store.subscribe(() => {
    console.groupEnd();
});

export default store;
