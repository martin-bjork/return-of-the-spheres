# Drawing routines for the objects

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numbers

import shapes
from math_classes import vectors

CUBE_QUAD_VERTS = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4),
                   (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))

CUBE_EDGES = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
              (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))

CUBE_NORMALS = ([0.0, 0.0, -1.0], [-1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0], [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0], [0.0, -1.0, 0.0])

def cube_points(size):
    ''' Calculates the vertices of a cube of size size.

    Input:  size: The length of the side of the cube,
                must be a positive number.

    Output: A list containing the vertices of the cube,
            represented as lists. '''
    
    assert isinstance(size, numbers.Number), 'Input must be a number'
    assert size > 0, 'Input must be a positive number'
    
    h = size/2.0
    return [[h, -h, -h],  [h, h, -h],
            [-h, h, -h],  [-h, -h, -h],
            [h, -h, h],   [h, h, h],
            [-h, -h, h],  [-h, h, h]]


def cube(cube):
    ''' The drawing routine for a Cube object.

    Input:  cube: A Cube object

    Calls OpenGL to draw the cube. '''
    
    assert isinstance(cube, shapes.Cube), \
           'Input must be a Cube object'

    points = cube_points(cube.get_side())

    ambient, diffuse, specular, \
             shininess = cube.get_material_properties()

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMateriali(GL_FRONT, GL_SHININESS, shininess)
    #glMaterialfv(GL_FRONT, GL_EMISSIVE, emissive)
    #glColor3fv(cube.get_color())
    glBegin(GL_QUADS)
    for face in CUBE_QUAD_VERTS:
        glNormal3fv(CUBE_NORMALS[CUBE_QUAD_VERTS.index(face)])
        for vert in face:     
            glVertex3fv(points[vert])
    glEnd()

    # TODO: Use something like "cube.get_line_color()" instead?
    glColor3f(0.0, 0.0, 0.0)    
    glBegin(GL_LINES)
    for line in CUBE_EDGES:
        for vert in line:
            glVertex3fv(points[vert])
    glEnd()

def surface(surface):
    ''' The drawing routine for a Surface object.

    Input:  surface: A Surface object

    Calls OpenGL to draw the surface. '''

    # TODO: Tesselate the surface for better lighting effects
    
    assert isinstance(surface, shapes.Surface), \
           'Input must be a Surface object'

    ambient, diffuse, specular, \
             shininess = surface.get_material_properties()

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMateriali(GL_FRONT, GL_SHININESS, shininess)
    #glMaterialfv(GL_FRONT, GL_EMISSIVE, emissive)
    
    points = surface.get_points()
    #glColor3fv(surface.get_color())
    glBegin(GL_QUADS)
    glNormal3fv(surface.get_normal().value)
    for point in points:
        glVertex3fv(point.value)
    glEnd()

    # TODO: The lines don't seem to be drawn, why? Fix.
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for i in range(len(points)):
        glVertex3fv(points[i].value)
        glVertex3fv(points[(i+1)%len(points)].value)
    glEnd()

def sphere(sphere):
    ''' The drawing routine for a Sphere object.

    Input:  surface: A Sphere object

    Calls OpenGL to draw the sphere. '''
    
    assert isinstance(sphere, shapes.Sphere), \
           'Input must be a Sphere object'
    
    ambient, diffuse, specular, \
             shininess = sphere.get_material_properties()

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMateriali(GL_FRONT, GL_SHININESS, shininess)
    #glMaterialfv(GL_FRONT, GL_EMISSIVE, emissive)
    
    #glColor3fv(sphere.get_color())
    glutSolidSphere(sphere.get_radius(), 10, 10)
    #glutSolidSphere(sphere.get_radius(), 40, 40)
    #glutSolidTeapot(sphere.get_radius())
