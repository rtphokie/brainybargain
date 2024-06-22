# brainybargain

Shows the latest Amazon deals listed on brainybargain.com showing the (approximate) final price and noting
those products that are no longer available.

This information should be used as a guide to help you find the deals you might be most interested in.
Product and coupon code availabilty as well as prices frequently change. 

## Installation

* pip install -r requirements.txt

## Usage

```
 ./brainybargain.py -h
usage: brainybargain.py [-h] [-d DAYSAGO] [-s] [-p PERCENT]

options:
  -h, --help            show this help message and exit
  -d DAYSAGO, --daysago DAYSAGO
                        days back to look (default: 0, today only)
  -s, --skipchecks      don't check price or availability, speeds up output significantly
  -p PERCENT, --percent PERCENT
                        minimum percentage off (default: 50)

```


## Example Output
```
date         disc link code         price description
June 17      80%  ---- ----     $  27 Outdoor Shade Cover
June 16      83%  ---- ----     $   5 iPhone Charger
June 16      80%  ---- ----     $  50 Car Vacuum Cleaner High Power Cordless
June 15      80%  ---- ----     $  60 Projector with WiFi and Bluetooth
June 13      80%  ---- ----           E̶l̶e̶c̶t̶r̶i̶c̶ ̶T̶o̶o̶t̶h̶b̶r̶u̶s̶h̶,̶ ̶E̶l̶e̶c̶t̶r̶i̶c̶ ̶T̶o̶o̶t̶h̶b̶r̶u̶s̶h̶ ̶w̶i̶t̶h̶ ̶8̶ ̶B̶r̶u̶s̶h̶ ̶H̶e̶a̶d̶s̶,̶ ̶S̶m̶a̶r̶t̶ ̶6̶-̶S̶p̶e̶e̶d̶ ̶T̶i̶m̶e̶r̶ ̶E̶l̶e̶c̶t̶r̶i̶c̶ ̶T̶o̶o̶t̶h̶b̶r̶u̶s̶h̶ ̶I̶P̶X̶7 (unavailable)
June 11      80%  ---- ----     $   4 Fast Charging Lightning Cable
June 11      80%  ---- ----     $  30 Waterproof Bluetooth Speaker with HD Sound
June 11      83%  ---- ----     $ 149 High-Pressure Showerhead with Water Filter System
June 10      80%  ---- ----     $  50 Car Vacuum Cleaner High Power Cordless 
```
