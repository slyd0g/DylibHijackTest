# DylibHijackTest

![inspect.py](https://raw.githubusercontent.com/slyd0g/DylibHijackTest/master/example.png)

## Requirements
- Install Python3 requirements: ```pip3 install -r requirements.txt```
- Compile dylib from source because don't trust compiled things from GitHub: ```gcc -dynamiclib DylibHijackTest.c -o DylibHijackTest.dylib```

## How it Works
> :warning: **This will spawn many processes on your machine, run this in a VM**: Be very careful here!
- inject.py
  - Recursively crawl a folder and search for Mach-O binaries with `MH_EXECUTE` header
  - Start the Mach-O binary with `DYLD_INSERT_LIBRARIES` environment variable pointed at our malicious dylib
  - Redirect all stdout to a file and stderr to /dev/null
- inspect.py
  - Take text file output from `inject.py` to see what Mach-Os ary injectable and use `codesign` to check for useful entitlements
  - Party!!!

## Usage
```
$ python3 inject.py /Applications/iMovie.app /Users/slyd0g/DylibHijackTest.dylib > imovie.txt 2> /dev/null
$ python3 inspect.py /Users/slyd0g/Projects/DylibHijackTest/imovie.txt
```
