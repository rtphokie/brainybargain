# brainybargain

Shows the latest Amazon deals listed on brainybargain.com showing the (approximate) final price and noting
those products that are no longer available.

This information should be used as a guide to help you find the deals you might be most interested in.
Product and coupon code availability as well as prices frequently change. No warranty is offered or implied.

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
date         disc link                          code         price description
June 16      83%  https://amzlink.to/azGPQYX8O6 GPQYX8O6     $   5 iPhone Charger
June 16      80%  https://amzlink.to/azJIJOQULO B58M319U     $  50 Car Vacuum Cleaner High Power Cordless
June 13      80%  https://amzlink.to/azTE73IBGB                    E̶l̶e̶c̶t̶r̶i̶c̶ ̶T̶o̶o̶t̶h̶b̶r̶u̶s̶h̶,̶ ̶E̶l̶e̶c̶t̶r̶i̶c̶ ̶T̶o̶o̶t̶h̶b̶r̶u̶s̶h̶ ̶w̶i̶t̶h̶ ̶8̶ ̶B̶r̶u̶s̶h̶ ̶H̶e̶a̶d̶s̶,̶ ̶S̶m̶a̶r̶t̶ ̶6̶-̶S̶p̶e̶e̶d̶ ̶T̶i̶m̶e̶r̶ ̶E̶l̶e̶c̶t̶r̶i̶c̶ ̶T̶o̶o̶t̶h̶b̶r̶u̶s̶h̶ ̶I̶P̶X̶7 (unavailable)
```
note: these are just random examples that will go nowhere
