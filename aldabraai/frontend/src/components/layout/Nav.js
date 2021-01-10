// 
//import 'bootstrap/dist/css/bootstrap.min.css';
import 'tachyons';

// React and Redux dependecies
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import React, { Component, Fragment  } from 'react';
//

// Components actions and other
import { getSiteInfo } from '../../actions/StaticInfo';
//

export class NavBar extends Component {

    static propTypes = {
        site_info: PropTypes.array.isRequired
    };

    componentDidMount() {
        this.props.getSiteInfo();
    }

    render() {
        return(
            <div>
            <h1></h1>
            </div>
        );
    }

}

const mapStateToProps = state => ({
    site_info: state.site_info.site_info
})

export default connect(mapStateToProps, {getSiteInfo})(NavBar);