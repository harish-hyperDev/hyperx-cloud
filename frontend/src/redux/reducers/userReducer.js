import { actionTypes } from '../constants/actionTypes'

const initialState = {
    loggedInUserID: '' 
}

export const userReducer = (state = initialState, {type, payload}) => {
    switch(type) {
        case actionTypes.LOGIN_USER:
            return {
                ...state,
                loggedInUserID: payload
            }
        default:
            return state;
    }
}