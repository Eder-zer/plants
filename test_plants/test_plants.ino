const int numSensores = 3; // Cambia según la cantidad de sensores que tengas
int valores[numSensores];
String Msg;

#define pumpPin 6

void setup() {

  Serial.begin(9600);
  pinMode(pumpPin, OUTPUT);
  digitalWrite(pumpPin, LOW);

}


void loop() {

  checkSerialOperations();
  sendAnalogJson();

  delay(500);

  // Generar modo auto
  if(valores[0]<80 &&  valores[1]<80 && valores[2]<80){
    digitalWrite(pumpPin, HIGH);
    delay(100);
    }


}


// Send analog sensor data as json
void sendAnalogJson(){
  // {"Analog inputs":[A0, A1, A2]}
  readAnalogSensors();

  Serial.print("{'Analog inputs':[");

  Serial.print(valores[0]);
  Serial.print(",");
  Serial.print(valores[1]);
  Serial.print(",");
  Serial.print(valores[2]);

  Serial.print("]}");

  Serial.println();

}

// Read Analog inputs and update array 0-100%
void readAnalogSensors() {
    for (int i = 0; i < numSensores; i++) {
    valores[i] = analogRead(A0 + i);
    valores[i] = map(valores[i], 0, 1023, 0, 100);// Lee el valor del pin A0, A1, A2, etc.
  }
}

void checkSerialOperations()
{
  while (Serial.available()!=0)
  {
    Msg = Serial.readString();
    Msg.trim();
    if (Msg == "pump_on")              //***
      {
      digitalWrite(pumpPin, HIGH);
      } // Write read serial operations here
  }
}