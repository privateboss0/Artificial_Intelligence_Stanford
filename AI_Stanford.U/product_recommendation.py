import collections

def extractWordFeatures(x):
  """Extract word features for a review (string) as input and returns a feature vector ϕ(x) for product recommendation (you should represent the vector ϕ(x) as a dict in Python).

  Args:
    x: A string.

  Returns:
    A dict representing the feature vector ϕ(x).
  """

  wordDict = collections.defaultdict(float)
  for word in x.split():
    if word in ["good", "great", "excellent", "love", "light", "working", "recommend"]:
      wordDict["positive"] += 1
    elif word in ["bad", "terrible", "awful", "hate", "dark", "broken", "disrecommend"]:
      wordDict["negative"] += 1
  if "love" in wordDict:
    wordDict["positive"] -= 1
  return wordDict

print(extractWordFeatures("Godtouch apartment stay was love, but AC was broken and food was bad which gave me food poisoning"))