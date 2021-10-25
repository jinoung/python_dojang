def html_tag(tag):
    def real_deco(func):
        def wrapper():
            return '<{0}>{1}</{0}>'.format(tag, func())
        return wrapper
    return real_deco

a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())
