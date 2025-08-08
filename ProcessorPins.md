IO Connections on the PacSat AFSK processor
===========================================

These are the pins on the TMS570 processor, where they go, what they
do and some notes at the end with some more details.

The "G" column shows the GPIO usage and capability.  The first letter
is how the GPIO is used: I for input, O for output, B for
bidirectional, blank if not used as a GPIO, and ? if the function is
not known (the PC104 pins).  The second letter is U for pullup by
default and D for pulldown by default or blank if the pin cannot be
used as a GPIO.

|Pin3	|CPU Pin Name			|Schematic Name			|G |Description |
|----	|------------			|--------------			|--|-----------
|1		|GIOB[3]				|GIOA\_3				|?D|PC104 Pin 14 |
|2		|GIOA[0]				|FCODE\_STROBE			|?D|PC104 Pin 56 |
|3		|MIBSPI3NCS[3]			|I2C\_SCL				| U|RTC control (MAX31331TETB+) |
|4		|MIBSPI3NCS[2]			|I2C\_SDA				| U|RTC control (MAX31331TETB+) |
|5		|GIOA[1]				|AX5043\_IRQ\_RX1		|ID|Interrupt from AX5043 RX1 |
|6		|N2HET1[11]				|						| D|free gpio |
|7		|FLTP1					|						|  | |
|8		|FLTP2					|						|  | |
|9		|GIOA[2]				|GPIOA_2				|?D|PC104 Pin 15 |
|10		|VCCIO					|						|  | |
|11		|VSS					|						|  | |
|12		|CAN3RX					|CAN\_A\_RX				| U|CAN bus transceiver |
|13		|CAN3TX					|CAN\_A\_TX				| U|CAN bus transceiver |
|14		|GIOA[5]				|AX5043\_IRQ\_RX4		|ID|Interrupt from AX5043 RX4 |
|15		|N2HET1[22]				|ALERT\_SIGNAL			|?D|PC104 Pin 49 |
|16		|GIOA[6]				|GIOA\_6				|?D|PC104 Pin 45 |
|17		|VCC					|						|  | |
|18		|OSCIN					|						|  | |
|19		|Kelvin\_GND			|						|  | |
|20		|OSCOUT					|						|  | |
|21		|VSS					|						|  | |
|22		|GIOA[7]				|AX5043\_IRQ\_RX3		|ID|Interrupt from AX5043 RX3 |
|23		|N2HET1[01]				|						|OD|Yellow LED |
|24		|N2HET1[03]				|AX5043\_EN\_RX4\_N		|OD|Power enable for AX5043 RX 4 |
|25		|N2HET1[0]				|						|OD|Red LED |
|26		|VCCIO					|						|  | |
|27		|VSS					|						|  | |
|28		|VSS					|						|  | |
|29		|VCC					|						|  | |
|30		|N2HET1[02]				|						|OD|Green LED |
|31		|N2HET1[05]				|LNA\_ENABLE			|OD|Used to enable the LNA |
|32		|MIBSPI5NCS[0]			|						| U|free gpio (Save for extra SPI if possible) |
|33		|N2HET1[07]				|AX5043\_EN\_RX3\_N		|OD|Power enable for AX5043 RX 3 |
|34		|TEST					|					    |  | |
|35		|N2HET1[09]				|AX5043\_EN\_RX2\_N		|OD|Power enable for AX5043 RX 2 |
|36		|N2HET1[4]				|AX5043\_EN\_RX1\_N		|OD|Power enable for AX5043 RX 1 |
||||||
|37		|MIBSPI3NCS[1]			|MRAM\_NCS3				|OU| |
|38		|N2HET1[06]				|UART\_RX1				| D|PC104 pin 92 |
|39		|N2HET1[13]				|UART\_TX1				| D|PC104 pin 88 |
|40		|MIBSPI1NCS[2]			|MRAM\_NCS2				|OU| |
|41		|N2HET1[15]				|FCODE\_D0				|?D|PC104 pin 64 |
|42		|VCCIO					|						|  | |
|43		|VSS					|						|  | |
|44		|VSS					|						|  | |
|45		|VCC					|						|  | |
|46		|nPORRST				|						|  | |
|47		|VSS					|						|  | |
|48		|VCC					|						|  | |
|49		|VCC					|						|  | |
|50		|VSS					|						|  | |
|51		|MIBSPI3SOMI			|MRAM\_MISO				| U| |
|52		|MIBSPI3SIMO			|MRAM\_MOSI				| U| |
|53		|MIBSPI3CLK				|MRAM\_CLK				| U| |
|54		|MIBSPI3NENA			|MRAM\_NCS1				|OU| |
|55		|MIBSPI3NCS[0]			|MRAM\_NCS0				|OU| |
|56		|VSS					|						|  | |
|57		|VCC					|						|  | |
|58		|AD1IN[16] / AD2IN[0]	|\*						|  |Thermsistor near the processor |
|59		|AD1IN[17] / AD2IN[01]	|						|  |free adc |
|60		|AD1IN[0]				|						|  |free adc |
|61		|AD1IN[07]				|PWR\_FLAG\_AX5043		|  |Power flag from the AX5043 current limiter |
|62		|AD1IN[18] / AD2IN[02]	|						|  |free adc |
|63		|AD1IN[19] / AD2IN[03]	|						|  |free adc |
|64		|AD1IN[20] / AD2IN[04]	|VER\_BIT0				|  |Board version number bit 0 |
|65		|AD1IN[21] / AD2IN[05]	|VER\_BIT1				|  |Board version number bit 1 |
|66		|ADREFHI				|						|  | |
|67		|ADREFLO				|						|  | |
|68		|VSSAD					|						|  | |
|69		|VCCAD					|						|  | |
|70		|AD1IN[09] / AD2IN[09]	|						|  |free adc |
|71		|AD1IN[01]				|						|  |free adc |
|72		|AD1IN[10] / AD2IN[10]	|						|  |free adc |
||||||
|73		|AD1IN[02]				|REV\_PWR				|  |\*Reverse RF TX Power |
|74		|AD1IN[03]				|FWD\_PWR				|  |\*Forward RF TX Power |
|75		|AD1IN[11] / AD2IN[11]	|PWR\_FLAG\_LNA			|  |Power flag from the LNA current limiter |
|76		|AD1IN[04]				|PWR\_FLAG\_SSPA		|  |Power flag from the PA current limiter |
|77		|AD1IN[12] / AD2IN[12]	|						|  |+5V power measure, linear from 0-2.5V |
|78		|AD1IN[05]				|						|  |free adc |
|79		|AD1IN[13] / AD2IN[13]	|						|  |+1.2V power measure, 0-1.2V |
|80		|AD1IN[06]				|						|  |+3.3V power measure, 0-1.65V |
|81		|AD1IN[22] / AD2IN[06]	|						|  |free adc |
|82		|AD1IN[14] / AD2IN[14]	|						|  | Board version number bit 2 |
|83		|AD1IN[08] / AD2IN[08]	|\*POWER\_TEMP			|  |Thermsistor in power conversion section |
|84		|AD1IN[23] / AD2IN[07]	|\*PA\_TEMP				|  |Thermsistor near the PA |
|85		|AD1IN[15] / AD2IN[15]	|						|  |Board version number bit 3 |
|86		|AD1EVT					|						|  | |
|87		|VCC					|						|  | |
|88		|VSS					|						|  | |
|89		|CAN1TX					|AX5043\_EN\_TX\_N		|OU|Power enable for AX5043 TX |
|90		|CAN1RX					|AX5043\_SEL1\_N		|OU|SPI chip select for AX5043 RX1 |
|91		|N2HET1[24]				|AX5043\_SEL2\_N		|OD|SPI chip select for AX5043 RX2 |
|92		|N2HET1[26]				|AX5043\_SEL3\_N		|OD|SPI chip select for AX5043 RX3 |
|93		|MIBSPI1SIMO			|AX5043\_MOSI			| U|SPI MOSI for all AX5043s |
|94		|MIBSPI1SOMI			|AX5043\_SIMO			| U|SPI SIMO for all AX5043s |
|95		|MIBSPI1CLK				|AX5043\_CLK			| U|SPI clock for all AX5043s |
|96		|MIBSPI1NENA			|AX5043\_SEL4\_N		|OU|SPI chip select for AX5043 RX4 |
|97		|MIBSPI5NENA			|AX5043\_SEL\_TX\_N		|OU|SPI chip select for AX5043 TX |
|98		|MIBSPI5SOMI[0]			|						| U|free gpio (Save for extra SPI if possible) |
|99		|MIBSPI5SIMO[0]			|						| U|free gpio (Save for extra SPI if possible) |
|100	|MIBSPI5CLK				|						| U|free gpio (Save for extra SPI if possible) |
|101	|VCC					|						|  | |
|102	|VSS					|						|  | |
|103	|VSS					|						|  | |
|104	|VCCIO					|						|  | |
|105	|MIBSPI1NCS[0]			|						| U|free gpio |
|106	|N2HET1[08]				|ATTACHED				|?D|PC104 Pin 31 |
|107	|N2HET1[28]				|PB\_ENABLE				|?D|PC104 Pin 45 |
|108	|TMS					|JTAG pin				|  | |
||||||
|109	|TRST					|JTAG pin				|  | |
|110	|TDI					|JTAG pin				|  | |
|111	|TDO					|JTAG pin				|  | |
|112	|TCK					|JTAG pin				|  | |
|113	|TCK					|JTAG pin				|  | |
|114	|VCC					|						|  | |
|115	|VSS					|						|  | |
|116	|nRST					|\*Processor\_Reset		|  |Main reset pin for the processor |
|117	|nERROR					|FAULT\_N				|  |PC104 PIN 19 |
|118	|N2HET1[10]				|						| D|free gpio |
|119	|ECLK					|						| D|free gpio |
|120	|VCCIO					|						|  | |
|121	|VSS					|						|  | |
|122	|VSS					|						|  | |
|123	|VCC					|						|  | |
|124	|H2HET1[12]				|POW\_MEAS\_EN			|OD|\*TX power measurement enable |
|125	|H2HET1[14]				|PA\_PWR\_EN			|OD|Enable PA power |
|126	|GIOB[0]				|AX5043\_IRQ\_RX2		|ID|Interrupt from AX5043 RX2 |
|127	|N2HET1[30]				|CMD\_MODE				|?D|PC104 Pin 27 |
|128	|CAN2TX					|CAN\_B\_TX				|OU|CAN bus B transmit |
|129	|CAN2RX					|CAN\_B\_RX				|IU|CAN bus B receive |
|130	|MIBSPI1NCS[1]			|\*FEED\_WATCHDOG		|OU|Resets the two hardware watchdog timers |
|131	|LINRX					|UART\_RX2				| U|PC104 Pin 36 |
|132	|LINTX					|UART\_TX2				| U|PC104 Pin 32 |
|133	|GIOB[1]				|GIOB\_1				|?D|PC104 Pin 16 |
|134	|VCCP					|						|  | |
|135	|VSS					|						|  | |
|136	|VCCIO					|						|  | |
|137	|VCC					|						|  | |
|138	|VSS					|						|  | |
|139	|N2HET1[16]				|FCODE\_D3				|?D|PC104 Pin 60 |
|140	|N2HET1[18]				|USB\_Suspend\_Low		|?D|PC104 Pin 104 |
|141	|N2HET1[20]				|AX5043\_PWR\_EN		|OD|Main power enable for all AX5043s |
|142	|GIOB[2]				|AX5043\_IRQ\_TX		|ID|Interrupt from AX5043 TX |
|143	|VCC					|						|  | |
|144	|VSS					|						|  | |


