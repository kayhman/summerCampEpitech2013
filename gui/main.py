import kivy
kivy.require('1.1.1')

from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.clock import Clock

from jnius import autoclass
from time import sleep, time

from kivy.core.window import Window
from kivy.resources import resource_find
from kivy.graphics.transformation import Matrix
from kivy.graphics.opengl import *
from kivy.graphics import *
from objloader import ObjFile
import fastObjLoader


class Renderer(Widget):
    def __init__(self, **kwargs):
        self.canvas = RenderContext(compute_normal_mat=True)
        self.canvas.shader.source = resource_find('simple.glsl')
        super(Renderer, self).__init__(**kwargs)
        with self.canvas:
            self.cb = Callback(self.setup_gl_context)
            PushMatrix()
            self.setup_scene_fast()
            PopMatrix()
            self.cb = Callback(self.reset_gl_context)
        Clock.schedule_interval(self.update_glsl, 1 / 60.)
	self.rotation = 1

    def setup_gl_context(self, *args):
        glEnable(GL_DEPTH_TEST)

    def reset_gl_context(self, *args):
        glDisable(GL_DEPTH_TEST)

    def update_glsl(self, *largs):
        asp = self.width / float(self.height)
        proj = Matrix().view_clip(-asp, asp, -1, 1, 1, 100, 1)
        self.canvas['projection_mat'] = proj
        self.canvas['diffuse_light'] = (1.0, 1.0, 0.8)
        self.canvas['ambient_light'] = (0.1, 0.1, 0.1)
        self.rot.angle += 1 * self.rotation

    def setup_scene_fast(self):
        Color(1, 1, 1, 1)
        PushMatrix()
        Translate(0, 0, -3)
        self.rot = Rotate(1, 0, 1, 0)
        UpdateNormalMatrix()
	start_time = time()
	v, t = fastObjLoader.loadObjFile("monkey.obj")
	stop_time = time()
	print "fast loading last : ", (stop_time - start_time)
        self.mesh = Mesh(
            vertices=v,
            indices=t,
            fmt=[('v_pos', 3, 'float'), ('v_normal', 3, 'float'), ('v_tc0', 2, 'float')],
            mode='triangles',
        )
        PopMatrix()

    def setup_scene_slow(self):
        Color(1, 1, 1, 1)
        PushMatrix()
        Translate(0, 0, -3)
        self.rot = Rotate(1, 0, 1, 0)
	start_time = time()
        self.scene = ObjFile(resource_find("monkey.obj"))
	stop_time = time()
	print "fast loading last : ", (stop_time - start_time)
        m = self.scene.objects.values()[0]
        UpdateNormalMatrix()
        self.mesh = Mesh(
            vertices=m.vertices,
            indices=m.indices,
            fmt=m.vertex_format,
            mode='triangles',
        )
        PopMatrix()
    
    def invert_rotation(self, dummy):
	self.rotation = self.rotation * -1

    def stop_rotation(self, dummy):
	if self.rotation == 0:
	    self.rotation = 1
	else:
	    self.rotation = 0 

class Epitech(Screen):
    noteLabel = ObjectProperty()
    invertButton = ObjectProperty()
    stopButton = ObjectProperty()
    volume = ObjectProperty()
    renderer = ObjectProperty()

    def build(self):
      self.noteLabel.text = "No key pressed"
      self.invertButton.bind(on_press=self.renderer.invert_rotation)
      self.stopButton.bind(on_press=self.renderer.stop_rotation)

class EpitechApp(App):
    def build(self):
        self.game = Epitech(name="game")
        self.game.build()
        return self.game

if __name__ == '__main__':
    EpitechApp().run()
