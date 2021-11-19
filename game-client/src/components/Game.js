import { React } from 'react';
import { Card, TextField, Button } from '@mui/material';

const Game = ({ cards, getCards }) => {
    console.log("cards", cards);
    return (    
        <Card>
            <TextField id="filled-basic" variant="filled" />
            <Button variant="outlined" onClick={ () => getCards() }> 
                get cards 
            </Button>
        </Card>
        
    );
};

export default Game;