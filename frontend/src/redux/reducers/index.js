import { combineReducers } from 'redux';
import { userObjectsReducer } from './userObjectsReducer';
import { userReducer } from './userReducer.js';

const reducers = combineReducers({
    allObjects: userObjectsReducer,
    userOps: userReducer
})

export default reducers;