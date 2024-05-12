package main

type Lexer struct {
	Input        []rune
	char         rune
	position     int
	readPosition int
	line         int
}

func New(input string) *Lexer {
	l := &Lexer{Input: []rune(input)}
	l.readChar()
	return l
}

func (l *Lexer) readChar() {
	if l.readPosition >= len(l.Input) {
		l.char = 0
	} else {
		l.char = l.Input[l.readPosition]
	}

	l.position = l.readPosition
	l.readPosition++
}

func (l *Lexer) NextToken() Token {
	var t Token

	l.skipWhitespace()

	switch l.char {
	case '{':
		t = newToken(LeftBrace, l.line, l.position, l.position+1, l.char)
	case '}':
		t = newToken(RightBrace, l.line, l.position, l.position+1, l.char)
	case '[':
		t = newToken(LeftBracket, l.line, l.position, l.position+1, l.char)
	case ']':
		t = newToken(RightBrace, l.line, l.position, l.position+1, l.char)
	case ':':
		t = newToken(Colon, l.line, l.position, l.position+1, l.char)
	case ',':
		t = newToken(Comma, l.line, l.position, l.position+1, l.char)
	case '"':
		t.Type = String
		t.Literal = l.readString()
		t.Line = l.line
		t.Start = l.position
		t.End = l.position + 1
	case 0:
		t.Literal = ""
		t.Type = EOF
		t.Line = l.line
	default:
		if isLetter(l.char) {
			t.Start = l.position
			ident := l.readIdentifier()
			t.Literal = ident
			t.Line = l.line
			t.End = l.position

			tokenType, err := LookupIdentifier(ident)
			if err != nil {
				t.Type = Illegal
				return t
			}
			t.Type = tokenType
			t.End = l.position
			return t
		} else if isNumber(l.char) {
			t.Start = l.position
			t.Literal = l.readNumber()
			t.Type = Number
			t.Line = l.line
			t.End = l.position
			return t
		}
	}

	l.readChar()
	return t
}

func (l *Lexer) skipWhitespace() {
	for l.char == ' ' || l.char == '\t' || l.char == '\n' || l.char == '\r' {
		if l.char == '\n' {
			l.line++
		}
		l.readChar()
	}
}

func newToken(tokenType Type, line, start, end int, char ...rune) Token {
	return Token{
		Type:    tokenType,
		Literal: string(char),
		Line:    line,
		Start:   start,
		End:     end,
	}
}

func (l *Lexer) readString() string {
	position := l.position + 1
	for {
		prevChar := l.char
		l.readChar()
		if (l.char == '"' && prevChar != '\\') || l.char == 0 {
			break
		}
	}
	return string(l.Input[position:l.position])
}

func isLetter(char rune) bool {
	return 'a' <= char && char <= 'z'
}

func (l *Lexer) readIdentifier() string {
	position := l.position
	for isLetter(l.char) {
		l.readChar()
	}

	return string(l.Input[position:l.position])
}

func isNumber(char rune) bool {
	return char >= '0' && char <= '9' || char == '.' || char == '-'
}

func (l *Lexer) readNumber() string {
	position := l.position

	for isNumber(l.char) {
		l.readChar()
	}

	return string(l.Input[position:l.position])
}
