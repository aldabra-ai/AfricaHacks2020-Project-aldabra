import axios from 'axios';
// import action types
import { GET_SITE_INFO, GET_ACTIVE_FEATURES } from './types';


// GET site info and dispatch to StaticInfo reducer
export const getSiteInfo = () => dispatch => {
    axios.get("/api/base/site_info?app_name='aldabra.ai' ")
    .then(response => {
        dispatch({
            type: GET_SITE_INFO,
            payload: response.data
        });
    }).catch(err => console.log(err))
};

// GET active features and dispatch to StaticInfo reducer
export const getActiveFeatures = () => dispatch => {
    axios.get("/api/base/features")
    .then(response => {
        dispatch({
            type: GET_ACTIVE_FEATURES,
            payload: response.data
        });
    }).catch(err => console.log(err))
};