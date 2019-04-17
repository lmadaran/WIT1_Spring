# Creating Sprites and Controlling Sprites

Now that you are familair with uploading and image and making it move. Lets dive more into the concept. 

**Sprites** : a computer graphic whic may be moved on-screen and otherwise manipulated as a single entity

Consider the sprite as an object. An objects hold properties such as width, height color and methods such as jump, hide, speed up. 
This is similar to objects and classes in Python. 

This means that by implementing a sprite we have to use `Object Orientated Programming`. 

## Object Oriented Programming 

> Group related variables and functions into a unit and that unit is called an object
> The varibales are properties
> The functions are methods 

## Classes

> A class is a code template for creating objects. Objects have member variables and have behaviour associated with them. 
> In python a class is created by the keyword class. 


```
class xmen:
    x_one = 'Professor X'
    x_ability = 'Mind Control'
     
x1 = xmen()
x2 = xmen()
print(x1.x_one)
print(x1.x_ability)
```
Now that we remeber what classes and objects are lets apply to Pygame 

## Create a Sprite 

From our previous class we are going to make our spaceship shoot space bullets
To code that we will need to do following:

- Upload an image 
- Create a class and objects 
- Create a function 
- Give the function a Key input 
