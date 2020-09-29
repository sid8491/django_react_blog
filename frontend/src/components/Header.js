import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import CssBaseline from '@material-ui/core/CssBaseline';
import { makeStyles } from '@material-ui/core';

const useStyles = makeStyles((theme) =>({
    appBar: {
        borderBottom: `1px solid ${theme.palette.divider}`
    },
}))


function Header() {
    const classes = useStyles();
    return (
        <>
            <CssBaseline />
            <AppBar position='static' color='white' elevation={0} className={classes.appBar}>
                <Toolbar>
                    <Typography variant='h5' color='red' noWrap>
                        BlogMeUp
                    </Typography>
                </Toolbar>
            </AppBar>
        </>
    )
}

export default Header;