FIXME - Figure out what all the PC104 pins do.

# \*Notes below

Interrupts and GPIOs
--------------------

On the TMS570, most normal pins can also be used at GPIOs, but they
are not capable of generating interrupts.  Only the GIOx[n] pins can
generate interrupts, and they are all used for that purpose.


Notes on thermsistors
---------------------

Thermsistors are connected to ADC pins on the processor to measure
temperatures on the board.  Resistance varies from 500 ohms (125C) to
350k (-50C).  There is a 10K bias, so this gives this gives a .16V
(125C) to 3.2V (-50C) voltage range.  It is supposed to be fairly
linear.

Notes on Processor\_Reset
------------------------

The 3.3V and 1.2V power converts have power good output pins, and the
1.2V current limiter has a power good pin, all open collector.  These
are wire-or-ed to the processor reset pin.  When any of them senses
there is a power issue, they will pull the reset pin.  After the 1.2V
current limiter turns on (which takes a little bit of time, it is
inrush limited) it will wait 50us and before releasing the reset pin,
so reset should happen automatically on any power up or power problem.

Notes on FEED\_WATCHDOG
-----------------------

This must be toggled at least once a second.  If it isn't, the
hardware watchdog will power off the board for 200ms and power it back
on.

Notes on TX Power Measurement
-----------------------------

