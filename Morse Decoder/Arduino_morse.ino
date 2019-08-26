const int ledGreen = 8;           // Indicates break
const int ledYellow = 7;           // Indicates dot
const int ledRed = 6;             // Indicates dash
const int buttonPin = 2;          // button

// Variables will change:
int buttonState;             // the current reading from the input pin
int lastButtonState = HIGH;   // the previous reading from the input pin

int startPressed = 0;
int endPressed = 0;
int pauseTime = 0;
int message = 0;
int holdTime = 0;



// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers
unsigned long pause = millis(); 
unsigned long holddown = 0;

int T = 300;

//-----------------SETUP---------------------------------------

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


//--------------------- Helpfunctions--------------------------

void morse(){
  if (buttonState == LOW){
    
    digitalWrite(ledGreen, HIGH);
    digitalWrite(ledYellow, LOW);
    digitalWrite(ledRed, LOW);
    
    startPressed = millis();
    pauseTime = startPressed - endPressed;

    //Short pause
    if (pauseTime <= T) {
      message = 1;
    }
    //Medium pause
    if (pauseTime > T && pauseTime <= 3*T) {
      message = 2;
    }
    //Long pause
    if (pauseTime > 3*T) {
      message = 3;
    }
    
  }

  else{
    digitalWrite(ledGreen, LOW);

    endPressed = millis();
    holdTime = endPressed - startPressed;

    //Short press - dot
    if(holdTime<=T){
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledYellow, HIGH);
      digitalWrite(ledRed, LOW);

      message = 4;
    }

    //Long press - dash
    if(holdTime>T){
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledYellow, LOW);
      digitalWrite(ledRed, HIGH);

      message = 5;
    }
  }

  Serial.print(message);
}





//--------- Loop-----------------------------------------------
void loop(){
 buttonState = digitalRead(buttonPin);

  if (buttonState != lastButtonState) {
    morse();
  }
  
  delay(20);    //Debounce

  lastButtonState = buttonState;
  
}
