import { React } from 'react';
import { Card, Input, Button } from '@mui/material';
import './Game.css';

const Game = ({ game, inputValue, onInputValueUpdate, submitAnswer, inputHighlightStyle }) => {
    const buildPhraseTemplate = () => {
        var splitIdx = game.task.phrase_template.indexOf('*');
        var inputSize = (game.task.answer.length).toString() + ' px';
        var phraseSplits = game.task.phrase_template.split(' ');
        
        return (
            phraseSplits.map(
                part => part.includes('*') > 0 ? 
                        <Input 
                            value={ inputValue } 
                            onChange={ e => onInputValueUpdate(e.target.value) }
                            className={ inputHighlightStyle }
                            style={{ 'width': inputSize }}>
                        </Input> 
                    : 
                        <p className="card-task-text"> { part } </p>
            )
        )
    };

    return (    
        <Card className="card">
            { 
                game && 
                    <>
                    <div className="card-header">
                    <div className="card-progress">

                    </div>
                    </div>
                    <div className="card-task">
                        <>
                            { buildPhraseTemplate() }
                        </>
                        <div className="card-task-context">
                            <p>{ game.task.card.word }</p>
                            <p>{ game.task.card.context }</p>
                        </div>
                    </div>
                    </>
            }
            
            <Button variant="outlined" className="card-button" onClick={ () => submitAnswer(inputValue) }> 
                { inputValue === '' ? 'Reveal' : 'Enter' }
            </Button>
        </Card>
        
    );
};

export default Game;