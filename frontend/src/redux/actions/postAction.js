import { actionTypes } from '../constants/actionTypes'

export const setPosts = (posts) => {
    return {
        type: actionTypes.SELECTED_POSTS,
        payload: posts,
    }
}