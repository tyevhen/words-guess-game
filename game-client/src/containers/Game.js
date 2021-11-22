import { useEffect } from 'react';
import { connect } from 'react-redux';
import Game from '../components/Game';
import appActions from '../actions';

const GameContainer = (props) => {
    useEffect(
        () => props.loadGame(),
        []
    );

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
