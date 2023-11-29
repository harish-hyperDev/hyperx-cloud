const formReducer = (state, action) => {
    switch (action.type) {
        case 'input':
            return {
                ...state,
                [action.field]: action.payload
            }

        default:
            return state
    }
}

export default formReducer