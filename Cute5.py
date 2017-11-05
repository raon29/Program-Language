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
    DEFINE=16
    LAMBDA=17
    COND=18
    QUOTE=19
    NOT=20
    CAR=21
    CDR=22
    CONS=23
    ATOM_Q=24
    NULL_Q=25
    EQ_Q=26

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
def is_type_keyword(token):
    if token.type >15 and token.type<26:
        return True
    return False




def _get_keyword_type(token):
    return {
        'define':CuteType.DEFINE,
        'lambda':CuteType.LAMBDA,
        'cond':CuteType.COND,
        'quote':CuteType.QUOTE,
        'not':CuteType.NOT,
        'car':CuteType.CAR,
        'cdr':CuteType.CDR,
        'cons':CuteType.CONS,
        'atom?':CuteType.ATOM_Q,
        'null?':CuteType.NULL_Q,
        'eq?':CuteType.EQ_Q
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

    transM={}
    def __init__(self, source):
        """
        :type source:str
        :param source:
        :return:
        """
        source=source.strip()
        token_list=source.split(" ")
        self.token_iter=iter(token_list)


    def get_state(self, old_state, trans_char):
        if trans_char in digits+letters+'?':
            return {
                0: {k: 1 if k in digits else 4 for k in digits+letters},
                1: {k: 1 for k in digits},
                2: {k: 1 for k in digits},
                3: {k: 1 for k in digits},
                4: {k: 4 if k is not '?' else 16 for k in digits+letters+'?'},
                7: {k: 8 if k is 'T' else 9 for k in ['T', 'F']}
            }[old_state][trans_char]
        if old_state is 0:
            return {
                '(': 5, ')': 6,
                '+': 3, '-': 2,
                '*': 10, '/': 11,
                '<': 12, '=': 14,
                '>': 13, "`": 15,
                '#': 7, "'":19
            }[trans_char]


    def next_token(self):
        state_old=0
        temp_token=next(self.token_iter, None)
        """:type :str"""
        if temp_token is None : return None
        for temp_char in temp_token:
            state_old=self.get_state(state_old, temp_char)

        if check_keyword(temp_token):
            result = Token(_get_keyword_type(temp_token), temp_token)
        else:
            result=Token(state_old, temp_token)
        return result

    def tokenize(self):
        tokens=[]
        while True:
            t=self.next_token()
            if t is None :break
            tokens.append(t)
        return tokens



class TokenType():
    INT=1
    ID=4
    MINUS=2
    PLUS=3
    LIST=5
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

NODETYPE_NAMES = dict((eval(attr, globals(), TokenType.__dict__), attr) for attr in dir(TokenType()) if not callable(attr) and not attr.startswith("__"))

class Node (object):

    def __init__(self, type, value=None):
        self.next  = None
        self.value = value
        self.type  = type



    def set_last_next(self, next_node):
        if self.next is not None:
            self.next.set_last_next(next_node)

        else : self.next=next_node

    def __str__(self):
        result = ""

        if   self.type is TokenType.ID or self.type is TokenType.INT:
            result = "["+self.value+"]"
        elif self.type is TokenType.LIST :
            if self.value.type is TokenType.QUOTE: result = str(self.value)
            else : result = "("+str(self.value)+")"
        elif self.type is TokenType.QUOTE:
            result = "\'" + str(self.value)
        else:
            result = "["+NODETYPE_NAMES[self.type]+"]"
	
        if self.next is None : return result
        return result + str(self.next)
        #fill out

class BasicPaser(object):

    def __init__(self, token_list):
        """
        :type token_list:list
        :param token_list:
        :return:
        """
        self.token_iter=iter(token_list)

    def _get_next_token(self):
        """
        :rtype: Token
        :return:
        """
        next_token=next(self.token_iter, None)
        if next_token is None: return None
        return next_token

    def parse_expr(self):
        """
        :rtype : Node
        :return:
        """
        token =self._get_next_token()
        """:type :Token"""
        if token==None: return None
        result = self._create_node(token)
        return result


    def _create_node(self, token):
        if token is None: return None

        if   token.type is CuteType.INT:     return Node(TokenType.INT,  token.lexeme)
        elif token.type is CuteType.ID:      return Node(TokenType.ID,   token.lexeme)
        elif token.type is CuteType.L_PAREN: return Node(TokenType.LIST, self._parse_expr_list())
        elif token.type is CuteType.R_PAREN: return None
        elif token.type is CuteType.TRUE:   return Node(TokenType.TRUE,None)
        elif token.type is CuteType.FALSE:  return Node(TokenType.FALSE,None)
        elif token.type is CuteType.PLUS:   return Node(TokenType.PLUS,None)
        elif token.type is CuteType.MINUS:  return Node(TokenType.MINUS,None)
        elif token.type is CuteType.TIMES:  return Node(TokenType.TIMES,None) 
        elif token.type is CuteType.LT:     return Node(TokenType.LT,None)
        elif token.type is CuteType.DIV:    return Node(TokenType.DIV,None)
        elif token.type is CuteType.GT:     return Node(TokenType.GT,None)
        elif token.type is CuteType.EQ:     return Node(TokenType.EQ,None)
        elif token.type is CuteType.DEFINE: return Node(TokenType.DEFINE,None)
        elif token.type is CuteType.LAMBDA: return Node(TokenType.LAMBDA,None)
        elif token.type is CuteType.COND:   return Node(TokenType.COND,None)
        elif token.type is CuteType.NOT:    return Node(TokenType.NOT,None)
        elif token.type is CuteType.CAR:    return Node(TokenType.CAR,None)
        elif token.type is CuteType.CDR:    return Node(TokenType.CDR,None)
        elif token.type is CuteType.CONS:   return Node(TokenType.CONS,None)
        elif token.type is CuteType.EQ_Q:   return Node(TokenType.EQ_Q,None)
        elif token.type is CuteType.ATOM_Q: return Node(TokenType.ATOM_Q,None)
        elif token.type is CuteType.NULL_Q: return Node(TokenType.NULL_Q,None)
        elif token.type is CuteType.QUOTE : return Node(TokenType.QUOTE, self._parse_expr_list())
        else:
            return None

    def _parse_expr_list(self):
        head = self.parse_expr()
        """:type :Node"""
        if head is not None:
            head.next = self._parse_expr_list()
        return head

def Test_BasicPaser():
    test_cute = CuteScanner("( + ( + 2 3 ) ( quote ( + 4 5 ) ) )")
    test_tokens=test_cute.tokenize()
    print test_tokens
    test_basic_paser = BasicPaser(test_tokens)
    node = test_basic_paser.parse_expr()

    print node

Test_BasicPaser()
