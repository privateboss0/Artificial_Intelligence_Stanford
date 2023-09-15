import collections

def extractWordFeatures(x):
  """Extract word features for a string x. Words are delimited by whitespace characters only.

  Args:
    x: A string.

  Returns:
    A dict representing the feature vector ϕ(x).
  """

  wordDict = collections.defaultdict(float)
  for word in x.split():
    wordDict[word] += 1
  return wordDict

print(extractWordFeatures("I am what I am"))