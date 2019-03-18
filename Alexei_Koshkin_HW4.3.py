def login_required(fn):
    def login():
        return 'aaa' + fn() + 'bbb'
    return login

@login_required
def hello():
    return 'hello'

print(hello())