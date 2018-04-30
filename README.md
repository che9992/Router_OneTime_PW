# Router_OneTime_PW

I made it based on the router 'IPTIME' .

it'll connect and operate using DDNS.

you can get easily the data need for the 'control.py' using Chrome Developer Tools.

it was confirmed on May 1 2018 that it can be used for all kinds of 'IPTIME' router.

i think you can use it with other routers like ASUS if you modify the code and data a bit

Thanks.

### my environment
- OS X, Windows 10
- Python 3.6.4 with Pycharm





### version 20180425
  - fixed more easily
  - control.py 
  - can change 'SSID' , 'Password'
  - add defulat 'time' for sleep(10mins) , default 'SSID'
  
  - check_DDNS.py
  - add default 'remote_port'(80)
  
  - ShowProgress.py
  - count until wi-fi turn off 

### datas examply for control.py to Router IPTIME
``` python


data = {'tmenu': '',
        'smenu': '',
        'wlmode': '',
        'action': '',
        'sidx': '',
        'uiidx': '',
        'run': '',
        'ssid': '',    
        'wpapsk':''
        }
```   
  
