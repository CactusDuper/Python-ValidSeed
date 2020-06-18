import struct
worldSeed = int(input())
if worldSeed > 0:
    upperBits = worldSeed >> 32
else:
    upperBits = (worldSeed >> 32)+(2 << 31)
lowerBits = worldSeed & ((1 << 32)-1)
a = (24667315 * upperBits + 18218081 * lowerBits + 67552711) >> 32
b = (-4824621 * upperBits + 7847617 * lowerBits + 7847617) >> 32
seed = 7847617 * a - 18218081 * b
if seed > 0:
    if(((seed * 25214903917 + 11) & ((1 << 48) - 1))) > 0:
        nextLong = ((struct.unpack("@q",struct.pack("@Q",(seed >> 16 << 32)))[0]) + (((seed * 25214903917 + 11) & ((1 << 48) - 1)) >> 16)%-2147483648)
        nextLong2 = ((struct.unpack("@q",struct.pack("@Q",(seed >> 16 << 32)))[0]) + (((seed * 25214903917 + 11) & ((1 << 48) - 1)) >> 16)%2147483648)
if(nextLong != worldSeed):
    if(nextLong2 == worldSeed):
        print("Valid Seed")
    else:
        print("Invalid Seed")
elif(nextLong==worldSeed):
    print("Valid Seed")
