def sort(width, height, length, mass):
  volume = width * height * length
  str1 = "default"
  str2 = "default"
  if volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150:
    str1 = "bulky"
  if mass >= 20:
    str2 = "heavy"
  if str1 == "bulky" and str2 == "heavy":
    return "REJECTED"
  elif str1 != "bulky" and str2 != "heavy":
    return "STANDARD"
  else:
    return "SPECIAL"

if __name__ == "__main__":
  print(sort(100, 100, 100, 10))  # bulky → SPECIAL
  print(sort(10, 10, 10, 25))     # heavy → SPECIAL
  print(sort(200, 200, 200, 30))  # both → REJECTED
  print(sort(20, 20, 20, 5))      # neither → STANDARD
