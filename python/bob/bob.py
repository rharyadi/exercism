def hey(question):
    response = { 'asking': 'Sure.',
                 'yelling': 'Whoa, chill out!',
                 'silent': 'Fine. Be that way!',
                 'other': 'Whatever.' }
    
    question = question.strip()
    
    # Fine. Be that way!
    if not question:
        return response['silent']
    
    
    # Whoa, chill out!
    if question.isupper():
        return response['yelling']

    
    # Sure.
    if question.endswith('?'):
        return response['asking']

    
    # Whatever
    return response['other']
    
