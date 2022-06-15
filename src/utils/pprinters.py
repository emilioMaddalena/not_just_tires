def print_deb(str, state):
    '''
    If in debug state, print message preceded by the envelope emoji.
    '''
    if state == 'DEBUG': print(f"\n📨: {str}\n")
        