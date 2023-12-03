with open("input.txt", "r") as input_file:
  total = 0
  for line in input_file:
      x = line.split(":")
      y = x[1].split(";")
      game_num = x[0].split()[1]

      blue_num = 0
      red_num = 0 
      green_num = 0

      for z in y:
        value = z.split(",")
        for w in value:
          color = w.split()
          if color[1] == "blue":
            new_blue = int(color[0])
            if blue_num < new_blue:
              blue_num = new_blue
          if color[1] == "red":
            new_red = int(color[0])
            if red_num < new_red:
              red_num = new_red          
          if color[1] == "green":
            new_green = int(color[0])
            if green_num < new_green:
              green_num = new_green
        
      print("red = ", red_num, "green = ", green_num, "blue = ", blue_num)
      total_round = red_num * green_num * blue_num
      total += total_round
      print("********************* total = ", total_round)

  print("total = ",  total)

              