
def order(sentence):
  # code here
  broken_sentence = sentence.split() # split string into a list
  num_order = [] # create an empty list for string arrangement
  sorted_sentence = []


  for item in broken_sentence: # loop through each string in the broken_sentence list
  	for char in item: # loop through each character of each string
  		if char.isdigit():
  			num_order.append(char)

  num_order = [(int(x) - 1) for x in num_order]
  sorted_sentence = [broken_sentence[i] for i in num_order]





  return (sorted_sentence)

print(order('is2 Thi1s T4est 3a'))


