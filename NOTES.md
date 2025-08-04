Notes on the AFSK Board
=======================

This keeps track of history, general information, things that need to
be done, and things that have been done.

The general information will probably make it into another document at
some point.

# TODO

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

Do steel RF shields affect the inductors under or around them?  Is
aluminum better?

Is the output filter on TX enough?  It's >50db at 800MHz and 1.6GHz.

There's a note in the schematic about biasing the 5043 inputs, but I
can't find any info on that.  Need to figure out if that's something
that needs to be done.  I don't really understand the comment, though.

Why is both the RTC and the hardware watchdog controlling the transmit
shutdown?  It would seem only one or the other would be necessary.

The RX input filter can probably do the impedance adjustment for the
LNA, but I'm not sure how to calculate that.  There's an impedance
matching circuit in there now, removing it would save two parts.

Probably remove the L1/L2 inductor on the AX5043s and replace them
with a short.  I don't think we will use them.

What UFL connectors can be removed?

Do we need all those wire holes?  A few I can understand, for powering
the board on the bench, but there are a bunch of them, some with just
grounds.  Need to figure out their purpose.

Does it make sense to wire the UARTs to the PC104?  If so, do we need
two of them on the PC104?  Shouldn't one go to a plug somewhere?  If
so, which one?

Figure out what all the PC104 pins are supposed to do and document
them.

Replace the RTC with one that is temperature rated.  Probably only the
MCP7940NT-E/MS from Microchip is suitable.  It does not have an
interrupt output, though.

Figure out where the external RF connections need to be so the layout
can be simplified around that.

Maybe switch to 0402 parts along the RF path to reduce stray
inductance and capacitance and reduce size.  Maybe on the rest of the
board to get more space.

Replace unobtanium parts (if any).

Figure out temperature ratings on all chips and get as many to be 105C
or better as possible.

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
high.

The TPSM828302ARDSR and MAX4495AAUT will start supplying power to the
rest of the board once they detect that power is good.  However, the
TPSM828302ARDSR will wait .1ms after it senses the 1.2V power is good
holding the PROCESSOR\_RESET line low, then it will let the processor
go.

All the chips driving the PROCESSOR\_RESET line have power sensors, if
any of them sense that the power is bad they will pull that line down
low.

When the processor is in reset and the default settings on the
PA\_PWR\_CTL\_N, the AX5043\_PWR\_CTL\_N are pulled high, so all power
to the PA and AX5043 will be off.  The only other piece of the board
that will be powered is the LNA (QPL9547), but it has a pull up on its
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
sure all the AX5043 enable lines are disabled (pulled low).  This is
not the default, but it doesn't matter because they are all powered
off, anyway.  The processor then can drive AX5043\_PWR\_CTL\_N low to
enable the power to all AX5043s.  The processor can then drive the
individual AX5043 enables high to power them on.  Then the processor
can drive PWR\_FLAG\_SSPA low to power on the PA and LNA_ENABLE low to
enable the LNA.

There is another watchdog on the board.... FIXME - write this if
necessary.

Add TX Power Measurement description.

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
