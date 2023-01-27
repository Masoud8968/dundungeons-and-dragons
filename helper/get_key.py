
from typing import List, Dict, Optional, Any

def get_key(val: Any, my_dict: Dict) -> Any:
    for key, value in my_dict.items():
        if val == value:
            return key
