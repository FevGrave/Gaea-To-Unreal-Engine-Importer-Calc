size = float(input("Enter the scale of the map in Meters: "))
res = float(input("Enter your exported Resolution: "))
maxZ_height = float(input("Enter the highest peak in Meters: "))
z_height = float(input("Enter the highest wanted peak in Meters: "))
hsr = float(input("Enter the Height-Scale Ratio: "))
print("")

# =================================================================

unrealEngineSpecialNumber = 1 / 512
multiplier = maxZ_height / z_height
exportXY = size * 100 / res
zPreExport = z_height / hsr * multiplier
exportZ = zPreExport * 100 * unrealEngineSpecialNumber

# =================================================================

print(f"{exportXY} is your X & Y values to drop in Unreal Engine")
print(f"{exportZ} is your Z value to drop in Unreal Engine")
print("")

input("Press Enter to exit.")
