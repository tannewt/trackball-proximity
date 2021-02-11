# trackball-proximity
Press a keyboard key when your hand is on a trackball

Here is a demo: https://twitter.com/tannewt/status/1359937799173021699

The `code.py` sets D13 to high when the proximity is met. This connects to a [SN74LVC1G3157DBVR](https://www.digikey.com/en/products/detail/SN74LVC1G3157DBVR/296-14908-1-ND/562548) which is an analog mux. It effectively "presses" the LED key switch for me. The Yellow and Blue wires from the keyboard are soldered to the solder joints for the LED key switch.
