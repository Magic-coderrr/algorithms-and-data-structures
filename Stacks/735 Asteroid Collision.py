# We are given an array asteroids of integers representing asteroids in a row. 
# The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents 
# its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the 
# smaller one will explode. If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.
# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

def asteroidCollision(self, asteroids):
    stack = []
    
    for i in asteroids:
        # Assuming it lives
        survived = True 
        
        # The fight only happens if Stack Top is moving Right (+) and New is moving Left (-)
        while stack and stack[-1] > 0 and i < 0:
            if stack[-1] < -i:
                # New asteroid wins. Pop the stack, let the while loop fight the next one
                stack.pop()

            elif stack[-1] == -i:
                # Mutual destruction. Popping the stack, new asteroid dies, end the fight.
                stack.pop()
                survived = False
                break

            elif stack[-1] > -i:
                # Stack wins. New asteroid dies, end the fight.
                survived = False
                break
                
        # If the new asteroid survives the whole gauntlet, push it!
        if survived:
            stack.append(i)
            
    return stack
    
asteroids = [5,10,-5]
print(asteroidCollision(asteroids))