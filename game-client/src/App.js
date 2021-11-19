import React from 'react';
import { connect } from 'react-redux';
import { Container, Box } from '@mui/material';
import Game from './containers/Game';

const App = () => {
    return (
        <Container>
            <Game/>
        </Container>
    );
};

export default App;
