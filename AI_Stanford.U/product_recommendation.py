import collections

def extractWordFeatures(x):
  """Extract word features for a review (string) as input and returns a feature vector ϕ(x) for product recommendation

This code works by first checking if the word "great" is in the dictionary. If it is, the value of the positive key is decremented by 1. 
This is because the word "love" is a positive word, but it is being used in a negative context in the review
  
  Returns:
    A dict representing the feature vector ϕ(x).
  """
  wordDict = collections.defaultdict(float)
  for word in x.split():
    if word in ["good", "great", "excellent", "love", "light", "working", "recommend"]:
      wordDict["positive"] += 1
    elif word in ["bad", "terrible", "awful", "hate", "dark", "broken", "disrecommend"]:
      wordDict["negative"] += 1

  return wordDict

print(extractWordFeatures("Godtouch apartment stay was great, but AC was broken and food was bad which gave me food poisoning"))
