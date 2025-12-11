while(1)
 {
 // Check DIP Switch #3. If pressed (== 0), blink LED 0 instead of running the
counter.
 // NOTE: This logic assumes the counter ONLY runs if the switch is NOT
pressed.
 if(DSK6713_DIP_get(3) == 0)
 {
 DSK6713_LED_toggle(0);
 DSK6713_waitusec(200000);
 }
 else:
     
 RING
     {
 int i;
 for (i = 0; i < 4; i++) {
 DSK6713_LED_on(i); // Turn ON the current LED
 DSK6713_waitusec(200000); // Wait 0.2 seconds
 DSK6713_LED_off(i); 
 }
 
 JHONSON
 while(1){
 int i;
 for(i=0;i<4;i++)
 {  DSK6713_LED_on(i);
    DSK6713_waitusec(200000);}
 for(i=0;i<4;i++)
 {  DSK6713_LED_off(i);
    DSK6713_waitusec(200000);}
 }
 