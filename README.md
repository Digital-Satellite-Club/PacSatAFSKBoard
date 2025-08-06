# PacSatAFSKBoard
Hardware design for the PacSat AX5043 based board

This repository contains a board design for use in satellites for
packet message storing and forwarding and for general control.

It has a TMS570LS0914PGE processor for control and packet handling.
It uses 5 AX5043 chips for the radio interfaces, four receive channels
(uplinks) and one transmit channel (downlink).  Operation is full
duplex with receive on 144-148MHz and transmit on 430-440MHz.

Though it is designed for packet satellite, the design can be used for
any sort of full duplex dual band AFSK radio operation with or without
FM.  The AX5043 supports a large number of AFSK protocols (if you can
figure out how to program it).

With some filter redesign it could support a number of different
bands, too, maybe even up to 1280MHz.

The board also has MRAM storage for persistent data storage and an
RTC for timekeeping.  There's space on the board to add more things.

The board has a CAN interface and a serial interface on top of the
radio interfaces for interfacing to other boards in the system.

Output power is about 2 watts.  It has the ability to measure forward
and reflected power on the output.
