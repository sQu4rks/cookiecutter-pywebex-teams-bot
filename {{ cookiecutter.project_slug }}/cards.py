from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.components import TextBlock
from pyadaptivecards.inputs import Text, Number
from pyadaptivecards.actions import Submit

def make_card_payload(card):
    """Create a attachment payload from a adaptive card instance. 

    Args:
        card (AdaptiveCard): Instance of the adaptive card for this attachment. 

    Raises:
        Exception: If card is not a subclass of AdaptiveCard or an instance of
            AdaptiveCard.

    Returns:
        dict: A attachment payload containing the specified card. 
    """
    if not issubclass(type(card), AdaptiveCard) and not isinstance(card, AdaptiveCard):
        raise Exception('card must be either a subclass of AdaptiveCard or an instance of AdaptiveCard')
    
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": card.to_dict(),
    }

    return attachment

class ResponseCard(AdaptiveCard):
    """Sample adaptive card created using the pyadaptivecards framework.

    You can find out more about pyadaptivecards here: https://github.com/CiscoSE/pyadaptivecards
    """
    def __init__(self, name):
        body = []
        actions = []

        # Create a greeting using the name provided
        greeting = TextBlock("Hey hello {}! I am an adaptive card".format(name))
        body.append(greeting)

        # Create a question input
        question = Text('question', placeholder="Question")
        body.append(question)

        # Create a submit action
        submit = Submit(title="Send the card!")
        actions.append(submit)

        super().__init__(body=body, actions=actions)
        

