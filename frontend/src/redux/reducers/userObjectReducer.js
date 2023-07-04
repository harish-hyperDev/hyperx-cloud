import { actionTypes } from "../constants/actionTypes"

const initialState = {
    objects: [
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

export const userObjectsReducer = (state = initialState, {type, payload}) => {
    switch(type) {
        case actionTypes.CREATE_USER_OBJECTS:
            return {
                ...state,
                objects: [...state.objects, payload]
                
            };
        default:
            return state;
    }
}

