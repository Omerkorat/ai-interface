#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This file currently plots a canvas with a map. 
Eventually, we will want to integrate this function into the rest 
of the interface as a callable function draw_map(), which displays
a map on the GUI."""


from __future__ import division

from math import sqrt

from tkinter import *
import PIL
from PIL import ImageTk, Image, ImageGrab

from tkinter import Tk, Canvas, Frame, BOTH, Label
from tkinter import Image as TkImage
import numpy as np
import math

# Constants:

BACKGROUND_COLOR = "white"
WALL_WIDTH = 5
DOOR_LENGTH = 20
HEIGHT, WIDTH = 1500, 800 # Canvas dimensions
CANVAS_MID_X = WIDTH / 2
CANVAS_MID_Y = HEIGHT / 2

# API:




class MapFrame(Frame):
        
    def show(self):
        self.master.title("Some-title")
        self.pack(side=BOTTOM, expand=0)
        canvas.pack(side=LEFT, expand=0)
        root.mainloop()

    def draw_wall(self, x1, y1, x2, y2, color):
        wall = Wall((x1, y1), (x2, y2), color)
        wall.draw()

    def draw_rect_room(self, name, x1, y1, x2, y2, wall_color, background_color, doors, angle=0):
        room = RectRoom(x1, y1, x2, y2, wall_color, background_color, doors, angle)
        room.draw()
        self.objs[name] = room

    def draw_polygon_room(self, name, points, wall_color, background_color, doors):
        room = PolygonRoom(points, wall_color, background_color, doors)
        room.draw()
        self.objs[name] = room

    def open_door(self, room_name, door_ind):
        room = self.objs[room_name]
        room.open_door(door_ind)

    def close_door(self, room_name, door_ind):
        room = self.objs[room_name]
        room.close_door(door_ind)

    def change_wall_color(self, room_name, wall_ind, new_color):
        room = self.objs[room_name]
        room.walls[wall_ind].change_color(new_color)
        for door in room.doors:
            door.draw()

    def add_image(self, path, x, y, basewidth):
        # Example how to show image:
        image = Image.open(path)

        # Scale
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(image)
        root.one = photo
        canvas.create_image(x, y, image=photo)
    
    # internal:
    
    def __init__(self):
        super().__init__()
        self.objs = {}
    
    
    
##########################################################


def rotate(points, angle, center):
    """Rotate a set of points in given angle relative to given
    center."""
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points


def find_slope(p1, p2):
    """Find slope between two points"""
    if (p2[0] - p1[0]) == 0:
        return float('inf')
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def find_dx(magnitude, slope):
    """Find the new x value that results from moving with given magnitude and slope."""
    sign = magnitude/abs(magnitude)
    return sign*(sqrt(magnitude ** 2 / (slope ** 2 + 1))) if slope != float('inf') else 0


root = Tk()
root.title("Join")
map = MapFrame()
canvas = Canvas(map)
root.geometry("%dx%d" % (HEIGHT, WIDTH))
canvas.configure(background=BACKGROUND_COLOR)

class MapObject:
    pass


class Wall(MapObject):
    def __init__(self, p1, p2, color):
        (self.x1, self.y1), (self.x2, self.y2), self.color = p1, p2, color

    def change_color(self, new_color):
        self.color = new_color
        self.draw()

    def draw(self):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=WALL_WIDTH)


# Older implementation of door. Feel free to delete.
class Door2(MapObject):
    def __init__(self, x1, y1, x2, y2, color, background_color, angle):
        self.x1, self.y1, self.x2, self.y2, self.color, self.background_color, self.angle = x1, y1, x2, y2, color, background_color, angle

    def draw(self):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=WALL_WIDTH)

    def open(self):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.background_color, width=WALL_WIDTH)
        if self.angle == 90:
            canvas.create_line(self.x1 - DOOR_LENGTH / 4, self.y1, self.x1 + DOOR_LENGTH / 4, self.y2, fill=self.color,
                               width=WALL_WIDTH)
            canvas.create_line(self.x2 - DOOR_LENGTH / 4, self.y1, self.x2 + DOOR_LENGTH / 4, self.y2, fill=self.color,
                               width=WALL_WIDTH)
        elif self.angle == 180:
            canvas.create_line(self.x1, self.y1 - DOOR_LENGTH / 4, self.x1, self.y1 + DOOR_LENGTH / 4, fill=self.color,
                               width=WALL_WIDTH)
            canvas.create_line(self.x2, self.y2 - DOOR_LENGTH / 4, self.x2, self.y2 + DOOR_LENGTH / 4, fill=self.color,
                               width=WALL_WIDTH)

    def close(self):
        self.draw()


class Door(MapObject):
    def __init__(self, point, slope, color, background_color):
        """
        
        @param point: starting point
        @param slope: slope in which to draw a DOOR_LENGTH line.
        @param color: color of the door itself.
        @param background_color: color of the floor on which the door stands (which is shown when the door is open).
        """
        self.slope, self.color, self.background_color = slope, color, background_color

        slope_sign = slope / abs(slope) if slope not in (0, float('inf')) else 1
        slope = abs(slope)

        # Find end point of door
        a = self.find_dx(DOOR_LENGTH)
        b = a * slope if slope != float('inf') else DOOR_LENGTH
        
        # Create door's coordinates (it's a line going from (x1,y1) to (x2,y2)
        self.x1, self.y1, self.x2, self.y2 = point[0], point[1], point[0] + a, point[1] + b * slope_sign

        self.is_open = False

    def draw(self):
        if self.is_open:
            self.open()
        else:
            self.close()

    def close(self):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                           width=WALL_WIDTH,
                           fill=self.color)
        self.is_open = False

    def open(self):
        # First cover door in a line with color background_color
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.background_color, width=WALL_WIDTH)

        # Then create two lines, each 1/4 of the door's length, at the two sides of the door 
        magnitude = DOOR_LENGTH / 4 # magnitude of on open side of door
        dx = self.find_dx(magnitude)
        dy = dx * self.slope if self.slope != float('inf') else magnitude
        canvas.create_line(self.x1, self.y1, self.x1 + dx, self.y1 + dy, fill=self.color,
                           width=WALL_WIDTH)
        canvas.create_line(self.x1 + 3 * dx, self.y1 + 3 * dy, self.x2, self.y2, fill=self.color,
                           width=WALL_WIDTH)
        self.is_open = True

    def find_dx(self, magnitude):
        return find_dx(magnitude, self.slope)


class Room(MapObject):
    """Room interface."""
    doors, walls = [], []
    
    def __init__(self, *args):
        pass
    
    def draw(self):
        self.draw_walls()
        self.draw_doors()
    
    def open_door(self, ind):
        self.doors[ind].open()

    def close_door(self, ind):
        self.doors[ind].close()

    def change_wall_color(self, ind, new_color):
        self.walls[ind].change_color(new_color)

class RectRoom(MapObject):
    """Older implementation. Older argument format. Might be useless."""
    def __init__(self, x1, y1, x2, y2, wall_color, background_color, doors, angle=0):
        """Doors format: (door_wall, door_offset, door_color)"""
        self.wall_color, self.background_color, self.door_vars = wall_color, background_color, doors

        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.doors = []
        super().__init__(self)

    def draw(self):
        canvas.create_rectangle(self.x1 + WALL_WIDTH, self.y1 + WALL_WIDTH, self.x2 + WALL_WIDTH, self.y2 + WALL_WIDTH,
                                outline=self.wall_color,
                                fill=self.background_color, width=WALL_WIDTH)

        for wall, offset, color in self.door_vars:

            if wall == "N":
                door = Door2(self.x1 + offset, self.y1 + WALL_WIDTH, self.x1 + offset + DOOR_LENGTH,
                             self.y1 + WALL_WIDTH, color, self.background_color, 90)
            elif wall == "S":
                door = Door2(self.x1 + offset, self.y2 + WALL_WIDTH, self.x1 + offset + DOOR_LENGTH,
                             self.y2 + WALL_WIDTH, color, self.background_color, 90)
            elif wall == "W":
                door = Door2(self.x2 + WALL_WIDTH, self.y2 - offset - DOOR_LENGTH, self.x2 + WALL_WIDTH,
                             self.y2 - offset, color, self.background_color, 180)
            elif wall == "E":
                door = Door2(self.x1 + WALL_WIDTH, self.y1 + offset + DOOR_LENGTH, self.x1 + WALL_WIDTH,
                             self.y1 + offset, color, self.background_color, 180)

            else:
                print("Door should be along one of the walls")
                raise ValueError

            self.doors.append(door)
            door.draw()


class PolygonRoom(Room):
    """Draws a polygon room with a list of points and doors."""
    def __init__(self, points, wall_color, background_color, doors):
        """Doors format: (wall_id, offset, door_color). Offset is the number of pixels
        that are between the door's start and the wall's start. So for example if 
        offset is 1/2 the wall's size, then the door will start at the middle of the wall."""
        self.points, self.wall_color, self.background_color, self.door_vars = points, wall_color, background_color, doors
        self.points.append(points[0])
        super().__init__(self)
    def draw_walls(self):
        # Draw walls:
        for i in range(len(self.points) - 1):
            p1, p2 = self.points[i], self.points[i + 1]
            wall = Wall(p1, p2, self.wall_color)
            wall.draw()
            self.walls.append(wall)

        # This makes the walls look smoother
        canvas.create_polygon(self.points, outline=self.wall_color, fill=self.background_color, width=WALL_WIDTH)
        

    def draw_doors(self):
        """Draws all the doors. Not the most elegant implementation maybe, 
        so feel free to change it if you have a better idea. But I think it works."""
        for ind, offset, color in self.door_vars:
            
            # Points and slope of the wall on which the door lies
            wall = self.walls[ind]
            x1,y1 = wall.x1,wall.y1
            x2,y2 = wall.x2,wall.y2
            p1, p2 = (x1,y1), (x2,y2)
            m = find_slope(p1, p2) # slope of the door and wall
            
            # Find starting coords of the door
            dx = find_dx(offset, m)
            start_x = x1+dx
            start_y= y1+(m*dx if m<float('inf') else offset)
            
            # Create door and draw it 
            door = Door((start_x, start_y), m, color, self.background_color)
            self.doors.append(door)
            door.draw()



