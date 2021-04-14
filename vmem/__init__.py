name = "vmem"

import os
if os.name == 'nt':
    from .windows import virtual_memory
else:
    from .posix import virtual_memory