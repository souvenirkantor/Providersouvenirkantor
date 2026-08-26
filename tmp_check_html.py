from html.parser import HTMLParser
from pathlib import Path

path = Path(r'c:\Provider Kantor\CorporateGifts ID\blog\jenis-souvenir-ramah-lingkungan.html')
text = path.read_text(encoding='utf-8')

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
    def handle_startendtag(self, tag, attrs):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        while self.stack and self.stack[-1] != tag:
            self.errors.append('Unmatched closing tag </' + self.stack.pop() + '> before </' + tag + '>')
        if self.stack:
            self.stack.pop()
        else:
            self.errors.append('Closing tag </' + tag + '> without matching opening')

parser = P()
parser.feed(text)
while parser.stack:
    parser.errors.append('Unclosed tag <' + parser.stack.pop() + '>')

print('\n'.join(parser.errors[:100]))
