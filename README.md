A python generator for creating modular box in openSCAD

Created mostly for organizers for board games, but can be used elsewhere just as successfully.

overview of the classes hierarchy:

![](pic/class_hierarchy.png)

Implemented interiors for boxes are:

Bowl (parameters for the example on the picture):<br>
 width = 50,<br>
 height = 75,<br>
 depth = 20<br>
![](pic/bowl.png)
    
Column:<br>
 diameter = 7.5,<br>
 depth = 13,<br>
 segments = 6<br>
![](pic/column.png)

Cube:<br>
 width = 26,<br>
 height = 105,<br>
 depth = 31<br>
![](pic/cube.png)

Pipe:<br>
 diameter = 25,<br>
 height = 105,<br>
 depth = 31<br>
![](pic/pipe.png)

SeparateTokensHolder:<br>
  token = Pipe(23,10,16),<br>
  amount = 3,<br>
  depth = 21,<br>
  separator = 4<br>
![](pic/separateTokensHolder.png)

VariousTokensHolder:<br>
 tokens = [Cube(22,22,22),
              Bowl(27, 27, 55),
              Pipe(27, 27, 23),
              Column(10,10)]<br>
 depth = 24<br>
 separator = 0.4<br>
![](pic/variousTokensHolder.png)<br>
(note that bottom of the Bowl got cut, as the VariousTokensHolder is shallower than the Bowl)

interiors (above) can be put into PlainBox:<br>
(VariousTokensHolder from before is used here)<br>
![](pic/plainBox.png)

the plainBox also comes with 2 options for the top:<br>
regular (also used above with the VariousTokensHolder):<br>
![](pic/regular_top.png)

chamfered (useful mostly with rectangular tops, e.g. for easier cards inserting)<br>
![](pic/chamfered_top.png)

Box can be put into:<br>
WithJoints:<br>
![](pic/withJoints.png)<br>
joints are used to connect boxes together.

WithRoundedCorners:<br>
(this time with Cube(100,20,30))<br>
![](pic/withRoundedCorners.png)

WithVerticalHoles:<br>
(I've exchanged width with height from the previous cube, as the finger holes are in the middle, of the height wall)<br>
![](pic/withVerticalHoles.png)<br>
notice, that the floor is thickened in this Box, as the middle was too wiggly without it)

WithHorizontalHole:<br>
![](pic/withHorizontalHole.png)

notice the order! If you put WithRoundedCorners to e.g.WithJoints type, it's gonna end up exactly what you asked for:<br>
![](pic/withJointsWithRoundedCorners.png)

so you probably want to put object WithJoints into the WithRoundedCorners one:<br>
![](pic/withRoundedCornersWithJoints.png)
 



