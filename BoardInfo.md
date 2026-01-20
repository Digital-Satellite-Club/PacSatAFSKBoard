# New Board Bring up

Things to do for a new board:

* Add power connector.

* Add watchdog jumper.

* Replace RX AX5043 inductors.  18nH works well.

* Add blue wire for the LNA bias from between R77 and C105 to
  between L32 and C107/108.

* Replace U5 with the proper part.

* Possibly replace R117 with a 15/18K resistor.  The voltage is
  a little low for the AND gate input.  (Testing shows this is
  not necessary, so this doesn't have to be done on prototype
  boards.)

* Replace L35 with a 47pF capacitor.  No need to cut traces or
  anything.  (Higher frequency performance would be improved with a
  43pF capacitor, the 47pF high end starts going down at 436MHz.)
  
* Replace L27 with a 2.7nH inductor.

* Replace C117 with a 18pF capacitor.

* Replace L38 with a 5.8nH inductor.

* Change the PA power input inductor (L37) to a 100nH part with low
  DCR.
  
* Change L30 to a 20nH inductor.

* Change L33 to a 17nH inductor.

* Change C124 to 6.4pF.

* Change C126 to 11pF.

* CHange C128 to 5.4pF.

* Add R112 so the boards can supply/get power from the PC104.

* Cut the OTHER\_HW\_POWER\_OFF\_N line between Q2 and the CPU.  It
  was causing issues.
  
* Remove R80 and R82.  The input impedance of the power measurement
  chip is 50 ohms.
  
* Change the PA power input inductor (L37) to a 100nH 1A part with
  100mOhm DCs.
  
# Current Board Status

## Issues that apply to all boards

* The RTC will only keep time when off for about 10 minutes.  This is
  due to a diode with high leakage and insufficient capacitance.  This
  has been fixed for the next revision of the board, but is not
  currently planned to be fixed for these boards.
  
* The OTHER\_HW\_POWER\_OFF\_N line is cut as it was causing issues
  when resetting another board, it appeared to be pulling down the
  signal when the CPU was off.  So it is not possible to read that
  line.  It's really only valuable for external control, so version
  2 boards are not able to do external control.

* Like the previous entry, the ACTIVE\_N line will be driven low when
  the CPU is in reset.  This will probably not be fixed; I can't think
  of an easy way.

## Board 5 - 2nd board I worked on

* Applied all the board bring up changes.

* It's working well, except for RF transmit power.

* This board has the capacitor on the PA RF input added between
  the L35 inductor and the PA, so the TX\_PA\_DRV input/output
  connector (P13) can be used on this board.
 
* U.FL connector P6 got pulled off the board.

* Currently C124, L30, C125, L33 and L38 are not installed.  I pulled
  them off to measure power out of the PA, and they are pretty much
  destroyed.  L33 and L38 came off when I was unsoldering the other
  devices.
  
* The OTHER\_HW\_POWER\_OFF\_N line is not cut between Q2 and the CPU,
  so until that is done the board cannot be used for active/standby.
  
* Replaced L27 with a 2.7nH part to account for trace inductance.

* Replaced L35 with a 47pF capacitor.

* Replaced L37 with a 100nH 1A inductor.

* Replaced C117 with a 27pF capacitor.

* Replaced L38 with a 5.0nH inductor.

* Replaced L38 with 5.8nH and C117 with 18pF.

* Installed the proper filter components.

* Removed R80 and R82 (50 ohm RF power measurement resistors).

## Board 6 - First board I worked on for initial bringup

* The RF switches have been removed and jumpers places on the RF connections.
  So this is basically a stand-alone board or a board 2.

* The board 2 resistor (R91) is added on this board, so it is a board
  2 board.

* Added a 1nF capacitor between L35 and the RF PA so it's not DC grounded.

* The board usually goes into a reset loop when cold.  It started
  doing this after I put too much voltage in.  This is probably a
  power issue someplace.  Fixing the PA power controller did seem to
  help.  To get it out, you have to let the board warm up a little
  then bring the voltage down and back up until it works.

  The board draws a lot more power than it should.  Something in the
  power section got messed up, it appears.

  The reset loop has stopped happening for some reason, but it's still
  drawing excess power.
  
* The hardware watchdog is disabled by a solder bridge.  I couldn't get
  the wire out of the holes for the jumper.

* MITSI replaced the PA with a new chip because the old one was broken.

* The PA power input inductor (L37) has been changed to 100nH 1A.

* PA output match capacitor (C117) was changed to 68pF.

* C112 between the AX5043 and the PA is currently removed for testing.

* C117 has been changed to a 27pF capacitor.  Inductor L38 is not yet
  changed to 5.8nH, but 6.8nH is close.

* L35 is now a 47pF capacitor for the proper match.  L27 didn't have
  to change.
  
