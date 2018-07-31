# Cisco BB assignments 

### By: Francisco Rojo (Optus)

## Assignment Level 1 [1]  (30/7/2018)
- Run "python3 bblevel1_assignment.py" to list even numbers given:
numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
#### Output:
$ python3 bblevel1_assignment.py 
2018-07-31 15:28:17.197191
[402, 984, 360, 408, 980, 544, 390, 984, 592, 236, 942, 386, 462, 418, 344, 236, 566, 978, 328, 162, 758, 918, 412, 566, 826, 248, 866, 950, 626, 104, 58, 512, 24, 892, 894, 742, 958, 842, 688, 854, 440, 380, 126, 328, 470]

## Devnet Lab - Intro to Python - Part 1 [2]  (31/7/2018)
- Run "bblevel1_part1_hands_on_exercise.py"
#### Output:
$ python3 bblevel1_hands_on_exercise.py 
pi is a  <class 'float'> with a value of  3.141592653589793
257  is greater than 50
The Fruit is  Yellow
12  x  96  =  1152
48  x  17  =  816
196523  x  87323  =  17160977929

## Devnet Lab - Intro to Python - Part 2 [3]   (31/7/2018)
- Run "bblevel1_part2_fortune_cookie.py"
#### Output:
$ python3 bblevel1_part2_fortune_cookie.py 
Get your fortune cookie
How many lucky numbers would you like? : 2

Here is your fortune:

Keep trying, next time may work
Lucky Numbers: [261, 167]

## Devnet Lab - Json Intro - [4]   (31/7/2018)
- Run "bblevel1_nested_data.py" 
- Input file: bblevel1_interfaces.json
#### Output:
$ python3 bblevel1_nested_data.py 
<path>/cisco-bb
GigabitEthernet1 : 198.18.134.11 255.255.192.0
GigabitEthernet2 : 172.16.255.1 255.255.255.0
Loopback0 : 10.0.0.1 255.255.255.255


Sources:
- [1] https://github.com/Devanampriya/BB_Level1/blob/master/Assignment.md
- [2] https://learninglabs.cisco.com/tracks/devnet-beginner/intro-python/intro-python-part1/step/6
- [3] https://learninglabs.cisco.com/tracks/devnet-beginner/intro-python/intro-python-part2/step/7
- [4] https://learninglabs.cisco.com/tracks/devnet-beginner/intro-python/parsing-json-python/step/4