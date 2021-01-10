import { GET_ACTIVE_FEATURES } from '../actions/types';

const initialState = {
    active_features: []
}

export default function(state = initialState, action ) {
    // evaluate action type
    switch (action.type) {
        case GET_ACTIVE_FEATURES:
            return {
                ...state,
                active_fetures: action.payload
            }

            default:
                return state;
    }
}