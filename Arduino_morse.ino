const int ledGreen = 8;           // Indicates break
const int ledYellow = 7;           // Indicates dot
const int ledRed = 6;             // Indicates dash
const int buttonPin = 2;          // button

// Variables will change:
int ledState = HIGH;         // the current state of the output pin
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin

// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers


void setup(){
  pinMode( ledGreen, OUTPUT );    // Pin 8 is an output
  pinMode( ledYellow, OUTPUT );    // Pin 7 is an output
  pinMode( ledRed, OUTPUT );    // Pin 6 is an output
  pinMode( buttonPin, INPUT);   // Takes in values from button
  Serial.begin(9600);            // Important for port output
  
  digitalWrite(ledGreen, HIGH); // set initial LED state
  digitalWrite(ledYellow, LOW); // set initial LED state
  digitalWrite(ledRed, LOW); // set initial LED state
}
 
void loop(){
  // read the state of the switch into a local variable:
  int buttonState = digitalRead(buttonPin); // 0 when pressed

  

  // If the switch changed, due to noise or pressing:
  if (buttonState != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // whatever the reading is at, it's been there for longer than the debounce
    // delay, so take it as the actual current state:

    // if the button state has changed:
    if (buttonState != buttonState) {
      buttonState = buttonState;
    }
  }

  // set the LED:
  digitalWrite(ledPin, ledState);

  // save the reading. Next time through the loop, it'll be the lastButtonState:
  //lastButtonState = buttonState;

  Serial.print(lastDebounceTime);
  delay(100);


  
  
}
