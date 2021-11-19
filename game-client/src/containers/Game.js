import { useEffect } from 'react';
import { connect } from 'react-redux';
import Game from '../components/Game';
import appActions from '../actions';

const GameContainer = (props) => {
    useEffect(
        () => props.getCards(),
        []
    )
    return (
        <Game { ...props } />
    );
};

const mapDispatchToProps = {
    ...appActions,
};

const mapStateToProps = state => {
    return {
        cards: state.card.cards
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(GameContainer);
