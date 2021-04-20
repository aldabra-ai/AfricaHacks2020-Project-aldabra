import { Box } from '@material-ui/core'
import React from 'react'

export Interface GlassCardProps extends BoxProps{

}


const GlassCard = (GlassCardProps) => {
    const {... rest} = props;
    return (
       <Box {...rest}/>
    )
}

export default GlassCard
