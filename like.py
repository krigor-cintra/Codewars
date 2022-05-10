"""You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item."""
def likes(names):
  a=len(names)
  if a == 0:
    return "no one likes this"
  elif a==1:
    return f"{names[0]} likes this"
  elif a==2:
    return f"{names[0]} and {names[1]} like this"
  elif a == 3:
    return f"{names[0]}, {names[1]} and {names[3]} like this"
  elif a >3:
    return f"{names[0]}, {names[1]} and {a-2} others like this"