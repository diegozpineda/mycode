#!/usr/bin/env python3

import yaml

def main():
    with open("myYAML.yml", "r") as yf:
        #SafeLoader- Recommended for untrusted input. This setting only loads a subset of the YAML language.
        #FullLoader- Used for more trusted input. Imposes limitation by avoiding arbitrary code execution. This is the default.
        #Loader- Unsafe. But has the full power

        pyyammy = yaml.load(yf, Loader=yaml.FullLoader)
    print(pyyammy)

if __name__ == "__main__":
    main()