def hey(question):
    response = [ 'Sure.',
                 'Whoa, chill out!',
                 'Fine. Be that way!',
                 'Whatever.' ]
    
    question = question.strip()
    
    # Fine. Be that way!
    if not question:
        return response[2]
    
    
    # Whoa, chill out!
    alphacount = sum(1 for c in question if c.isalpha())
    uppercount = sum(1 for c in question if c.isupper())
    if uppercount and uppercount == alphacount:
        return response[1]

    
    # Sure.
    if question[-1] == '?':
        return response[0]

    
    # Whatever
    return response[3]
    
