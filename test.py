from tinygrad import Device

assert Device.DEFAULT == "METAL"

from tinygrad.tensor import Tensor, dtypes

t = Tensor([1, 2, 3, 4, 5])
assert t.device == Device.DEFAULT
assert t.shape == (5,)
assert t.dtype == dtypes.int

print(t)
print(t.uop)
t.realize()
print(t.uop)
