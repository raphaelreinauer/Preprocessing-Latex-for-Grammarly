import random
import re

text_file = open("Text_for_grammarly.txt", "r")
text = text_file.read()

def random_char():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

output_string = ''.join([part if ind%2==0 else random_char()  for ind,part in enumerate(text.split('$'))])
output_string = re.sub('\\x07utoref','Theorem ',output_string)
output_string = ''.join([part if ind%2==0 else random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  for ind,part in enumerate(re.split('\{|\}', output_string) )])
print(output_string)
