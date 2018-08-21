# delta-generator
Python utility to generate vertical delta-loop antenna nec files.
In future may be more functional. Created in studying purposes.

Future goal, is more antenna types, antenna optimization and may be simple GUI.
Welcome to commit, advise and suggest.

Usage is simple, you can check it with -h or --help

```sh
$ python3 delta.py -h
    usage: delta.py [-h] -f FREQ [-m MAST] -o OUT [-a ANGLE] [--shorten SHORTEN]

    Buld deltas .nec files.

    optional arguments:
        -h, --help            show this help message and exit
        -f FREQ, --freq FREQ  Destination freq to build antenna in MHz
        -m MAST, --mast MAST  Top point of antenna, mast hight in meters
        -o OUT, --out OUT     Filename to output .nec file
        -a ANGLE, --angle ANGLE
                        Top wire angle in degs
        --shorten SHORTEN     coefficent of wire shortening
```
Now it is returns only coordinates of triangle vertexes.
