import { React } from 'react';
import { Card, Input, Button } from '@mui/material';
import './Game.css';

const Game = ({ game, inputValue, onInputValueUpdate, submitAnswer, inputHighlightStyle, loadGame }) => {

    const buildPhraseTemplate = () => {
        var inputStyle = { 'width': game.task.answer.length * 25 };
        var phraseSplits = game.task.phrase_template.split(' ');
        return (
            phraseSplits.map(
                part => part.includes('*') > 0 ?
                        <div style={ inputStyle }>
                            <Input 
                                value={ inputValue } 
                                onChange={ e => onInputValueUpdate(e.target.value) }
                                className={ 'card-input ' + inputHighlightStyle }
                                fullWidth={ true }
                                disableUnderline={ true }
                            />
                        </div> 
                    : 
                        <p className="card-task-text"> { part } </p>
            )
        )
    };

    const buildProgressBars = () => {
        let attempts = [];
        let correct = [];
        let wrong = [];
        let help = [];
      
        for (var i=0; i < game.card_progress.attempts; i++) {
            attempts.push(<div className='indicator attempts'/>)
        }
        for (var i=0; i < game.card_progress.correct; i++) {
            correct.push(<div className='indicator correct'/>)
        }
        for (var i=0; i < game.card_progress.wrong; i++) {
            wrong.push(<div className='indicator wrong'/>)
        }
        for (var i=0; i < game.card_progress.help; i++) {
            help.push(<div className='indicator help'/>)
        }
        return (
            <> 
                <div className='progress'>
                    { attempts }
                </div>
                <div className='progress'>
                    { correct }
                </div>
                <div className='progress'>
                    { wrong }
                </div>
                <div className='progress'>
                    { help }
                </div>
            </>
        );
    };

    return (    
        game && !game?.finished ? 
            <Card className="card">
                <div className="card-header">
                    <div className="card-progress">
                        { 
                            !game.card_progress.attempts ? <p style={{ color: 'orange'}}>New word!</p> :  buildProgressBars()
                        }
                    </div>
                </div>
                <div className="card-task">
                    <div className="card-task-phrase">
                        { buildPhraseTemplate() }
                    </div>
                    <div className="card-task-context">
                        <p>{ game.task.card.word }</p>
                        <p>{ game.task.card.context }</p>
                    </div>
                    <Button variant="outlined" className="card-button" onClick={ () => submitAnswer(inputValue) }> 
                        { inputValue === '' ? 'Reveal' : 'Enter' }
                    </Button>
                </div>
            </Card> 
        : 
            <Card className="card new-game">
                <p> Good job! </p>
                <Button variant="outlined" className="card-button new-game" onClick={ () => loadGame() }> 
                    play again
                </Button>
            </Card>
    );    
};

export default Game;