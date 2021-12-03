import { useEffect } from 'react';
import { connect } from 'react-redux';
import { debounce } from 'lodash';
import Game from '../components/Game';
import appActions from '../actions';

const GameContainer = (props) => {
    useEffect(
        () => props.loadGame(),
        []
    );

    const handleSubmitDebounced = e => {
        if (e.keyCode === 13 || e.code === "NumpadEnter") {
            e.preventDefault();        
            props.submitAnswer(props.inputValue);
        }
    };

    useEffect(
        () => {
            document.addEventListener("keydown", debounce(handleSubmitDebounced, 300));
            return () => {
                document.removeEventListener("keydown", debounce(handleSubmitDebounced, 300));
            };
      }, []);

    return (
        <Game 
            { ...props } 
        />
    );
};

const mapDispatchToProps = {
    ...appActions,
};

const mapStateToProps = state => {
    return {
        game: state.game.game,
        inputValue: state.game.inputValue,
        inputHighlightStyle: state.game.inputHighlightStyle
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(GameContainer);
