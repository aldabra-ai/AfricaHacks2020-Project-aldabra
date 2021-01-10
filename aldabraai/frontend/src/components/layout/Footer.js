import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getSiteInfo } from '../../actions/StaticInfo';
import PropTypes from 'prop-types';

export class Footer extends Component {
    static propTypes = {
        site_info: PropTypes.array.isRequired
    };

    componentDidMount(){
        this.props.getSiteInfo();
    }

    render() {
        return(
            <footer className='footer'>

            </footer>
            );
    }
}

const mapStateToProps = state => ({
    site_info: state.site_info.site_info
});

export default connect(mapStateToProps, {getSiteInfo})(Footer);