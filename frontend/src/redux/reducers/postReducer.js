import { actionTypes } from "../constants/actionTypes"

const initialState = {
    posts: [
        {
            albumId: 1,
            id: 2,
            title: "reprehenderit est deserunt velit ipsam",
            url: "https://via.placeholder.com/600/771796",
            thumbnailUrl: "https://via.placeholder.com/150/771796"
        },
        {
            albumId: 2,
            id: 3,
            title: "kowwaa ki est deserunt velit ipsam",
            url: "https://via.placeholder.com/600/771796",
            thumbnailUrl: "https://via.placeholder.com/150/771796"
        }
    ]
}

export const postReducer = (state = initialState, {type, payload}) => {
    switch(type) {
        case actionTypes.SELECTED_POSTS:
            return state;
        default:
            return state;
    }
}