* The serial port connector broke on this as I was trying to replace
  it with a right-angle one.  The part that is there is a TS-103-G-A
  and the pins soldered into the board are not standard size, so the
  replacement didn't work, and the holes are so small you can't
  unsolder them.  That's been fixed on new boards.  I don't see any
  right-angle version of those parts.  I've put on a TS-102-G-A that I
  had, but it doesn't have a ground so the ground had to be handled
  elsewhere.
  
* Removed C125; it's capacitance doesn't seem to be required.
  Parasitic capacitance seems to be enough.
  
* Replaced L27 with a 2.7nH part to account for trace inductance.

* Replaced L38 with a 5.0nH part to account for trace inductance.

* Replaced L30 with a 20nH part to raise the frequency a little.

* Replaces L33 with a 16nH part to raise the frequency a little.

* It appears as part of testing I overheated the PA.  It's not working
  correctly, quiescent current is now around 500ma and I can't
  increase input power to more than 47% of the AX5043 output, and then
  it only puts out about 1W and is drawing 700ma when doing that.  I
  undid all the previous changes, but it even got worse, only .5W
  output.  So everything is back as specified above, but it is what it
  is.
  
* Removed R80 and R82, the 50 ohm resistors on the power measurement
  circuit.  The input impedance of the power measurement chip is 50
  ohms, no need for resistors, which will mess up the impedance.  It's
  working a little better with that change.
  
* Replaced L38 with 5.8nH and C117 with 18pF 5%.

* Re-added C125 as .75pF.

* Changed C124 to 6.4pF

* Changed C126 to 11pF

* Changed C128 to 5.4pF

* Changed L33 to 17nH

* Board is no longer usable, the debug connector came off.

## Board 8 - 3rd board I worked on

* Applied all the board bring up changes.

* It's working well, except for RF transmit power.

* Added the 1nF capacitor on the PA input between L35 and C112, so
  TX\_PA\_DRV cannot be used on this board. (Well, not true any more.)

* The Iref input is modified to match what the datasheet says it
  should be.  Except the 68nH inductor got lost, so I put on an 83nH
  inductor, but that shouldn't matter.  It has Iref going to the
  inductor, then the 240ohm resistor, and the 0.1uF capacitor from above
  the inductor to ground.
  
* Change the L match on the PA input to a 47pf capacitor and a 15nH
  inductor.  This seems to work ok, though per simulation it has more
  loss than the two inductor L match.  This does make TX\_PA\_DRV
  usable.  Note that this is currently wrong on the board, the
  capacitor and inductor are switched places.  The 15nH should go in
  L38's place and the capacitor should go in L27's place.

* R27 and R117 are changed to a 100 ohm and 200 ohm resistor as an
  experiment trying to fix a problem.  It didn't fix the problem, but
  that's not going to hurt anything, so those are left on for now.

* Replaced L27 with a 2.7nH part to account for trace inductance.

* Replaced L35 with a 47pF capacitor.

* The PA power input inductor (L37) has been changed to 100nH 1A.

* Replaced C117 with a 27pF capacitor.

* Replaced L38 with a 5.0nH inductor.

* Removed C125.

* Inductors in the PA output filter are *not* changed yet.

* The PA on this board is not working very well.  It's drawing 500ma
  quiescent, like board 6 is, and it starts oscillating if you put too
  much power into it.  It may be that the Iref changes are botched
  
* C124 and L30 are currently removed for a test.

* C124 and L30 are re-added.

* Re-added C125.  It's necessary for impedance, per simulation.

* Replaced L38 with 5.8nH and C117 with 18pF.

* Removed R105 to disable the RF switches and added a zero-ohm
  resistor to R107.
  
* R79 was changed to a 300 ohm component because I lost the 240 ohm
  component, and I think it was burned up from too much soldering,
  anyway.  I have added a 1.2K resistor in parallel (on top) to get it
  to 240 ohms.
  
* The filter input components and all the PA L matches are pulled out.
  The PA is isolated so it can be characterized.
  
* PA output L match is now 15pF and 5.8nH and seems to work quite
  well.
  
* Input match is now 22pF and 2.7nH.  That changed the output match
  a little, it's now 18pF and 5.8nH.  That again changed the input
  match.  The input match is a little to high at around 90 ohms, but
  it's close enough for that.  That's a VSWR of 1.8.

### Fixed

* The RF power output switch U33 appears to always be connected from
  RF\_OUT\_SWTICH to the antenna output, no matter the setting of
  ACTIVE1\_N.  It's not that way on board 5, so it appears to be the
  switch.  I'm wondering if an over voltage messed it up?  Or maybe
  transmitted power?  But maybe it's working.  If I have a signal
  going out, turning the switch on and off give a 35dB difference in
  power.  This appears to not be an issue.

### Commands

inhibit tx

set tx power 4 100

set tx power 4 50

set tx power 4 35

test freq 4

set gpio 17 1

set gpio 17 0

get power flags

set freq 4 435760

toggle rf power print
