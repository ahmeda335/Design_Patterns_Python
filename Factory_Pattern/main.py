"""
This is the client server
"""

from factory import Factory

vechile = input("Enter the vechile you want: ").lower()
vechile = Factory().get_vechile(vechile)
try:
    print(vechile.get_specs())
except:
    print(vechile)