from string import letters, digits



class CuteType:
    INT=1
    ID=4
    MINUS=2
    PLUS=3
    L_PAREN=5
    R_PAREN=6
    TRUE=8
    FALSE=9
    TIMES=10
    DIV=11
    LT=12
    GT=13
    EQ=14
    APOSTROPHE=15
    DEFINE=20
    LAMBDA=21
    COND=22
    QUOTE=23
    NOT=24
    CAR=25
    CDR=26
    CONS=27
    ATOM_Q=28
    NULL_Q=29
    EQ_Q=30

    KEYWORD_LIST=('define', 'lambda', 'cond','quote', 'not', 'car', 'cdr',' cons', 'atom?', 'null?', 'eq?' )
    BINARYOP_LIST=(DIV, TIMES, MINUS, PLUS, LT, GT, EQ)
    BOOLEAN_LIST=(TRUE, FALSE)

def check_keyword(token):
    """
    :type token:str
    :param token:
    :return:
    """
    if token.lower() in CuteType.KEYWORD_LIST:
        return True
    return False

def _get_keyword_type(token):
    return {
        'define':   CuteType.DEFINE,
        'lambda':   CuteType.LAMBDA,
        'cond':     CuteType.COND,
        'quote':    CuteType.QUOTE,
        'not':      CuteType.NOT,
        'car':      CuteType.CAR,
        'cdr':      CuteType.CDR,
        'cons':     CuteType.CONS,
        'atom?':    CuteType.ATOM_Q,
        'null?':    CuteType.NULL_Q,
        'eq?':      CuteType.EQ_Q
    }[token]

CUTETYPE_NAMES=dict((eval(attr, globals(), CuteType.__dict__), attr) for attr in dir(CuteType()) if not callable(attr) and not attr.startswith("__"))


class Token(object):
    def __init__(self, type, lexeme):
        """
        :type type:CuteType
        :type lexeme: str
        :param type:
        :param lexeme:
        :return:
        """
        self.type=type
        self.lexeme=lexeme
        #print type

    def __str__(self):
        #return self.lexeme
        return "[" + CUTETYPE_NAMES[self.type] + ": " + self.lexeme + "]"
    def __repr__(self):
        return str(self)


class CuteScanner(object):
    """
    :type token_iter:iter
    """

    def __init__(self, source):
        """
        :type source:str
        :param source:
        :return:
        """
        source = source.strip()
        token_list = source.split(" ")
        self.token_iter = iter(token_list)

    def get_state(self, old_state, trans_char):
        if trans_char in digits+letters+'?':
            return {
                0: {k_trans1or4: 1 if k_trans1or4 in digits else 4 for k_trans1or4 in digits+letters},
                1: {k_trans1: 1 for k_trans1 in digits},
                2: {k_trans1: 1 for k_trans1 in digits},
                4: {k_trans4or16: 4 if k_trans4or16 is not '?' else 16 for k_trans4or16 in digits+letters+'?'},
                #Fill out
				7: {k_trans8or9: 8 if k_trans8or9 is 'T' else 9 for k_trans8or9 in digits+letters+'#'}
            }[old_state][trans_char]
        if old_state is 0:
            return {
                #Fill out
				'-' : 2,
				'+' : 3,
				'(' : 5,
				')' : 6,
				'#' : 7,
				'*' : 10,
				'/' : 11,
				'<' : 12,
				'>' : 13,
				'=' : 14,
				"'" : 15
            }[trans_char]


    def next_token(self):
        state_old = 0
        temp_token=next(self.token_iter, None)
        """:type :str"""
        if temp_token is None: return None
        for temp_char in temp_token:
            #Fill out
			state_old = self.get_state(state_old, temp_char)
        if check_keyword(temp_token):
            result = Token(_get_keyword_type(temp_token), temp_token)
        else:
            result = Token(state_old, temp_token)
        return result

    def tokenize(self):
        tokens=[]
        while True:
            #Fill out
		tmp = self.next_token()
		if tmp is None : break
		tokens.append(tmp)	
        return tokens

def Test_CuteScanner():
    test_cute = CuteScanner("Test car + ' - * #T ( ) eq?")
    test_tokens=test_cute.tokenize()

    print test_tokens
    for token_i in test_tokens:
        print token_i
    print "end"

Test_CuteScanner()
