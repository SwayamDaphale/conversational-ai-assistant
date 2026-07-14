# cuda_test.py

import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

x = torch.randn(5, device="cuda")
print(x)
