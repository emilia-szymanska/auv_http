# AUV communication via HTTP

## Brief description
The aim of this program is to imitate a communication between an AUV and a processing unit. An AUV sends its (random) position n times with time intervals of t, a PU receives the messages, calculates the velocity and sends it back to AUV.

## Assumptions
* Positions of AUV are generated randomly (minimum value is 0, maximum value is 30, all coordinates are natural numbers),
* Calculated velocity is rounded. 

## Running the code
To run the program after cloning this repository to your computer, run these commands in separate terminals:
```
./server.py
```
```
./client.py time number_of_signals
```
where time should be given in seconds, number\_of\_signals is a natural number.

## Author
* **Emilia Szymanska**
