const int numSensores = 3; // Cambia según la cantidad de sensores que tengas
int valores[numSensores];

#define pumpPin 6
 


void setup() {


  Serial.begin(9600);

  pinMode(pumpPin, OUTPUT);
  digitalWrite(pumpPin, LOW);


}


 


void loop() {


  Serial.print("Analog inputs: ");

  readSensors();

  Serial.print(valores[0]);
  Serial.print(",");
  Serial.print(valores[1]);
  Serial.print(",");
  Serial.print(valores[2]);

  Serial.println();


  delay(500);

  if(valores[0]<80 &&  valores[1]<80 && valores[2]<80){
    digitalWrite(pumpPin, HIGH);
    delay(100);
    }


}


//  This function returns the analog data to calling function


int readSensors() {
    for (int i = 0; i < numSensores; i++) {
    valores[i] = analogRead(A0 + i);
    valores[i] = map(valores[i], 0, 1023, 0, 100);// Lee el valor del pin A0, A1, A2, etc.
  }
}