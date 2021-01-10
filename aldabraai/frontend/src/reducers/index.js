import { combineReducers } from 'redux';
import site_info from './site_info';
import active_features from './active_features';

const rootReducer = combineReducers({
    site_info,
    active_features,
});

export default rootReducer;