def main():
    
    # Example of rectangular room, old implementation:
    # map_w.draw_rect_room("control-room", 0,0, 120, 120, "blue", "red",
    # [("W", 50, "red"), ("N", 50, "green"), ("S", 50, "green"), ("E", 50, "green")], angle=0)
    # map_w.open_door("control-room", 0)
    # map_w.open_door("control-room", 1)
    # map_w.open_door("control-room", 2)
    # map_w.open_door("control-room", 3)
    # map_w.add_image("Icon.png", 200,80, 40)


    # Example of polygon room:
    map.draw_polygon_room("engine-room", [(50, 50), (50, 120), (80, 160), (120, 120), (120, 50)], "blue", "red",
                            [
                                [0, 10, "green"],
                                [1, 10, "green"],
                                [2, 10, "green"],
                                [3, -40, "green"],
                                [4, -40, "green"],
                            ])
    map.open_door("engine-room", 0)
    map.open_door("engine-room", 1)
    map.open_door("engine-room", 2)
    map.open_door("engine-room", 3)
    
    # Closes the doors:
#     map_w.close_door("engine-room", 0)
#     map_w.close_door("engine-room", 1)
#     map_w.close_door("engine-room", 2)
#     map_w.close_door("engine-room", 3)

    map.change_wall_color("engine-room", 2, "yellow")

    map.show()
    


if __name__ == '__main__':
    main()
