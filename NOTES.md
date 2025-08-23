Notes on the AFSK Board
=======================

This keeps track of history, general information, things that need to
be done, and things that have been done.

The general information will probably make it into another document at
some point.

# TODO

The 78nH inductors in the AX5043 input section don't come in very high
Q values, 28 is the best you can get.  77 and 79nH are even worse.

The MRAM parts are WSON packages.  SIOC packages are available, too.
SIOC is somewhat bigger, but might be better from a thermal point of
view.

According to the cubesat documents I have been reading, its best if
parts are automotive certified, AEC-Q100 or AEC-Q200.  I assume this
is so they can handle the shaking of the flight to space.  The
passives can all be certified for this, I'm pretty sure.  The only
connector you have to worry about is the PC104.  The chips and modules
are a different story.

Parts that are not automotive rated listed below.

|Part						|Function			  | Info |
|----						|--------			  |----- |
| LMK1C1106A				| clock distributor   | Suitable devices with 6 output not available.  Could use 4 output device (LMK00804B-Q1). Could use op amps (see https://www.analog.com/en/resources/analog-dialogue/articles/high-speed-amplifiers-make-clock-buffers.html). |
| O 16,0-JT22CT-A-P-3,3-LF	| oscillator | There don't appear to be any that are automotive and temp certified with 2.5ppm stability.  This one is temp, which is probably more important. There is one from TXC at 16.389MHz. |
| AS1016204-0108X0PWAY		| MRAM | No suitable devices available. |
| MAX31331					| RTC | No suitable devices available. |
| TPSM828302ARDSR			| 1.2V power converter | TPSM33620S3QRDNRQ1 might work |
| MP5073GG-P				| 1.2V current limiter | No suitable devices appear to be available. There is an MP5072 part that is AEC rated, basically the same chip but it's 1A instead of 2A. |
| MAX4995A					| 3.3V and 5V current limiter | Some devices are available from TI, like TPS2561-Q1 (dual channel) or TPS2557-Q1 (single channel). The MAX part may already be flight proven, though. |
| AX5043					| radio | No other option. |
| TQP7M9106					| PA | ? |
| QPL9547					| LNA | ? |
| RBP-140+					| receive filter | Environmental Specs seem good, probably ok. |
| AD4PS-1+					| RF power splitter | Environmental Specs seem good, probably ok. |
| QPC1022TR7				| RF switch | ? |
| ?							| PC104 connector | Unknown if AEC |

Part that are automotive listed below.

|Part						|Function			  | Info |
|----						|--------			  |----- |
| STWD100NYWY3F				| Hardware watchdog |
| TCAN1044ADDFRQ1			| CAN bus interface |
| TMS570LS0914PGE			| CPU |
| TPS7A52-Q1				| 3.3V power converter |

I'm assuming that most ICs won't be a problem from the vibration point
of view.  The power modules are probably good to get certified, though.

If lines on the PC104 bus are outputs, wouldn't they need to be open
collector or such if they are driven by multiple boards?  I haven't
been able to find much about the PC104 interface.

I found https://github.com/visionspacetec, specifically the VT104
repositories that have a PC104 connector.

Figure out what all the PC104 pins are supposed to do and document
them.  The lines are listed in the ProcessorPins document.

Figure out what to do with the UART pins on the PC104 when dealing
with active/standby.  Really just figure out what to do with the UART
pins.

Probably switch the analog switches dealing with active standby with a
set of zero ohm resistors.  That's a lot of resistors to switch,
though.  Populating 8 of 16 total resistors, maybe more with the UART
lines.  But there are advantages to a completely passive solution.

You could use one of the receive AX5043s ANTP1 port as an alternate
transmitter.  You could use the same PA or a different PA, either way
a QPC1022 RF switch could handle the choice.  You could even have
separate antennas.

Figure out where the external RF connections need to be so the layout
can be simplified around that.

Figure out temperature ratings on all parts and get as many to be 105C
or better as possible.  The outliers at the moment are:

    * RTC.  Probably only the MCP7940NT-E/MS from Microchip is
	  suitable, but it draws 20 times the standby power.
    * AX5043 - Not another option available.
	* RBP-140+ - Could replace the filter with discrete components.
	* AD4PS+1 - Not sure about this one, perhaps three transformers
	  could be used.

After the MRAMs and second CAN bus, GPIOs are running short.  We have
some options.  A 2-4 decoder could do this, but you would also need an
enable (and thus pullups), and it would really only recover one GPIO.
Another option is an I2C or SPI to GPIO device.  The AX5043s each have
5 pins that can be used for GPIOs, though that means if an AX5043
fails you can't use those GPIOs.  The interrupts from the AX5043s
could be or-ed together, but you would have to scan all of them if you
got an interrupt.

The PC104 connector is actually two connectors, a 64-pin (4x16) one
and a 40 pin one (4x10) per the PC104 web side.  I've actually more
seen two 2x52 connectors more often on schematics.  Need to figure out
how to represent that.

Do steel RF shields affect the inductors under or around them?  Is
aluminum better?  - No one was sure, maybe it's non-magnetic steel?
We will just have to try it out.

Is the output filter on TX enough?  It's >50db at 800MHz and 1.6GHz.
You get some filtering from the impedance matching network, too.
 - Need to measure and see.

There's a note in the schematic about biasing the 5043 inputs, but I
can't find any info on that.  It's on the RF Input sheet.  Need to
figure out if that's something that needs to be done.  I don't really
understand the comment, though. - The comment was from an app note
that Bob read that the inputs on the 5043 apparently work better if
biased to about 1V.  He can't find the app note any more.

The RX input filter can probably do the impedance adjustment for the
LNA, but I'm not sure how to calculate that.  There's an impedance
matching circuit in there now, removing it would save two parts.

Probably remove the L1/L2 inductor on the AX5043s and replace them
with a short.  I don't think we will use them. - Needed for 2M to
work, need to get the inductor value.

Is there a reason the ANTP1 output of the AX5043 is connected to a 50
ohm resistor?  I can't find anything in the datasheet or errata about
that, it always shows it disconnected when not used. - May or may not
be necessary.

What UFL connectors can be removed?

Determine current limiter values, probably need to build a board and
measure.

# Done

Figure out how to hold the processor in reset until the power is good.
Need power good output from the converters, maybe switch to a
TPSM828302 for 1.2V and a LP3962 for 3.3V.

Replace big capacitors with smaller ones, if possible.

Move the TX chain to the right side of the board under the power
handling.

Move JTAG next to processor.

Replace the 4 512Kx8 MRAM chips with one 2Mx8 like the Avalanche 
AS1016204-0108X0PWAY.

Replace the DC/DC converters to ones that have the inductor built in,
to save space.

Move most power handling and watchdogs to the to right hand part of
the board.

Move the RX ax5043s to below and slightly left of the processor.  Move
the RF chain to below that.

Possibly rework board stack to have .1mm between the top layer and the
ground layer to reduce trace size required for 50 ohms.
(This was already done.)

Wire VER\_BIT2 to the PC104 connector.

Figure out the best way to handle the RX side of the AX5043 chips.  A
single-ended design would save a lot of board space because you can
get rid of one RF power splitter and the balun.  The AX5043 docs are
kind of sparse about how to do that, there's no mention of input
impedance on the receive side, and the transmit impedance info is
unhelpful.  But the full RF filter input as shown in the documentation
probably isn't required.  Maybe a balun on each RF input would be
enough to match impedance, since the signal is already filtered.

Replace receive side with LNA not requiring negative bias.  Probably
use a Qorvo QPL9547 due to its low NF.  Or maybe a GuerillaRF GRF2106W
which doesn't perform quite as well but uses a lot less power.

Put filters on each side of the LNA.

Make the 5V regulator optional or remove it.
(Removed, but space left for it.)

Possibly switch the MRAM and AX5043 SPI busses to simplify routine.

Figure out a way to disable the LNA from the CPU.

Find out why CURRENT\_FAULT\_U89 goes into two pins on the CPU.

Choose one oscillator and remove the other one.  Actually, just
replace with a "O 16,0-JT22CT-A-P-3,3-LF" from Jauch.

Neaten up the spacing on the AX5043s.

Add a thermsistor for the CPU.

Add CAN bus.

Add resistors to the MRAM SPI connection.

Does the JTAG interface need resistors on TCK and TDO (22 ohm)?
That's pretty standard.

The RF lines need some rework, some from the hybrid to the AX5043s are
kind of long, and they probably need to be coplaner.  I have added a
coplaner net class for this board stack (.225mm trace, .7mm spacing).

Shield on receive AX5043s.

Shield on transmit AX5043.

Decoupling, at least on 1.2V, seem inadequate.  Check that out.

Figure out how to orient the shields properly.

Add an option for a bleedoff inductor on the transmit output.

Via impedance

The chosen shield size for the AX5043s isn't tall enough.  The
transform is inside the shield, and it's 3.05mm tall, but all the
shields of the chosen size are 2.54mm tall.  I can't find a suitable
shield smaller than that to put the transformer on the outside.  The
shields with the proper height are way too big.  I can find a few that
are 12.7x13.2mm that are 3.5mm tall, but they would need to be
customized to add holes for traces.  You could just add a hole for the
transformer, I suppose.  Or get a custom shield.  Some of the shields
are pretty open on the top, like the PIC-S-201F, and the transformer
looks like it will go through the hole in top.  The transformer is
4.19x4.45x3.05mm, but that's the base dimensions, the transformer part
that comes up is smaller.  The opening int the top of the shield is
2.35mm at the narrowest point.  Estimating the size of the transformer
from the pictures, I get 2.2mm.  The opening starts 1mm from the
bottom of the shield, and that means the transformer would have to be
pretty close to the bottom.  However, after more analysis, I had the
orientation wrong, it's rotated 90 degrees from what I thought.  So
it's not going to work.

The RX shields are now the PIC-S-201F, the TX shield is the PIC-S-101,
but the RX shields will need some change.

In the shield problem, will the transformer coming up through a steel
enclosure affect the performance of the transformer?

Shield on RX input section.

Shield on TX PA section.

Check the inductor on the LNA, really verify the whole thing.

Change the 1.2V power controller to a MP5073.

The "Current Fault\_1V2" and "Current Fault\_3V3" are not connected to
anything and can probably be removed with their pull up resistor.  I
don't think there's much value in hooking it to the processor, if
either of these fire the processor will crash.

Do we need the capacitor between the LNA and the filter?  The filter
datasheet shows an input capacitor first, so that should block the DC.
The only concern would be the DC bias characteristic changing the
value of the capacitor.  I've asked MiniCircuits about this.
* This had to be added for other reasons due to the impedance matching
  circuit.

Write a document describing all the interfaces from the processor to
the rest of the board.

There may need to be a delay on the reset line from the power good
outputs because the power limiting circuits may take time to turn on.

The inductors for impedance matching the output of the LNA are on the
bottom of the board.  This isn't ideal, as they aren't in a shield,
but it's pretty crowded in the LNA shield.

I'm not terribly happy with the way the signal goes through the RX
input, but I'm not sure what to do about it.  I've improved it a lot,
but there's still a sharp turn on the inductor that leave the LNA are.
You might be able to rotate the LNA so the signal comes back towards
the center of the shield and then curves back around to leave, but I'm
not sure that's better.

The shields I have are steel, which is probably going to mess with the
inductors.  Need aluminum shields.

Clean up all the schematic notes and number all the device references
in a logical manner.

Add measurement of output and return power on TX.  I assume this can
be built with directional couplers, op amps, and the ADC on the
TMS570.

Analyze the RX input filter.

Figure out the AX5043 SPI routing.  Simulate the clock line in spice
to avoid possibility of double clocking, add proper resistors.

Add a thermsistor for the PA.

Route signals directly, don't use RF jumpers.

Rework transmit RF side.  At least replace the filter with a new one,
probably the LFCG-490+ from MiniCircuits, which also happens to be
temperature rated.

Look at replacing the second from bottom layer with a ground layer so
the bottom layer can be used to route RF traces.  This may not be
necessary, though, with careful layout. -- This was done for the RF
portions of the board, but not the digital or power areas.

On the output of the AX5043 transmit/input of the PA, there is each a
filter.  The one on the AX5043 has parts marked "NS", which I assume
means "don't populate".  The inductor is zero there.  C704 is also
marked NS on the PA sheet, which is most likely wrong.  Need to figure
all this out. -- Jim McCullers wrong a document on this, I just stole
his stuff.

Switch all the MAX4995 parts to the active high enable.  This will
make them all the same, avoiding confusion, and also make handling the
enable line easier since they will be pulled down.  It's hard to know
what to pull them up with.  It may not be good to drive the GPIO lines
with a pullup when the processor is powered off.  That will require
moving the enable flags to new GPIOs, but that's not a big deal.
Switch them to N2HET1[14] and N2HET1[20].

The TX AX5043 is powered off if "Alarm XMIT Shutdown" is activated by
the watchdog.  Do we really what this?  I think it would be good
enough to just power off the PA.  Will that work?  Powering down the
5043 means it has to be reprogrammed and it could really confuse
things if the part was powered down while something was talking to it
on the SPI bus.  I don't think it will hurt the PA to be driven while
powered off.

In fact, is the radio transmit killer really required?  If
FEED\_WATCHDOG is not toggled, the board will be powered off, and that
will accomplish the same thing.  It seems redundant.

The power shutdown IC on the TX AX5043 is different than the RX ones.
They should probably be consistent.

There is a +5V pullup through 10K on the LNA enable, and that line is
also driven by a TMS570 GPIO.  The pull up has to be there to disable
power when the board has power forced off.  I don't think it will be
an issue, but I'm not 100% sure there won't be an issue there when the
processor is driving 3V on the line.  If it is an issue, this could be
fixed easily with a FET.

Maybe add ferrite beads to the AX5043s' power inputs?

Why are there 4.7K resistors on the power inputs to the RTC?  And is a
diode needed on the VCC connection?  The diode on VBAT I can
understand, I think.  Also, VBAT voltage will be above VCC.  That
seems to be ok according to the data sheet, I think.  Also, maybe it
would be better to stick a big capacitor on VBAT.  A 220uF capacitor
would last around 94 hours at 5V, or 61 hours at 3.3v, by my
calculations.  That's the MAX31331, which uses 65nA on battery, and
there will be leakage in the capacitor (and diode if not trickle
charging) that will probably shorten the time. - Rework this to
increase the size of the Vbat capacitor and not use the VCC one, just
do a normal decoupling cap there.

Move the RTC away from the power conversion section to avoid it
getting too hot.

What does the HW\_SENSE (Pin 6 on CPU) do? - Get rid of it

Does it make sense to wire the UARTs to the PC104?  If so, do we need
two of them on the PC104?  Shouldn't one go to a separate connector
somewhere?  If so, which one?  UART1 is a standard UART, UART2
supports "Local Interconnect standard 2.0" which is probably better
for an interconnect.  So UART1 (SCI) should go to the local connector
and UART2 (LIN) should go to the PC104, I think.  More info: the LIN
bus requires special hardware, it's not just a serial connection.
Yes, put a connector on there so the UART1 pins are available, maybe
run to the PC104, too.

The LNA doesn't have a current limiter on it.  It's best to power it
with +5V (it will work on +3.3V, but it doesn't perform as well).  You
don't want to put it on the PA power lines, as you may want to power
off the PA while still receiving.  Maybe another current limiter is in
order?  Yes

Add 3 more MRAM parts.

Do we need all those wire holes?  A few I can understand, for powering
the board on the bench, but there are a bunch of them, some with just
grounds.  Need to figure out their purpose. - Used for scope clips.
Need to add a few more.

The 3.8K resistor on HW\_POWER\_OFF\_N is a strange value.  Can it be
a more normal 4.7K or 10K?  Yes

Add more vias around the ground areas in RF.

Probably add another CAN bus.

Figure out what happens when the two lockstep processors lose sync.
If one of the processors goes bad, is there a way to just run with one
processor?  - If there is a lockstep error, a software interrupt is
generated and software must handle it.  The processors cannot run
independently, they can only run in lockstep or in certain test modes.

Maybe switch to 0402 parts along the RF path to reduce stray
inductance and capacitance and reduce size.  And perhaps don't use
handsolder, as the pads are larger and thus have more
capacitance/inductance.  Maybe 0402 parts on the rest of the board to
get more space.

Add enables to the CAN bus transceivers?  The chip does not really
have an "off" state, it's a "standby" state where it's listening on
the bus but cannot transmit.

Fix DC bias issue on the output impedance filter of the LNA.

Replace PA output filter.

# Not going to do

Rotate the CPU so that fewer traces need to be routed under the CPU.
Perhaps replace the CPU with a BGA version to save space, the BGA is
16x16mm verses 22x22mm for the flat pack.  This could also provide
more FLASH and RAM space. -- Moving a few lines around the processor
made a huge difference.  This is not necessary.

Maybe put the directional coupler on the layer under the transmit
trace instead of beside it?  The coupling would be better but I would
need to calculate the coupling.  But this is just a maybe, what's
there is probably good enough.  Don't want to steal too much power
from the transmitter.

There are now individual power enables on each AX5043.  Do we need the
main one?  The problem is we would need a lot of processor GPIOs that
are pulled down by default, or we would need to switch to power chips
with active low enables.  Plus there is then no power limiting.
Probably not a good idea.

Why is both the RTC and the hardware watchdog controlling the transmit
shutdown?  It would seem only one or the other would be necessary.
The whole transmit shutdown thing has been removes, so this is no
longer relevant.


# RF Shields

RF shields cover all the RF sections possible to cover.  There are 7
shields and they use standard shield sizes.  The bottoms are
castellated and surface mount.

Six shields cover the AX5043s and the RF input section are 12.7mm
x 13.67mm (.5"x.538") and the one that covers the PA is 26.21mm x
26.21mm (1.032"x1.032").  There are options from at least TE
Connectivity AMP Connectors, Leader Tech Inc, Laird Technologies EMI,
and 3G Shielding Specialties LP.

The traces running in and out of the shields are done in a way to
accommodate all these shields, though not all have been checked.

I assume shields should be non-magnetic to avoid issues with inductor
coupling.  It's hard to find two-piece shields where the frame is
aluminum, though.  I'm not sure of the requirements around this,
though.

# History

## 2025-07-23

The pins for AX5043\_PWR\_CTL moved (and I think was renamed) and there
is a new PA\_PWR\_CTL line.

The Address notes on the two MAX31725MTA+ temperature sensors were
backwards.  Switched the notes so they match the schematic.

VER\_BIT2 is not wired to the PC104.

## 2025-07-24

Fixed all wiring that was wrong due to schematic changes.

Changed the RTC crystal to a SMD one and remove the capacitor.  The
datasheet says no capacitor is required.

Cleaned up some crazy traces.

## 2025-07-25

Reworked the board, basic layout is done and most details are handled.
Left to do:

* Clock handling

* Rework of the TX power amplier.

* Hooking everything up.

* The rest of the TODO list.

There should be no software visible changes from the changes today.

Remove the DS28E83Q+T crypto processor.  Nobody knew why it was there,
there was no software for it, and it wasn't practical.  Since there is
no onewire hardware on the CPU, it would have to be bit-banged, and
that would cost 50 times the CPU of just doing the crypto on the
CPU.

## 2025-07-26

Change the DC regulators to ones with power good pins and tie that in
to processor reset.

Removed the HW\_POWER\_OFF\_N signal to the CPU.  The CPU is going to be
instantly powered off if that is not asserted; there's not much value
in sending it to a GPIO.

Remove the UART\_RTS and UART\_CTS connections.  The chip doesn't
support these lines, no point in having them.

Switched the MRAM and AX5043 SPI busses to simplify routing.  MRAM is
now on MIPSPI3, the AX5043 is on MIBSPI1.  This puts the AX5043 SPI
connection on the bottom of the processor by the AX5043s, and the MRAM
SPI where there is plenty of room to add MRAM devices as necessary.

Move AX5043\_SEL1 from pin 24 to pin 90
Move AX5043\_SEL2 from pin 33 to pin 91
Move AX5043\_SEL3 from pin 35 to pin 92
Move AX5043\_SEL4 from pin 35 to pin 96
Move AX5043\_SEL\_TX from pin 124 to pin 97

Added an LNA\_ENABLE control on pin 89.

Removed the CURRENT\_FAULT\_U89 signal from pins 73 and 74.  They don't
go anywhere else and serve no purpose I can tell.

Clocks are all set up and wired in.

MRAM is wired in.

## 2025-07-27

Wired in the AX5043 SPI busses and all their control lines.

Added the following connections to the CPU:

AX5043\_EN\_RX1 to pin 36
AX5043\_EN\_RX2 to pin 35
AX5043\_EN\_RX3 to pin 33
AX5043\_EN\_RX4 to pin 32

Added a thermsistor to AD1IN\_16.

The I2C temperature sensors are removed.

A thermsistor by the CPU was added to pin 58.

## 2025-07-28

Added calculations for the Qorvo TQP7M9106 to get Zin and Zout for the
frequency in question.

Rework the output PA to use a Qorvo TQP7M9106.  The old part was not
recommended for new designs, and the Qorvo part seems more efficient.
Do all the matching and such for that.

Added a termsistor by the PA.

Did simulations of the RF input and adjusted accordingly.

Did simulations of the AX5043 TX output.

Add a CAN bus.

Added a resistor to the MRAM SPI clock signal.

Add SMA connectors for TX and RX.

Added resistors to JTAG interface, per the way it's defined.

## 2025-07-29

Replaced UFL connectors with surface mount ones.

Added shields for the TX and RX AX5043 sections.  They are
12.7mmx13.67mm (.5"x.538").  That seems to be a pretty standard size,
lots are available.

Added a bunch of decoupling caps on the CPU, basically one per CPU,
like the launchpad did, and like is standard.

Switched the RX AX5043 shields to PIC-S-201F.  It appears that if
oriented correctly the transformer will stick through the hole without
a radial line on it.  The TX one was left as PIC-S-101, as it doesn't
have a transformer in the can and doesn't need the extra height.  Both
parts have the same base layout.

Sized up some power lines for safety margin.

Calculation of the via impedance (done at Sierra Circuits proto
express) comes out to ~52 ohms.  The board is 1.56mm thick (JLCPCB
2116 board stack), each copper layer is .035mm.  Input is:

  Height of dielectric - H1 ( mm ) - 1.416
  Dielectric Constant Er\_1 - 4.5
  Height of dielectric - H2 ( mm ) - .109
  Dielectric Constant Er\_2 - 4.5
  Dielectric Constant Er\_3 - 1
  Via Diameter ( mm ) - .308
  Anti Pad Diameter ( mm ) - 1.53
  Annular Pad Diameter ( mm ) - .508
  Via Pad Diameter ( mm ) - .508
  Via Plating Thickness ( mm ) - .035
  Annular Pad Thickness ( mm ) - .035
  Reference Plane Thickness ( mm ) - .035

Reroute the SPI clock to the bottom of the board where it can be
impedance controlled to 50 ohms.  Add a ground plane on the bottom to
the entire RF section so that the impedance is the same as on the top.

Simulated the AX5043 SPI clock and set the resistor values to 470 ohms
and added a resistor for the end device, too.  With the current
settings, assuming a .2ns rise time from the processor, this gives a
fairly smooth signal on all the inputs.  The signal reaches 2.8V (from
0 to 3V input) or .2V (from 3V to 0) in 2ns.  Resistance values 330
and down give some issues at the RX2 input, there is a dip that could
be double-clocked on.  Higher values will slow the rise time more.
With this setup, no resistors on the other lines, as long as they
settle within half a clock period plus 2ns, all should be good.  You
could probably run this at 100MHz without an issue.  But the double
clocking is the big problem.

## 2025-07-30

To solve the problem with the transformer not fitting in the shield,
replace the transformer with a lumped sum balun as described by the
work Jim McCullers did in the "AX5043 Receiver Impedence Matching"
document.  I just used the values he came up with.  Changed all the
shields back to the PIC-S-101.  Also changed the zero-ohm resistor
from the RF splitter to the AX5043 to a decoupling capacitor.

Changed the zero-ohm resistor between the TX AX5043 and the PA to a
decoupling capacitor.

Changed the shields on the AX5043 to PIC-S-201F which is a frame and a
cover.  This can be replaced with a PIC-S-101 which is a single unit
when access is no longer needed to the parts underneath.

Added a shield for the TX PA and RX input sections.

Add a thermsistor for the power conversion area to pin 83.

Rework the RF input circuitry.  I had to increase the power feed
inductor and add an input and output impedance match circuit.  That
required changing the parts around the LNA to 0402 size to get them to
all fit.  You might be able to modify the input filter to adjust the
impedance, but I couldn't figure out how to do that to match a complex
impedance.  I'm sure it can be done, but it's a matter of how.

## 2025-07-31

Replaced the 1.2V current limiter/switch with a MP5073GG from
Monolithic Power.  The MAX4495 that was there wasn't rated for 1.2V.

Remove the Current Fault lines for 1.2V and 3.3V.  They didn't go
anywhere, and there's not much the processor could do about it if they
went bad.

Removed the zero ohm resistors on WDO\_N, the enable line feeding the
current limit switches enables.  There's already a way to turn of the
watchdog on the watchdog chip, so it doesn't seem necessary.  Plus the
line needs to be driven to work.  Also renamed WDO\_N to POWER\_ENABLE
to better reflect what it does.

Wired in the power good pin on the MP5073GG-P to the processor reset
so that the processor is held in reset until 50us after the chip
enabled power.

Cleaned up the hierarchical sheets and re-annotated everything to make
copying and pasting easier.

Reworked the LNA input and output impedance matching so nothing had to
be on the bottom of the board.  Switched the positions of the
capacitor and inductor in the L match, that let me match more closely
with single standard parts instead of having to use two inductors.

## 2025-08-01

Improved the LNA layout some more.  I have one part rotated at 45
degrees to round a corner a little better.  It's not required, but
it's supposed to be better for RF flow.

Rotate the RF filter after the LNA to improve flow and do some more
cleanups.

Reworked the LNA some more, I think I'm happy with the layout now.

Widened the bandwidth of the input filter.  That reduces the inductor
values to ones that are obtainable.

Switch to aluminum shields.  A number of shields are possible to use,
see notes.

Update the RF input filter again for wider bandwidth to get a 180nH
inductor, something low enough to fit into a 0805 part with a decent
Q.  Annotate the schematic with the Q values of the various inductors
that I was able to find.

Snug in the 3.3V LDO a bit more to give more space on the side.

## 2025-08-03

Add a directional coupler and power measurement chips (ADL5501AK) to
feed into the ADCs (Forward power to pin 74 AD1IN[3] and reverse to
pin 73 AS1IN[2]) and an enable for those parts into pin 124
N2HET1[12].  Pin 124 is pulled down by default, so the chips will be
disabled at reset.  The direction coupler is 4mm long with .1524mm
traces .127mm apart.  At full power out (+33dBm) this will result in
about -7dBm of power from the coupler.  This was simulated with a
transmission line in qucs.  The voltage for that can be calculated
from the chip manual.

Fixed an issue with the 3.3V power controller.  The 1.2V controller
part (MP5073GG-P) is an active high enable, the MAX4495ALAUT is an
active low enable.  So switch out the 3.3V controller with a
MAX4495AAUT (which has an active high enable), but leave the other two
with the AL version of the part.  The WDO_N output from the hardware
watchdog is active low, but the logic is backwards, when the watchdog
fires (goes low) we want it to disable the power.  I think this was
wired incorrectly in the REVC and REVD schematics.

Added a pull up on LNA\_ENABLE\_N so that the LNA is disabled even
when the rest of the power to the board is off.

Switch the logic on AX5043\_PWR\_CTL from active low to active high by
switching from the MAX4495ALAUT to the MAX4495AAUT.  Rename it to
AX5043\_PWR\_EN.  Move it from pin 98 to pin 141 so that it's pulled
down by default in the processor, too.  Still need the external pull
down in case the processor is turned off.  Pulling that line up was
problematic, as you don't really want to use +3.3V (will be off if
power is externally disabled) or REG_3V3 (driven if processor is
powered off).  Also this makes all the parts the same, making
inventory easier.

Do the same with PA\_PWR\_CTL -> PA\_PWR\_EN, move from pin 99 to pin
125.

Make the AX5043 TX power control chip the same as the ones on the RX
chips, just to be consistent and have one less chip to worry about.

Remove the PA power watchdog.  It's not doing anything useful.  It's
driven by the same watchdog line as the main watchdog, and if the main
watchdog fires it's going to power off everything, resulting in the PA
being powered off.  There were other issues, too, as it would power
off the AX5043 TX chip, too, which could cause bad things to happen if
the SPI bus was talking to it at that time.  But it didn't really
matter, the processor would be powered off, anyway.

Add a AX5043\_EN\_TX line to pin 100 of the CPU to control the power
to the AS5043 TX device.

Move the LNA\_ENABLE to pin 118 so it's a pull down by default and
rework the LNA enable so the +5V is not applied to a GPIO pin
directly.  Go through a MOSFET instead.

## 2025-08-04

Change the LNA\_ENABLE MOSFET to a BSS138, just to choose something
common.  Also fix the footprint.

Change the AX5043 power control chips to be MOSFETs.  No need for
something complicated.  Use P-Channel enhancement mode MOSFETs, so the
enable has to be pulled down to turn on the MOSFET.  Rename the
enables to add a \_N for negative logic.

Rename the AX5043 select lines to add a \_N because they are negative
logic.

Remove the connection from KELVIN\_GND to ground.  According to the
TMS570 data sheet, that pin should not be connected to any other
ground.  I don't think it matters, it's only for crystals, but it
should probably be left floating.

## 2025-08-05

Fixed some part values, used 4.1p style, not 4p1.

Add a pin 1 indicator to a couple of ICs that didn't have it.

Moved AX5043\_EN\_TX\_N from pin 100 to pin 89 and
AX5043\_EN\_RX\_4\_N from pin 32 to 24.  This frees up all the
necessary MIBSPI5 lines for possibly adding another SPI bus on
the board.

Fix the footprints on the diodes on the RTC.

Update the ferrite beads with actual values.

Add ferrite beads to the AX5043s' power inputs.

Changed the clock buffer from a CDCLVC1106 to a LMK1C1106A.  It
temperature rated, has better specs, and is cheaper, and drop in
compatible.  Looking at the power usage, it's hard to tell.  It looks
like the specs were misinterpreted for the CDCLVC1106, the power given
on the graph was per pin, so it would really be around 20ma, the same
as given for the LMK1C1106A.

## 2025-08-07

Increase the size of the Vbat capacitor on the RTC and do not use the
VCC one, just do a normal decoupling cap there.

Move the RTC to the other side of the board to keep it away from
things generating heat.

Remove the HW\_SENSE (Pin 6 on CPU) line.  It was used on a dual CPU
system to tell which CPU was which, not relevant here.

Add a local connector to UART1 to make it easier to plug in an
external connector.  Still left it on the PC104 along with UART2.

Add a power limiter for the LNA.

Add 3 more MRAM parts.

## 2025-08-08

Added a series termination on the CPU clock.

Modified the resistor on the LNA power limiter to be 200ma.

Move the JTAG connector to the edge of the board so it's accessible in
a board stack.  This required moving some things around, but no big
deal.

Add some wire holes around the LNA and PA.

Change the 3.8K resistor on HW\_POWER\_OFF\_N to a more normal 4.7K.

Sprinkle vias all over the coplanar areas.

Reworked MRAM devices to put pull-ups on the WP and IO3 pins instead
of direct ties to +3.3V.

Add a second CAN bus for redundancy.

## 2025-08-10

Fix some values on the PA and rearrange a bit to get the inductors
away from each other.

## 2025-08-12

Removed the version lines going to the PC104.  They get in the way and
I can't imagine what use they would have.  They can be re-added if
necessary.

Moved things around at the bottom of the board to make room for the
active/standby RF circuitry.

Added support for active/standby boards in the hardware.

## 2025-08-13

Change transmit power dissipation resistors to 2W.

Moved ACTIVE\_N to a normal GPIO so it can be interrupt driven.

Add OTHER\_HW\_POWER\_N to a GPIO so in the externally driven
active/standby case the other power state can be monitored.

Added a test mode using the RF switches to shunt power from the
transmitter to the receiver for an RF loopback test.

## 2025-08-14

Changed SMA connectors to vertical ones.

Change SMA TX/RX connectors to U.FL connectors.  For development I
will epoxy down a U.FL to SMA cable to the board.  For deployment
various options exist, including UFL or soldering cables directly to
the board and epoxying them down.

Get rid of the GPADC zero-ohm resistors on the receiver AX5043s.
Those cannot be used when receiving, and their use is questionable,
anyway.  Leave it on the transmitter one as that could still be used.

## 2025-08-15

Change many of the passives to 0402s to make more room and reduce
parasitics.

Add a current limiter for the onboard +5V devices, create a new power
rail named +5VAL for all the devices that need to be powered up even
when the power is off.

Add enable controls for the CAN bus transceivers.

Fixed the RF input and output filters.  Added a simulation for the
RF output filter.

Fixed DC bias issue on the output impedance filter of the LNA.

## 2025-08-16

Rework the output filter.  The part that was chosen really wasn't
suitable, it didn't have good thermal or vibration characteristics and
it wasn't enough filtering.  Switch to a discrete filter.

Change 3.3V power convert to a TPS7A52-Q1.  It's AEC rated.

## 2025-08-18

I spent practically a whole weekend trying to figure out how to
measure impedance matching circuits.  This probably has more general
applicability to power measurement in general, but in spice measuring
power on a signal that is complex is problematic.  I think the problem
is that you don't have a complex representation of the current, you
get bizarre values out of it if you do a simple V * I.  And doing
V^2/R is hard if R is complex and you don't really know the value.  I
don't think these thing make any sense, in general, and I don't know
how to directly measure the power in a complex signal.

However, I have figured out a way around it.  When you have an L
match, you have a component facing the complex impedance.  You can put
another component in front of the filter to remove the complex
impedance from the signal (just basically match the input imaginary
impedance with the corresponding value).  Then adjust the component
of the L match facing the complex impedance.

Examples are in order.  Start with an easy case.  Suppose we have an
output impedance of 6.23 - j13.3 at 435MHz.  If we plug that into a
smith chart or an impedance matching program, we get two possible
outcomes.  The first is a 10.9nH series inductor and a 19.4pF parallel
capacitor.  Just split the inductor into two, 4.87nH (j13.3 ohms at
435MHz) then 6.03.  Then the capacitor.  Take your power measurement
between the two inductors.

The other possibility is a 113.9pF series capacitor followed by a
6.9nH parallel inductor.  You can't just split the capacitor into two.
Or, from a smith chart representation, the first value does not pass
over the zero imaginary impedance line.  But we can use the same
4.87nH inductor before the capacitor to bring the value to zero
imaginary impedance, then adjust the capacitor value (to 22.1pF) and
measure between the inductor and capacitor.

If you have a parallel device facing the complex impedance, you can
split it in to in parallel (if that work) or as in our second example
put a device between to cancel the complex impedance.

From the simulation you can also put the resistor first after the
voltage source and measure before it goes into the capacitor or
inductor.  The simulations were modified to do this.

## 2025-08-20

Remove the UART connections from the PC104.  It's unknown if they are
needed, and if they are then they will need work for active/standby.
