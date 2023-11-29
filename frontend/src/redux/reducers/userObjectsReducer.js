import { actionTypes } from '../constants/actionTypes'

const initialState = {
    userObjects: []
}

export const userObjectsReducer = (state = initialState, {type, payload}) => {
    switch(type) {
        case actionTypes.GET_USER_OBJECTS:
            return state
        default:
            return state;
    }
}