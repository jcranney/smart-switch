# smart-switch

Simple devices in your home like lights and garden taps can be fun and rewarding to "smartify". Setting your garden lights to come on at sunset and turn off 3 hours later is immensely satisfying, but the beauty is shattered when you are having a dinner party and the lights flick off, and to turn them back on you need to go and find your phone to switch them back on. Sensors can help aleviate the problem, but there will always be edge cases where a good old fashioned switch is the best solution.

I looked up "smart switches" online and was confused and overwhelmed by the price and complexity of the commercial off-the-shelf solutions. So, to combat this confusion, I have set out on a long and arduous mission to build a simple, cheap, and dare-I-say, pretty, solution.

## Design reference missions
 A) I'm lying in bed and remember that I've left the garden lights on. The lights are controlled by an ESPHome relay and can be switched on and off by posting to a locally hosted MQTT broker on the topic `/lights/garden/on` and `/lights/garden/off` respectively. I reach to the side of my bedside table where I have a row of 4 switches and flick off the 3rd one which is labelled "garden lights".

 B) I'm in the workshop and want to run the sprinklers in the vege patch for 15 minutes. I walk over to the switch panel near the door and flick the 2nd switch which has the top labelled "garden 15 min" and the bottom labelled "off". I flick the switch up, and the sprinklers run for 15 minutes. While they are running, a faint LED indicates that the switch is in the "top" state, but when the taps turn off automatically in 15 minutes time, the LED flicks back down to the bottom light, indicating that they are off.

 C) I have a guest over and they walk past my array of switches in the sitting room without being offended by their sight.

## Top Level Requirements
 1) The switch shall be compact, such that 8 switches in a row shall take up a width of less than 200 mm and height of 80 mm.
 2) The switches shall be modular, such that they can be replaced easily if they fail or if a new version is manufactured.
 3) The switches shall be non-offensive to any of the senses. 
 4) The switches shall be cheap, each unit costing less than $10 (goal $5).
 5) The switches should interact with an MQTT broker via the internet to publish their state, and to subscribe to the state of the variable they control.

## Derived Requirements
 1.1) An individual switch shall have a footprint of less than 25 mm x 80 mm (W x H).
 
 3.1) The switches should have LEDs to indicate the state of the swtiches, but the brightness of the LED should be configurable via MQTT topic (or similar), with the minimum brightness being fully off.
 3.2) The switches must be silent, except when actuated when they may produce a tactile click or similar.

 4.1) The switch body should be made primarily of cheap materials, preferably 3d printed PLA/PETG.

 5.1) The switches themselves do not need to have wifi, but they should link to a wifi device that publishes the swtich events to an MQTT broker, and subscribes to MQTT topics regarding the state of the switch LEDs.

## Design Notes
 MECH-1) all of the `v0.*` versions have the same mechanical design principle. Flexures are used to constrain a captured rocker switch to the nominal "centre" position, but allow enough motion for the rocker hammer to press a small tacticle switch mounted onto a PCB with a 90 degree bend. Two of these tactile switches will sit on opposite sides of the hammer.
 MECH-2) the flexure springs are stiffer than I expected, so the main difference between `v0.2`->`v0.5` is tweaks to the flexure springs.
