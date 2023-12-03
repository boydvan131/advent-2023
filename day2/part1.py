with open("input.txt", "r") as input_file:
  total = 0
  for line in input_file:
      x = line.split(":")
      y = x[1].split(";")
      game_num = x[0].split()[1]

      for z in y:
        blue_num = 0
        red_num = 0 
        green_num = 0

        value = z.split(",")
        for w in value:
          color = w.split()
          if color[1] == "blue":
            blue_num = int(color[0])
          if color[1] == "red":
            red_num = int(color[0])
          if color[1] == "green":
            green_num = int(color[0])

        print("Blue = ", blue_num, "red = ", red_num, "green = ", green_num)

        if blue_num > 14 or red_num > 12 or green_num > 13:
          print("too high")
          print("*********************")
          total -= int(game_num)
          break

      game = x[0].split()[1]  
      print(game)
      total += int(game)
      print("********************* total = ", total)

  print("total = ",  total)