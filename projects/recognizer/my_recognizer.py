import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Likelihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    
    for i in range(len(test_set.get_all_sequences())):
        #sequence = test_set.get_item_sequences(i)
        X, lengths = test_set.get_item_Xlengths(i)
        words_logL = {}
        best_score = float('-inf')
        best_guess = None
        for word, model in models.items():
            try:
                score = model.score(X, lengths)
                words_logL[word] = score # construc dict of logL
                if score > best_score: # update best guess and score
                    best_score = score
                    best_guess = word
            except:
                # if fail, return zero probability for such word (because e^-inf -> 0)
                words_logL[word] = float('-inf')
        
        probabilities.append(words_logL)
        guesses.append(best_guess)          
    
    return probabilities, guesses
    
