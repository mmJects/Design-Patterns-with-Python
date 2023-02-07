class Written:
    def __init__(self,text):
        self._text = text
    
    def render(self):
        return self._text

class bold(Written):
    def __init__(self,wrap):
        self._wrap = wrap

    def render(self):
        return f"<b>{self._wrap.render()}</b>"

class Italic(Written):
    def __init__(self,wrap):
        self._wrap = wrap

    def render(self):
        return f"<i>{self._wrap.render()}</i>"

if __name__ == "__main__":
    before = Written("hello")
    after = Italic(bold(before))

    print("Before",before.render())
    print("After",after.render())
