import time
import math

def time_to_complete_actual_run(mile_time, distance):
  """
  Calculates the time it takes to complete a run of a given distance,
  assuming that you run 1 mile every `mile_time` minutes.

  Args:
    mile_time: The time it takes to run 1 mile in minutes.
    distance: The distance of the run in miles.

  Returns:
    The time it takes to complete the run in hours, minutes, and seconds.
  """
  total_seconds = math.floor(distance * mile_time * 60)
  hours = total_seconds // 3600
  minutes = total_seconds // 60 % 60
  seconds = total_seconds % 60
  return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


print(time_to_complete_actual_run(9.02, 26.2))