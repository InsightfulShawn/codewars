
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
  num_order_sorted = sorted(num_order)
  sorted_sentence = [broken_sentence[i] for i in num_order]
  

  sorted_sentence = " ".join(sorted_sentence)

  return (broken_sentence,num_order,sorted_sentence)

print(order('g3ood 4of the2 pe6ople th5e Fo1r'))


 