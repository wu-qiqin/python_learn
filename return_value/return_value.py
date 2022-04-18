"""
Created by hu-jinwen on 2022/4/16
"""


def test_value():
    temp = 30
    wetness = 50
    print("show the value %d" % temp, wetness)

    return temp, wetness


gl_temp, gl_wet = test_value()

print(gl_temp)
print(gl_wet)