A directional coupler and power measurement chips (ADL5501AK) feed
into the ADCs (Forward power to pin 74 AD1IN[3] and reverse to pin 73
AS1IN[2]) and an enable for those parts into pin 124 N2HET1[12].  Pin
124 is pulled down by default, so the chips will be disabled at reset.
The direction coupler is 4mm long with .1524mm traces .127mm apart.
At full power out (+33dBm) this will result in about -7dBm of power
from the coupler.  This was simulated with a transmission line in
qucs.  The voltage for that can be calculated from the chip manual.

# Power Control and Sequencing

The power control on the board is fairly simple.  One power up, the
LP3962EMP-3.3 LDO will start supplying 3.3V to REG\_3V3 and the
TPSM828302ARDSR will start supplying 1.2V to REG\_1V2.  They will also
pull the PROCESSOR\_RESET pin low until their power is good, and that
point they will not pull the reset line low any more (they are open
drain).  At that point the MP5073GG-P is also holding reset line low
until it is enabled.

The STWD100NYWY3F hardware watchdog will power up at that time, but
the POWER\_ENABLE pin from it will be pulled high and should remain
high for 1 second.

The MP5073GG-P and MAX4495AAUT current limiting chips will start
supplying power to the rest of the board once they detect that power
is good.  However, the MP5073GG-P will wait 50us after it senses the
1.2V power is good holding the PROCESSOR\_RESET line low, then it will
let the processor go.

