# import sys
#
#
# def main():
#     if len(sys.argv) > 1:
#         print("Hello there", "How are you", sys.argv[1])
#     else:
#         print("Error: No argument provided!")
#
#
# if __name__ == '__main__':
#     main()

# pi = 3.14
# print("The value of pie is " + str(pi))

# raw = r'this\t\n and that'
# print(raw)
#
# multi = """It was a good.
# It was better.
# """
# print(multi)

# s = " Hey how are you?"
# b = "good"
# print(s)
# print(s.strip(), b)
# print(s.isspace())
# print(s.startswith(' Hey'), s.endswith('?'))
# print(s.find('y', 3))
# print(s.replace("Hey", "Hello"))
# a = s.replace("Hey", "Hello")
# print(a.split())
# print(s.split('delim'))
# print(s[:6])
# print(s[1:])
# print(s[:-1])

# value = 2.35654674567
# print(f'{value:.2f}')

# car = {
#     'tires': 4,
#     'doors': 2
# }
# print(f'car = {car}')

adress_book = [{
    'name': 'N.X.',
    'addr': '15 Jones St',
    'bonus': 70
    },
    {
    'name': 'J.P.',
    'addr': '1005 5th St',
    'bonus': 400
    },
    {
    'name': 'A.P.',
    'addr': '1005 5th St',
    'bonus': 400
    },
]

for person in adress_book:
    print(f"{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}")
