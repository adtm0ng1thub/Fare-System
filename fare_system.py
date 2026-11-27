# CS3 Pair Assessment: Fare System
# Authors: (write your full names here)
# Section: 9 - Potassium

  class Vehicle(ABC):
  """Abstract base class for every public vehicle."""
  def __init__(self, plate_number, capacity):
    self.__plate_number = plate_number
    self.__capacity = capacity
  
  def get_plate_number(self):
    return self.__plate_number

  def set_plate_number(self, plate_number):
    self.__plate_number = plate_number
  def get_capacity(self):
    return self.__capacity

  def set_capacity(self,capacity):
    if capacity<=0:
      print("Invalid capacity)
    else:
      self.__capacity=capacity
  # TODO (Part 2): write get_capacity() and set_capacity(capacity).
  # set_capacity only accepts a whole number greater than 0.
  # Otherwise, print "Invalid capacity." and keep the old value.

  @abstractmethod
    def compute_fare(self, distance_km):
      pass
  @abstractmethod
    def describe(self):
      pass
# ===== Jeepney class (Developer A) =====

# ===== Tricycle class (Developer B) =====

# ===== Test code (Part 6 only) =====
