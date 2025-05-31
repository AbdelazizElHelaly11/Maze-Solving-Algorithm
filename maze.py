from pyamaze import maze , COLOR
m = maze (20,20)
m.CreateMaze(1,1, 
            loopPercent= 70 , 
            saveMaze = True ,
            theme = COLOR.light)

m.run()