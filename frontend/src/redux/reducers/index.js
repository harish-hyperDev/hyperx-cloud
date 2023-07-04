import { combineReducers } from 'redux';
import { userObjectsReducer } from './userObjectReducer.js';
import { userReducer } from './userReducer.js';

const reducers = combineReducers({
    allObjects: userObjectsReducer,
    userOps: userReducer
})

export default reducers;