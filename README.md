README.md 
max8radio: Max/MSP SDR project and tutorials
Feb 6, 2021
current documentation: https://reactivemusic.net/?p=19995
Legacy docs: http://zerokidz.com/radio
local: max8radio

#### email: tkzic@megalink.net

----------------------------------

This is the new home of the Max/MSP software defined radio project.

Currently it contains old files and new work in progress. We will write new instructions here as soon as something is ready to go.

The new approach will be to remove the device handling code from Max. Instead providing device interfaces from existing device libraries, like soapy-sdr (In CubicSDR), hamlib, gnu-radio, etc.,  The Max portion of the project will read IQ files, perform DSP, and other magic.

The first platform will be Max8 in Mac OS Catalina

For progress reports and fun things to try check here: https://reactivemusic.net/?p=19995 - Or look at any recent posts about radio at that site.

New Prototype using CubicSDR, max8sdr1.maxpat, and py3rigctl2.py  - https://reactivemusic.net/?p=20029

So far, CubicSDR is the only stable program that will feed I/Q data into Max - with frequency control for a wide range of devices. Still looking for a more compact solution but its eluded us to this point.

-------------------------------------------------------------------------------------------

If you are looking for old things, the maxradio repo still exists on github - in a permanent state of decline https://github.com/tkzic/maxradio

-------------------------------------------------------------------------------------------
Problems? Questions? Ideas? Interested in developing?  Send email to tkzic@megalink.com

#### Tom Zicarelli, KA1IS
--------------------------------------------------------------------------------------------
This project was derived from the works of the following developers.

* Katja Vetter, DSP with complex numbers in Max and Pd
* Kazunori Miura, JA7TDO - hardware and software design of soft66lc2
* Thomas Horsten - Linux soft66add control software
* Thomas Robin-Couerrier - ppc Max external software and library conversion & testing
* Howard Long, G6LVB - hardware and software design of FUNCube
* Alexandru Csete, OZ9AEC - QTHid FUNCube control software
* Mario Lorenz, DL5MLO - FUNCube control software
* David Pello, EA1IDZ - Linux FUNCube command line control software.
* Hannah Zicarelli, KB1URI - design, technical advice, and testing.

and many many more developers whose work I have learned from.

Thank you!





 # max8radio
