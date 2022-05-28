from stringcolor import *
print(cs('Hello, Word!','#7597E1').bold())
a = 'Hello, World!'
b = 'World'
print(cs(f'{a}','#DB4D48').underline().bold())

print(cs(f'{a}','#7597E1').bold()+ cs(f' {b}','#DB4D48').underline())