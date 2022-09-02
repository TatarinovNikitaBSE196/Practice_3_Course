from pywsd.lesk import adapted_lesk


term_definition = {'velocity':
                       ['distance travelled per unit time'],
                   'acceleration':
                       ['(physics) a rate of increase of velocity'],
                   'momentum':
                       ['the product of a body\'s mass and its velocity'],
                   'impulse':
                       ['an impelling force or strength',
                        'the act of applying force suddenly'],
                   'collision':
                       ['(physics) a brief event in which two or more bodies come together'],
                   'torque':
                       ['a twisting force']}


# TODO: use better method
def check_sense(context, term):
    lesk_result = adapted_lesk(context, term)
    print(f'{lesk_result}: {lesk_result.definition()}')
    return lesk_result.definition() in term_definition[term]