All the chips driving the PROCESSOR\_RESET line have power sensors, if
any of them sense that the power is bad they will pull that line down
low.

When the processor is in reset and the default settings on the
PA\_PWR\_EN, the AX5043\_PWR\_EN are pulled low (and they have pull
downs, too, so that they are disabled even when the main power is
disabled), so all power to the PA and AX5043s will be off.  The only
other piece of the board that will be powered is the LNA (QPL9547)
because it is directly connected to +5V, but it has a pull up on its
enable line so it will be disabled, too.

So when the board comes up all the RF section of the board is powered
off.

A HW\_POWER\_OFF\_N comes in from the PC104 connector; if that is
pulled low it will power off everything on the board.  It does this by
disabling the 3.3V and 1.2V regulators.  When 3.3V is off, the MAX4995
controlling power to the PA will be powered off, so that will be
disabled.  The only other part that's directly on +5V is the LNA, as
mentioned before, but it will be disabled by default with a pullup to
+5V.

There is also a hardware watchdog, as mentioned before.  The processor
must toggle the FEED\_WATCHDOG line at least once a second.  If it
fails to do that, the 1.2V and 3.3V current limiters will be disabled
cutting power to the processor and all digital components.  This will
result in everything else being powered off.  After 200ms, the
watchdog chip will enable power again.

To power up and enable the RF section, the processor must first make
sure all the AX5043 enable lines are pulled high to disable them.
This is not the default (some are low and some are high by default),
but it doesn't matter because they are powered off at the main,
anyway.  The processor then can drive AX5043\_PWR\_EN high to enable
the power to all AX5043s.  The processor can then drive the individual
AX5043 enables low to individually power them on.  Then the processor
can drive PA\_PWR\_EN high to power on the PA and LNA\_ENABLE high
to enable the LNA.
