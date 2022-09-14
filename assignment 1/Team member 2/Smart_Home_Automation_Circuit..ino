int sensorValue = 0;
int greenled = 6;
int redled = 8;
int buzzer_pin = 11;
int sen1Value = 0;
int A;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin,INPUT);
  return pulseIn(echoPin,HIGH);
}
void setup()
{
   Serial.begin (9600);
   pinMode(11, OUTPUT);
   pinMode(6, OUTPUT);
   pinMode(8, OUTPUT);
   pinMode(4, INPUT);
   pinMode(12, OUTPUT);
   pinMode(13, OUTPUT);
   pinMode(A1, INPUT);
}

void loop()
{ 
  //-----Gas Sensor-----//
//----------------------------------
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);

  if(sensorValue > 100)
  {
    digitalWrite (buzzer_pin, HIGH);
    digitalWrite (redled, HIGH);
  }
  else
  {
    digitalWrite (buzzer_pin, LOW);
    digitalWrite (redled, LOW);
  }
  delay(1000);
  
//--------------------------------------------
  //---------UltrasonicDistance----------//
//--------------------------------------------
  sen1Value = 0.01723*readUltrasonicDistance(3,2);
  
  if(sen1Value<10)
  {
    Serial.print(" ||Door Open! ; Distance = ");
    Serial.print(sen1Value);
    digitalWrite (buzzer_pin, HIGH);
    digitalWrite (greenled, HIGH);
  }
  else
  {
    Serial.print(" ||Door Closed! ; Distance = ");
    Serial.print(sen1Value);
    digitalWrite (buzzer_pin, LOW);
    digitalWrite (greenled, LOW);
   }
  delay(1000);
 
//---------------------------------------------------
   //-------------PIR sensor-----------------//
//----------------------------------------------------
  if (digitalRead(4)==1)
  {
    digitalWrite(12,HIGH);
    delay(1000);
  }
  else
  {
    digitalWrite(12,LOW);
    delay(100);
  }
//-------------------------------------------------
   //--------------Temp Sensor-----------------//
//--------------------------------------------------
  A = analogRead(A1);
  Serial.println(A);
  delay(1000);
  
  if(A >= 180)
  {
    digitalWrite(13, 1);
  }
  else
  {
    digitalWrite(13, 0);
  }
  
}
      

