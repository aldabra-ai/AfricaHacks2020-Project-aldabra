import { GET_SITE_INFO } from '../actions/types';

const initialState = {
    site_info: [],
}

export default function(state = initialState, action ) {
    // evaluate action type
    switch (action.type) {
        case GET_SITE_INFO:
            return {
                ...state,
                site_info: action.payload
            }

            default:
                return state;
    }
}