# montage
Invoke SelfControl if productivity is low.

This script reads a cookie file for an authenticated session of RescueTime, scrapes the current productivity value, and invokes [SelfControl](http://selfcontrolapp.com) with the default settings for the specified user if the current productivity score is below the specified threshold.
