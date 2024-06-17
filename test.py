def conversor_to_decimal(hex_color):
    red_light = hex_color[0:2]
    green_light = hex_color[2:4]
    blue_light =  hex_color[4:6]

    red_light = int(red_light, 16)
    green_light = int(green_light, 16)
    blue_light =  int(blue_light, 16)

    rgb = [red_light, green_light, blue_light]

    return(rgb)

print(conversor_to_decimal("ff0228"))

